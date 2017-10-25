from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route("/")
def root():
    return render_template('hello.html'), 200

@app.route("/breeds")
def breeds():
    return render_template('breeds.html'), 200

@app.route("/history")
def history():
    return render_template('history.html'), 200

@app.route("/action")
def action():
    return render_template('action.html'), 200

@app.route("/con")
def con():
    return render_template('contact.html'), 200

@app.route("/bs")
def bs():
    return render_template('bs.html'), 200

@app.route("/rag")
def rag():
    return render_template('rag.html'), 200

@app.route("/per")
def per():
    return render_template('per.html'), 200

@app.route("/lr")
def lr():
    return render_template('per.html'), 200

@app.route("/sf")
def sf():
    return render_template('per.html'), 200

@app.route("/es")
def es():
    return render_template('per.html'), 200

@app.route("/login")
def login():
    return render_template('login.html'), 200

@app.route("/abcd")
def abcd():
    return redirect(url_for('root'))

@app.errorhandler (404)
def page_not_found ( error ):
    return " Couldn 't find the page you requested .", 404

@app.route('/')
def hello():
    return "Welcome back!"

@app . route ("/login", methods =['POST ','GET '])
def account():
    if request.method == 'POST':
      print request.form
      name = request.form ['name']
      return " Hello %s" % name
    else :
      page = '''
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>LOGIN</title>
<style type:"text/css">
*{margin:0;padding:0;}
#nav{ width:900px;height:50px;
font-family:'Georgin';
background:#6ac;

border-radius:5px;
}
#nav ul li{list-style:none;
float:left;
width:120px;
height:50px;
line-height:50px;
text-align:center;
}
#nav ul li:hover{
cursor:poiinter;
background:#f34;
border-radius:5px;
}
#nav ul li a{text-decoration:none;
color:#fff;
</style>


</head>

<body>
<body background="static/img/bg1.jpg"/>

<div id="nav">
        <ul>
         <li><a href="/">HOME</a></li>
         <li><a class="navbar-brand" href="/breeds">Breeds</a></li>
         <li class="active"><a href="/action">Action</a></li>
         <li><a href="/history">History</a></li>
         <li><a href="/login" >login</a></li>
         <li><a href="/con" >Contact</a></li>
         <div class="navbat-brand"></div>
        </ul>
      </div>


<div id="login_frame">
	<form method="post" action="login.js">
		<p>
			<label class="label_input">NAME</label>
			<input type="text" id="username" class="text_field"/>
		</p>
		<p>
			<laber class="label_input">PASSWORD</laber>
			<input type="text" id="password" class="text_field"/>
		</p>
		<div id="login_control">
		<a href="/"><input type="button" id="btn_login" value="LOG IN"
    onclick="login();"/></a>
		</div>
	</form>
</div>

</body>
</html> '''

      return page





if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
