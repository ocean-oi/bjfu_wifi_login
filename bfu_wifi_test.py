import requests    # 用于向目标网站发送请求
import os
import re
import time
import base64
import sys

filepath = 'D:\\bfu_login_wifi\\pass_bfu_wifi_auto_login.txt'

def is_logined():
    resp = requests.get("http://10.1.1.10")
    text = resp.text
    loginStatu = resp.text.find("上网登录页")
    model_1 = re.compile(r'v46ip=\'(.+?)\'')
    model_2 = re.compile(r'v4ip=\'(.+?)\'')
    
    ip_1 = model_1.findall(text)
    ip_2 = model_2.findall(text)

    vaild_ipv4 = ''
    if ip_1:
        vaild_ipv4 = ip_1[0]
    else:
        if ip_2:
            vaild_ipv4 = ip_2[0]
    
    if len(vaild_ipv4) == 0:
        return -1,'-1'
    else:
        if loginStatu == -1:
            return 0,'0'
        else:
            print('您的ip为',vaild_ipv4)
            return 1,vaild_ipv4

def try_login(your_account,your_pass,ipv4):

    b64_pass = base64.b64encode(your_pass.encode('utf-8')).decode('utf-8')

    url = 'http://10.1.1.10:801/eportal/portal/custom/auth'

    datas = {

        "callback": "dr1004",
        "login_method": "1",
        "user_account": your_account,
        "user_password": b64_pass,
        "wlan_user_ip": ipv4,
        "wlan_user_ipv6": "",
        "wlan_user_mac": "000000000000",
        "wlan_ac_ip":"", 
        "wlan_ac_name":"", 
        "jsVersion": "4.1.3",
        "terminal_type": "1",
        "type": "1",
        "lang": "zh-cn",
        "v": "2053",
        "lang":"zh",
    }

    header = {
        "Accept":"*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Host": "10.1.1.10:801/",
        "Referer": "10.1.1.10/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44",
    }

    response = requests.get(url, params=datas).status_code  # GET 方式向 URL 发送表单，同时获取状态码
    print("状态码{}".format(response))  # 打印状态码

def restore_info():

    if not os.path.exists('D:\\bfu_login_wifi'):
        os.mkdir('D:\\bfu_login_wifi')

    with open(filepath, 'w') as f:
        f.write('account=\'\'\n')
        f.write('password=\'\'\n')
        f.write('# 请仔细输入，账号密码错误程序是不会提示的。')


def get_info():
        
    with open(filepath,'r') as f:
        content = f.read()
        account = re.findall(r'account=\'(.+?)\'',content)
        passwd = re.findall(r'password=\'(.+?)\'',content)

        if not account or not passwd:
            return -1,'',''
        else:
            return 0,account,passwd

        

def main():
    
    
    if not os.path.exists(filepath):
        restore_info()
        print('请您正确填写',filepath,'的内容。')
        print('否则程序无法继续运行')
        time.sleep(3)
        return
    
    status,ipv4_str = is_logined()
    if status == -1:
        print('获取ip错误，可能是因为您尚未连接校园网。')
        time.sleep(3)
        return
    
    if status == 1:
        print("校园网未连接，连接中...")
        
        stcode,account,passwd = get_info()
        if stcode != 0:
            print('请您正确填写',filepath,'的内容。')
            restore_info()
            time.sleep(5)
            return
        else:
            try_login(account[0],passwd[0],ipv4_str)
        
        
        print('校园网连接成功。')

        # print(stcode)
        # print(account)
        # print(passwd)
    else:
        print('您在使用本程序前已经连接过校园网。')
        print('退出程序。')

    time.sleep(0.5)
    

main()
