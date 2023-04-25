'''
Date: 2023-04-21 11:33:36
Author: yongbao
LastEditTime: 2023-04-21 14:49:29
Description: 
'''
import requests
import hmac
import hashlib
import datetime
import base64
import re

url = "https://backend.tianhe.wenchang.bianjie.ai/nodejs/blocks?pageNum=1&pageSize=10&useCount=false"
username = "hmac-tianhe"
secretkey = "Zf8R7ecX9VzL"

# Get the current time in GMT format
gm_time = datetime.datetime.now(datetime.timezone.utc).strftime('%a, %d %b %Y %H:%M:%S GMT')
# gm_time = "Fri, 21 Apr 2023 05:43:39 GMT"

# Generate the string to sign
str_to_sign = f"x-date: {gm_time}\nGET /nodejs/blocks?pageNum=1&pageSize=10&useCount=false HTTP/2.0"


signature = hmac.new(secretkey.encode(), str_to_sign.encode(), digestmod=hashlib.sha256)
signature_b64 = base64.b64encode(signature.digest())

# auth_header = f'hmac username="{username}", algorithm="hmac-sha256", headers="x-date request-line",  signature="{signature_b64.decode()}"'
auth_header = f'hmac username="{username}", algorithm="hmac-sha256", headers="x-date request-line", signature="{signature_b64.decode()}"'
# auth_header= %(hmac username="#{username}", algorithm="hmac-sha1", headers="date", signature="#{hmac}")

header = {
    # "authorization": auth_header,
    # 7NruyF1IbSPPlE86mP3QM6RS4FFFqIvV5WaoQ5jn4tg=
    "authorization": auth_header,
    "x-date": gm_time,
}

# header = {
#     # "authorization": auth_header,
#     # 7NruyF1IbSPPlE86mP3QM6RS4FFFqIvV5WaoQ5jn4tg=
#     "authorization": 'hmac username="hmac-tianhe", algorithm="hmac-sha256", headers="x-date request-line",  signature="YYjYiwadDgveqotqcoQuhf926rzQfREEglJtdDQlHrE="',
#     "x-date":'Fri, 21 Apr 2023 06:23:52 GMT'
# }



# headers = headers.strip().split('\n')
# headers = {x.split(':')[0].strip(): ("".join(x.split(':')[1:])).strip().replace('//', "://") for x in headers}


print(header)
response = requests.request("GET", url, headers=header)
# response = requests.get(url, headers=header)
print(response.text)


def GetAuthHeader(username, secretkey, body=None):
    url = "https://backend.tianhe.wenchang.bianjie.ai/nodejs/blocks?pageNum=1&pageSize=10&useCount=false"

    # Get the current time in GMT format
    # gm_time = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")
    gm_time =  "Fri, 21 Apr 2023 05:43:39 GMT"

    # Generate the string to sign
    str_to_sign = f"x-date: {gm_time}\nGET /nodejs/blocks?pageNum=1&pageSize=10&useCount=false HTTP/2.0"

    # Generate the HMAC signature
    signature = hmac.new(secretkey.encode(), str_to_sign.encode(), digestmod=hashlib.sha256)
    signature_b64 = base64.b64encode(signature.digest()).decode()

    # Generate the authorization header
    auth_header = f'hmac username="{username}", algorithm="hmac-sha256", headers="x-date request-line", signature="{signature_b64}"'

    headers = {
        "Authorization": auth_header,
        "x-date": gm_time,
    }

    return headers

# header=GetAuthHeader(username,secretkey)
# print(header)
# response = requests.request("GET", url, headers=headers)
# response = requests.get(url, headers=header)
# print(response.text)