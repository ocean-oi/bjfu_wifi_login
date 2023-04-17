import requests    # 用于向目标网站发送请求
import os
import socket
import time

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(("8.8.8.8", 80))
# ip = s.getsockname()[0]

# print("IP:", ip) 


import requests

resp = requests.get("http://10.1.1.10")

text = resp.text
# print(text)
posi = resp.text.find("v46ip") + 7
posi2 = resp.text.find("v4ip") + 6
loginStatu = resp.text.find("上网登录页")
# print(resp.text)
# print(loginStatu)
ipv4 = []
ipv41 = []
# print(text[posi+6])
while True:
    if text[posi] != '\'':
        ipv4.append(text[posi]) 
        posi += 1
    else:
        break

while True:
    if text[posi2] != '\'':
        ipv41.append(text[posi2]) 
        posi2 += 1
    else:
        break
vaildIpv4 = ""
if len(ipv4) <= len(ipv41):
    vaildIpv4 = ipv4
else:
    vaildIpv4 = ipv41

# print(len(ipv4))
# print(len(ipv41))

ipv4str = "".join(vaildIpv4)
print("你当前的IP为：",ipv4str)


url = 'http://10.1.1.10:801/eportal/portal/custom/auth'
# url = 'http://10.1.1.10/'
# paramsop = "eyJtc2ciOiLnmbvlvZXmiJDlip/vvIEiLCJ3bGFuX3VzZXJfaXAiOiIxNzIuMjcuMTY5LjIiLCJ3bGFuX3VzZXJfbWFjIjoiMDAwMDAwMDAwMDAwIiwiaXNfb25saW5lIjoiMSJ9"
paramsop = {
    "DDDDD": '211002604',   # 这行是你需要根据自己的情况修改的地方
    "upass": '12130170',      # 这行是你需要根据自己的情况修改的地方

    # 下面的这些一般可以直接用(不用改),也有可能要根据你自己的浏览器中的data(数据)做些修改
    "R1": "0",
    "R3": "1",
    "R6": "0",
    "pare": "00",
    "OMKKey": "123456",
}
datas = {
    # "DDDDD": '211002604',   # 这行是你需要根据自己的情况修改的地方
    # "upass": '12130170',      # 这行是你需要根据自己的情况修改的地方

    # "R1": "0",
    # "R3": "1",
    # "R6": "0",
    # "pare": "00",
    # "OMKKey": "123456",

    "callback": "dr1004",
    "login_method": "1",
    "user_account": ",b,211002604",
    "user_password": "MTIxMzAxNzA=",
    # "wlan_user_ip":"172.27.169.2",
    "wlan_user_ip": ipv4str,
    "wlan_user_ipv6": "",
    # "wlan_user_mac": "38d57ae0fb35",
    # "wlan_user_mac": "38d57ae0fb3f",
    "wlan_user_mac": "000000000000",
    "wlan_ac_ip":"", 
    "wlan_ac_name":"", 
    "jsVersion": "4.1.3",
    "terminal_type": "1",
    "type": "1",
    "lang": "zh-cn",
    "v": "2053",
    "lang":"zh",
    # "wlan_user_ipv6":"",
    # "wlan_ac_ip":"",
    # "v":"6633",
    # "lang":"en",
    
    


    # 下面的这些一般可以直接用(不用改),也有可能要根据你自己的浏览器中的data(数据)做些修改
    
    # "account": "211002604",
    # "params": "eyJtc2ciOiLnmbvlvZXmiJDlip/vvIEiLCJ3bGFuX3VzZXJfaXAiOiIxNzIuMjcuMTY5LjIiLCJ3bGFuX3VzZXJfbWFjIjoiMDAwMDAwMDAwMDAwIiwiaXNfb25saW5lIjoiMSJ9",
    # "timestamp": "1679328767892",
    # "sign": "63b1b28f0a57e6b7cf9c54ec0c74cc94",

}
# 下面这整个 header 都是需要根据网页中的请求头来做修改
# 下面这整个 header 是我的,你需要按照你自己浏览器中出现的 Response Headers (请求标头)来修改
header = {

    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept":"*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Host": "10.1.1.10:801/",
    "Referer": "10.1.1.10/",
    # "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44",
}
# response = requests.get(url, data=datas).status_code  # POST 方式向 URL 发送表单，同时获取状态码

if loginStatu != - 1 :
    print("校园网未连接，连接中...")
    response = requests.get(url, params=datas).status_code  # GET 方式向 URL 发送表单，同时获取状态码
    print("状态码{}".format(response))  # 打印状态码
else:
    print("使用本程序前你已经连接好校园网，退出程序。")

time.sleep(0.5)


