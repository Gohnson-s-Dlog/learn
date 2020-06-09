import requests

body={
    'd1':'hello',
    'd2':'flask123'
}
#post请求
resp=requests.post('http://127.0.0.1:9090/post',data=body)
print(resp.text)