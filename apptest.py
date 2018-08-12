from flask import Flask,request,url_for,render_template,abort
from flask import flash

from User import Users
app = Flask(__name__)
app.secret_key = "a"

@app.route('/')
def hello_world():

    return render_template("secret2.html")


@app.route('/secret')
def secret():
    flash("xiaoxitishi")
    return render_template("secretindex.html")

@app.route('/login',methods=["POST"])
def secret2():
    form = request.form
    username = form.get('username')
    password = form.get('password')
    if not username:
        flash("user")
        return render_template("index.html")
    if not password:
        flash("password")
        return render_template("index.html")
    if username == "123" and password == "abc":
        flash("success")
        return render_template("index.html")
    else:
        flash("user or password")
        return render_template("index.html")

@app.errorhandler(404)
def error(e):
    return render_template("404.html")


#主动抛出异常
@app.route('/user/<user_id>')
def userindex1(user_id):
    user = None
    if int(user_id) == 1:
        user = Users(1,"xjl==1")
        return render_template("userindex.html",user=user)
    else:
        return abort(404)

@app.route('/userlsit')
def userindex2():
    user = None
    userlist = []
    for i in range(1,11):
        user = Users(i,"bianli"+str(i))
        userlist.append(user)
    return render_template("user_list.html",user=userlist)
@app.route('/one')
def userindex3():
    return render_template("one.html")
@app.route('/two')
def userindex4():
    return render_template("two.html")


@app.route('/test1',methods=["post"])
def test1():
    return "test1"
@app.route('/test2/<aa>',methods=['post'])
def test2(aa):
    return 'test2:'+aa
#jianzhichuangsong
@app.route('/test3')
def test3():
    ars = request.args.get("id")
    return 'test3:'+ars

# 反向路由
@app.route('/test4')
def test4():
    ars = url_for("test1")
    return 'test4:'+ars





if __name__ == '__main__':
    app.run(host="0.0.0.0")
