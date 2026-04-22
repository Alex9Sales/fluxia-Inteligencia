#!/usr/bin/env python3
import json
import os
import sys
from urllib.parse import urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

API_VERSION = os.getenv("META_API_VERSION", "v19.0")
BASE = f"https://graph.facebook.com/{API_VERSION}"


def get_json(url: str):
    req = Request(url, headers={"User-Agent": "OpenClaw-setup-instagram-meta/1.0"})
    with urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    token = os.getenv("INSTAGRAM_ACCESS_TOKEN") or (sys.argv[1] if len(sys.argv) > 1 else None)
    if not token:
        print("Usage: meta_token_check.py <ACCESS_TOKEN>")
        print("Or set INSTAGRAM_ACCESS_TOKEN in the environment.")
        sys.exit(1)

    params = urlencode({
        "fields": "id,name,instagram_business_account{id,username}",
        "access_token": token,
    })
    url = f"{BASE}/me/accounts?{params}"

    try:
        data = get_json(url)
    except HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print("HTTP error while checking token:")
        print(body)
        sys.exit(2)
    except URLError as e:
        print(f"Network error: {e}")
        sys.exit(3)

    accounts = data.get("data", [])
    if not accounts:
        print("Token valid, but no pages were returned.")
        print(json.dumps(data, indent=2, ensure_ascii=False))
        sys.exit(4)

    result = []
    for page in accounts:
        ig = page.get("instagram_business_account") or {}
        result.append({
            "page_name": page.get("name"),
            "page_id": page.get("id"),
            "instagram_business_id": ig.get("id"),
            "instagram_username": ig.get("username"),
        })

    print(json.dumps({"accounts": result}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
