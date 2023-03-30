'''
Date: 2023-03-30 15:49:48
Author: diaoyb
LastEditTime: 2023-03-30 18:27:59
Describe: wordpress 一些网站的签到
'''
import requests
import os
import sys
from tools import notify 

url = "https://www.22vd.com/wp-admin/admin-ajax.php"


def login(wp_name,wp_password):

    querystring = {"action":"xh_social_add_ons_login","tab":"login","xh_social_add_ons_login":"3de9245720","notice_str":"6736851510","hash":"37f1a771fc282a565c5aa4361b9ed957"}

    payload = "login_name=%s&login_password=%s" % (wp_name,wp_password)
    headers = {
        'accept': "application/json, text/javascript, */*",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9,und;q=0.8,zh-Hans",
        'content-type': "application/x-www-form-urlencoded",
        'origin': "https://www.22vd.com",
        'referer': "https://www.22vd.com/",
        'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    wp_cookie = response.headers['set-cookie']
    return wp_cookie

if os.environ.get("wp_name"):
    wp_name = os.environ.get("wp_name")
    wp_password = os.environ.get("wp_password")
else:
    print("请在环境变量填写wp的值")
    sys.exit()

wp_cookie=login(wp_name,wp_password)

payload = "action=sign_ajax&ajax_date=days"
headers = {
    'accept': "*/*",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.9,und;q=0.8,zh-Hans;q=0.7",
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
    'origin': "https://www.22vd.com",
    'referer': "https://www.22vd.com/wordpress",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    'x-requested-with': "XMLHttpRequest",
    'cookie': wp_cookie
    }

response = requests.request("POST", url, data=payload, headers=headers)

if response.status_code==200:
    message = "签到成功"
    notify.send("wp签到", message)


