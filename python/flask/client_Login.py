import json
from pprint import pprint

import requests as requests

# 使用fiddler抓包查看请求消息体Content-Type为x-www-form-urlencoded;
data = {
    'm': 'Home',
    'c': 'Cart',
    'body': '''
        {'username': '13800138006',
        'password': '123456',
        'verify_code': '1'
        }    
    '''
}
# 头域
headers = {}
# url
url = 'http://www.testingedu.com.cn:8000/index.php'
datax = 'm=Home&c=Cart&a=header_cart_list'
# 发送request请求,接收响应response
respon = requests.post(url=url, data=data, json=True)  # , headers=headers
# print(type(respon))
print(respon.status_code)
pprint(respon.text)
# pprint(respon.headers)
# pprint(respon.json(),width=10)