import os
import io
import time 
from mysql import MySQL
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, send_file
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

DATABASE_HOST = os.environ['DATABASE_HOST']
DATABASE_NAME = os.environ['DATABASE_NAME']
DATABASE_USER = os.environ['DATABASE_USER']
DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']

Database = MySQL(DATABASE_HOST, DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD)

app = Flask(__name__)
CORS(app)
app.secret_key = b'bb,hjd87li7fiopsddfrgt5'

def validate_session():
    def wraper(function):
        @wraps(function)
        def decorator(*args, **kwargs):
            user=session.get("user","")
            if user:
                return function(*args, **kwargs)
            else:
                return redirect(url_for("login"))
        return decorator
    return wraper                

@app.route("/login/", methods=["GET", "POST"])
def login():
    """ 
    Si el usuario accede carga la página muestra el formulario, 
    si no valida los datos del formulario para redirigir al home 
    """

    if request.method=="GET":           
        return render_template('index.html', error="")
    elif request.method=="POST":
        user=request.form['user']
        password=request.form['password']
        userfound=Database.run_sql(f"select * from users where user='{user}' AND password='{password}'")
        if userfound:
            session["user"]=user
            return redirect(url_for('index'))
        else:
            return render_template('index.html', error="Invalid credentials")    

@app.route("/")
@validate_session()
def index():
    return render_template('selection.html')

@app.route("/logout/")
@validate_session()
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True, port=3000) 