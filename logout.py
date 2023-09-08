from typing import Optional
import re

import httpx


class SelfServiceNet:
    def __init__(self, client: Optional[httpx.Client] = None) -> None:
        if client is None:
            self.client = httpx.Client(
                headers={
                    "User-Agent": "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36"
                },
                verify=False,
                follow_redirects=True,
            )
        else:
            self.client = client

    def login(self, name: str, password: str):
        resp = self.client.post(
            "http://10.240.0.100:8080/selfservice/module/scgroup/web/login_judge.jsf?mobileslef=true",
            data={"name": name, "password": password},
        )
        resp.raise_for_status()
        match = re.search(r"errorMsg=(.*?)&", resp.text)
        if match:
            error_msg = match.group(1)
            raise Exception(error_msg)

    def get_onlines(self):
        resp = self.client.get(
            "http://10.240.0.100:8080/selfservice/module/webcontent/web/onlinedevice_list.jsf"
        )
        resp.raise_for_status()
        if "操作执行失败" in resp.text:
            raise Exception("远程服务器错误")
        ips = re.findall(r'<input.*?id="userIp.*?value="(.*?)".*?>', resp.text)
        return ips

    def logout(self, name: str, ip: str):
        resp = self.client.post(
            "http://10.240.0.100:8080/selfservice/module/userself/web/userself_ajax.jsf?methodName=indexBean.kickUserBySelfForAjax",
            data={"key": f"{name}:{ip}"},
        )
        resp.raise_for_status()


if __name__ == "__main__":
    self_service_net = SelfServiceNet()
    username = "1"
    password = "1"
    self_service_net.login(username, password)
    self_service_net.get_onlines()
    for ip in self_service_net.get_onlines():
        print(ip)
        self_service_net.logout(username, ip)
