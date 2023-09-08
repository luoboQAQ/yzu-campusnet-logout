# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv

load_dotenv()


def e(key, default=None, *, required=False):
    if required and key not in os.environ:
        raise ValueError(f"Environment variable {key} is required")
    return os.environ.get(key, default)


USER_AGENT = e(
    "USER_AGENT",
    "Mozilla/5.0 (Linux; U; Android 11; zh-cn; Redmi K30 Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.147 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.5.14",
)

SSO_USERNAME = e("SSO_USERNAME", required=True)
SSO_PASSWORD = e("SSO_PASSWORD", required=True)
