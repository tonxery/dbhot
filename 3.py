from flask import Flask,render_template,request,redirect,session,url_for,jsonify,make_response

app = Flask(__name__)

print(app.config)
# app.config['DEBUG'] = "True"         #更改配置文件1
app.config.from_object("settings.Dev")  #更改配置文件2
print(app.config)

# @app.route('/index/<int:nid>',methods=['GET','POST'],endpoint='n1')
# def index(nid):  #获取文件名
#     print(nid)
#     print(url_for('n1'))
#     return "Index"

# @app.route('/index/<int:nid>',methods=['GET','POST'])
# def index(nid):  #接受整形
#     print(nid)
#     return "Index"

@app.route('/index/<str>',methods=['GET','POST'])
def index(str):  #默认接受字符串http://127.0.0.1:5000/index/abcd
    print(str)
    # return "Index"

    # dic = {'k1':'v1'}
    # return jsonify(dic)

    obj = make_response(jsonify({'k1':'v1'}))
    obj.headers['xxxxxx'] = '123'
    obj.set_cookie('key','value')
    return  obj

if __name__ == "__main__":
    app.run()