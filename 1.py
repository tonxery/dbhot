# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/index')
# def index():
#     return "仝信庙"
#
# if __name__ == '__main__':
#     app.run()
#

from flask import Flask,render_template,request,session

app = Flask(__name__,template_folder="templates",static_folder="static")

@app.route("/login",methods=['Get','POST'])
def login():

    if request.method == "GET":
        return render_template('login.html')
    user = request.form.get("user")
    pwd = request.form.get("pwd")
    if user == 'oldboy' and pwd == '666':
        return credits('/index')
    else:
        return render_template("login.html",error="用户名或密码错误")
        #return render_template("loginhtml",**{error="用户名或密码错误"})
    # return "Login"
    return render_template('login.html')

@app.route("/index")
def index():
    return "欢迎使用"

if __name__ == "__main__":
    app.run()