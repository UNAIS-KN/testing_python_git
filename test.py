from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World fdf"

@app.route("/h")
def testing():
   return "tested ok"

if __name__ == '__main__':
   app.run('0.0.0.0', '8080')
