from flask import Flask
from flask import Flask, redirect, url_for, request, render_template
import os
from src.User import User
from src import check
import base64

app = Flask(__name__,template_folder='template')
basename = '/iotcloud'

@app.route("/")
def mainpage():
   return "<h1>Server Running </h1> "

@app.route("/hello")
def helloworld():
   d = {
      "username": whoami().strip(),
      "env": "labs",
      "avatar": "https://sibidharan.me/wp-content/uploads/2020/06/Logo-round.png"
   }
   return render_template('helloworld.html',data=d)

@app.route(basename+"/dashboard")
def dashboard():
   return render_template("dashboard.html",data={})


# @app.route(basename+"/hello_world")
# def hello_world():
#    return render_template('helloworld.html')
   

@app.route(basename+'/')
def hello():
   return "<h1/>Welcome to Selfmade Ninja Academy</h1>"

@app.route(basename+'/whoami')
def whoami():
   return os.popen('whoami').read()


@app.route(basename+'/encode')
def encode():
   string = request.args['data']
   print(string)
   string = base64.b64decode(string)
   return string
 

if __name__ == '__main__':
   app.run(debug=True , port=7000)
