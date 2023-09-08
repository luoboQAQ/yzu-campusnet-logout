# YZU CampusNet Logout

扬州大学校园网下线器

## 简介

受到[YZU CampusNet Login](https://github.com/TerraceCN/yzu-campusnet-login)这个项目的启发，整了个一键下线的脚本。

还在担心免费时长不够用？用完直接下线，不浪费一秒钟（雾

## 用法

首先设置环境变量或者添加`.env`文件，环境变量定义如下：

|变量名|描述|默认值|
|-|-|-|
|USER_AGENT|模拟访问所用的UA|见`config.py`|
|USERNAME|统一身份认证系统的用户名|-|
|PASSWORD|统一身份认证系统的密码|-|

脚本会把所有在线的设备全部退出，鉴于校园网系统经常抽风，也提供了自动/手动获取ip下线的功能

只是一个简单的脚本，也就不整什么Docker了🫠

### 命令行

```shell
pip install -r requirements.txt
python main.py
```

## 免责说明

YZU Campus Logout（以下简称“本脚本”）为便于作者个人生活的脚本，本脚本所用的方法均为对正常登录过的模拟，不得用于任何商业用途。

本脚本之著作权归脚本作者所有。用户可以自由选择是否使用本脚本。如果用户下载、安装、使用本脚本，即表明用户信任该脚本作者，脚本作者对因使用项目而造成的损失不承担任何责任。
