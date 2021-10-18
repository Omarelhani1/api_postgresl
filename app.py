import os
from flask import Flask, render_template,abort,request
app = Flask(__name__)	

@app.route('/',methods=["GET"])
def login():
    return render_template("login.html")

port=os.environ["PORT"]
app.run('0.0.0.0',int(port),debug=False)