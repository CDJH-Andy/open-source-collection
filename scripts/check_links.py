#!/usr/bin/env python3
"""扫描仓库内的 Markdown 外链并检查可用性。

用法:
    python scripts/check_links.py            # 检查全部
    python scripts/check_links.py --warn-only # 只打印，不返回非零退出码

设计要点:
    - 并发检查，默认 8 个线程，避免被目标站限流
    - 只认 http(s) 链接，忽略锚点、相对路径和内部引用
    - HEAD 失败时自动降级为 GET（部分站点不实现 HEAD）
"""

from __future__ import annotations

import argparse
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")
SKIP_HOSTS = {"img.shields.io"}  # 徽章类链接不稳定，不参与巡检
TIMEOUT = 10
USER_AGENT = "link-checker/1.0 (+https://github.com/CDJH-Andy/open-source-collection)"


def collect_links() -> dict[str, list[str]]:
    """返回 {url: [出现该链接的文件]} 映射。"""
    found: dict[str, list[str]] = {}
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        text = md.read_text(encoding="utf-8", errors="ignore")
        for url in LINK_RE.findall(text):
            url = url.rstrip(".,;")
            if any(host in url for host in SKIP_HOSTS):
                continue
            found.setdefault(url, []).append(str(md.relative_to(ROOT)))
    return found


def check(url: str) -> tuple[str, str, int | None]:
    """返回 (url, 状态描述, HTTP 码)。"""
    for method in ("HEAD", "GET"):
        try:
            req = Request(url, method=method, headers={"User-Agent": USER_AGENT})
            with urlopen(req, timeout=TIMEOUT) as resp:
                return url, "ok", resp.status
        except HTTPError as exc:
            if method == "HEAD" and exc.code in (403, 405, 501):
                continue  # 换 GET 再试
            return url, f"http {exc.code}", exc.code
        except URLError as exc:
            if method == "HEAD":
                continue
            return url, f"unreachable: {exc.reason}", None
        except Exception as exc:  # noqa: BLE001 - 巡检脚本需要兜住所有异常
            return url, f"error: {exc}", None
    return url, "unreachable", None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--warn-only", action="store_true", help="不因死链返回非零退出码")
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()

    links = collect_links()
    if not links:
        print("没有找到任何外链。")
        return 0

    print(f"共发现 {len(links)} 个外链，开始检查……\n")
    broken: list[tuple[str, str, int | None]] = []

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(check, url): url for url in links}
        for future in as_completed(futures):
            url, status, code = future.result()
            if status != "ok":
                broken.append((url, status, code))
                for path in links[url]:
                    print(f"[BROKEN] {url} -> {status}  ({path})")

    if not broken:
        print(f"全部 {len(links)} 个链接均可用。")
        return 0

    print(f"\n发现 {len(broken)} 个异常链接。")
    return 0 if args.warn_only else 1


if __name__ == "__main__":
    sys.exit(main())
