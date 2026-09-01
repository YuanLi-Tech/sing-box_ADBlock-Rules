#!/usr/bin/env python3
"""Convert 1Hosts Lite plain-domain list to sing-box rule-set JSON (source format).

Usage: python3 convert.py <input.txt> <output.json>
"""
import json
import sys


def main() -> None:
    if len(sys.argv) != 3:
        print("usage: convert.py <input.txt> <output.json>", file=sys.stderr)
        sys.exit(1)
    src, dst = sys.argv[1], sys.argv[2]

    domains: list[str] = []
    seen: set[str] = set()
    with open(src, encoding="utf-8", errors="replace") as f:
        for line in f:
            d = line.strip().lower()
            if not d or d.startswith(("#", "!", "[", "0.")) or " " in d:
                continue
            if d.endswith((".local", ".localhost")):
                continue
            if d not in seen:
                seen.add(d)
                domains.append(d)

    with open(dst, "w", encoding="utf-8") as f:
        json.dump({"version": 3, "rules": [{"domain": domains}]}, f,
                  ensure_ascii=False, separators=(",", ":"))
    print(f"converted {len(domains)} unique domains -> {dst}")


if __name__ == "__main__":
    main()
