# coding=utf-8
__author__ = 'g7842'

'''Flask通过Python的装饰器在内部自动地把URL和函数给关联起来'''
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

# if __name__ == '__main__':
#     app.run()




'''使用模块'''
# 使用模板，我们需要预先准备一个HTML文档，这个HTML文档不是普通的HTML，而是嵌入了一些变量和指令，然后，根据我们传入的数据，替换后，得到最终的HTML，发送给用户：
# 在Jinja2模板中，我们用{{ name }}表示一个需要替换的变量。很多时候，还需要循环、条件判断等指令语句，在Jinja2中，用{% ... %}表示指令。
from flask import Flask, request, render_template

app1 = Flask(__name__)

@app1.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app1.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app1.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app1.run()



'''其他web框架'''
# Django：全能型Web框架；
#
# web.py：一个小巧的Web框架；
#
# Bottle：和Flask类似的Web框架；
#
# Tornado：Facebook的开源异步Web框架。
