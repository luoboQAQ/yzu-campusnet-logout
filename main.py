# -*- coding: utf-8 -*-
from loguru import logger
import httpx

from config import *
from self_service_net import SelfServiceNet
from get_ip import get_ip

client = httpx.Client(
    headers={
        "User-Agent": USER_AGENT,
    },
    verify=False,
    follow_redirects=True,
)
self_service_net = SelfServiceNet(client)

try:
    self_service_net.login(SSO_USERNAME, SSO_PASSWORD)
    logger.info("Login success")
except Exception as e:
    logger.exception("Failed to login")
    exit(1)

try:
    ips = self_service_net.get_onlines()
    logger.info("Get onlines success")
except Exception as e:
    logger.exception("Failed to get onlines, try to get it locally")
    ip = get_ip()
    if ip and ip[:3] == "10.":
        ips = [ip]
        logger.info("Get ip locally success")
    else:
        logger.exception("Failed to get ip locally")
        ips = [input("Please input your ip: ")]

for ip in ips:
    try:
        self_service_net.logout(SSO_USERNAME, ip)
        logger.info(f"Logout {ip} success")
    except Exception as e:
        logger.exception(f"Failed to logout {ip}")
        continue