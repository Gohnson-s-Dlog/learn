from pprint import pprint

import requests
# post请求连接百度
body={
    'd1':'ni',
    'd2':'hao'
}
res=requests.post('http://localhost:9999/post',data=body)
# respon=requests.post('http://www.baidu.com')

#仅供参考,一般响应码不做为判断依据
print(res.status_code)
print(type(res.status_code))
if res.status_code==200:
    pprint('响应码为%s,测试通过'%(res.status_code))#打印语句中获取变量  pprint打印比print打印更漂亮
else:
    print('不通过')
print(res.cookies)