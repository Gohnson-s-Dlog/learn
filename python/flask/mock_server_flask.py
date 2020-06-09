# 指定一个接口
# 导包
from flask import Flask,request

app=Flask (__name__)

@app.route('/')
def hello():
    return '你好flask!'


@app.route('/post',methods=['POST'])
def test_post():
    d1=request.form['d1']
    d2=request.form['d2']
    return d1+d2

if __name__=='__main__':

    app.run('localhost','9999')