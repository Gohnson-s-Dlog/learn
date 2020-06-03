# 1.安装 pip install flask
# 利用flask编写一个接口
# 导包
from flask import Flask,request
# 实例化一个web服务对象
app =Flask (__name__)
# 创建一个方法来处理请求
# 定义一个路由--访问服务的根目录就可以得到结果
@app.route('/')
def hello():
    return '<h1>hello flask!</h1>'
# 定义post请求
@app.route('/post',methods=['POST'])
def test_post():
    # 处理发送过来的两个数据,将两个参数合并成一个字符串
    d1=request.form['d1']
    d2=request.form['d2']
    return  d1+d2
# 启动
if __name__=='__main__':
    # 运行服务,并确定运行服务的ip与端口
    app.run('127.0.0.1','9090')
