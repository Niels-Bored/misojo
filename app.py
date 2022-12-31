import os
import io
import time
from pdfmaker_Texas.PDFMaker import generatePDF as pdfTexas 
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
        return render_template('index.html', error=False)
    elif request.method=="POST":
        user=request.form['user']
        password=request.form['password']
        userfound=Database.run_sql(f"select * from users where user='{user}' AND password='{password}'")
        if userfound:
            session["user"]=user
            return redirect(url_for('index'))
        else:
            return render_template('index.html', error=True)    

@app.route("/")
@validate_session()
def index():
    return render_template('selection.html')

@app.route("/texas/", methods=["GET", "POST"])
@validate_session()
def texas():
    user = session.get("user","")
    userdata=Database.run_sql(f"select * from users where user='{user}'")[0]

    if request.method=="GET":     
        return render_template('texas.html', user=userdata["user"], counter=userdata["counter"])
    elif request.method=="POST":
        print("Petición recibida en post")
        json_data = request.get_json()
        pdfTexas(json_data["plate"], json_data["year"], json_data["make"], json_data["issue_date"], json_data["expiration_date"], json_data["vin"], json_data["major_color"], json_data["minor_color"], json_data["body"], json_data["model"], json_data["owner"], json_data["address"], json_data["city"], json_data["state"], json_data["zip_code"])
        print("Archivo pdf generado")
        # Get last counter
        sql = f"""SELECT counter FROM users WHERE user = "{session['user']}";;"""
        counter = Database.run_sql(sql)[0]["counter"]
        counter += 1
        print("Contador obtenido")
        # Update counter
        sql = f"""UPDATE users SET counter = {counter} WHERE user = "{session['user']}";"""
        Database.run_sql(sql)
        print("Contador actualizado")

        return ({"ok":True},200)   

@app.route("/california/", methods=["GET", "POST"])
@validate_session()
def california():
    user = session.get("user","")
    userdata=Database.run_sql(f"select * from users where user='{user}'")[0]

    if request.method=="GET":     
        return render_template('california.html', user=userdata["user"], counter=userdata["counter"])
    elif request.method=="POST":
        json_data = request.get_json()
        pdfTexas(json_data["plate"], json_data["year"], json_data["make"], json_data["issue_date"], json_data["expiration_date"], json_data["vin"], json_data["major_color"], json_data["minor_color"], json_data["body"], json_data["model"], json_data["owner"], json_data["address"], json_data["city"], json_data["state"], json_data["zip_code"])
        
        # Get last counter
        sql = f"""SELECT counter FROM users WHERE user = "{session['user']}";;"""
        counter = Database.run_sql(sql)[0]["counter"]
        counter += 1

        # Update counter
        sql = f"""UPDATE users SET counter = {counter} WHERE user = "{session['user']}";"""
        Database.run_sql(sql)

        return ({"ok":True},200)
    

@app.route("/new_mexico/", methods=["GET", "POST"])
@validate_session()
def new_mexico():
    user = session.get("user","")
    userdata=Database.run_sql(f"select * from users where user='{user}'")[0]

    if request.method=="GET":     
        return render_template('new_mexico.html', user=userdata["user"], counter=userdata["counter"])
    elif request.method=="POST":
        json_data = request.get_json()
        pdfTexas(json_data["plate"], json_data["year"], json_data["make"], json_data["issue_date"], json_data["expiration_date"], json_data["vin"], json_data["major_color"], json_data["minor_color"], json_data["body"], json_data["model"], json_data["owner"], json_data["address"], json_data["city"], json_data["state"], json_data["zip_code"])
        
        # Get last counter
        sql = f"""SELECT counter FROM users WHERE user = "{session['user']}";;"""
        counter = Database.run_sql(sql)[0]["counter"]
        counter += 1

        # Update counter
        sql = f"""UPDATE users SET counter = {counter} WHERE user = "{session['user']}";"""
        Database.run_sql(sql)

        return ({"ok":True},200)

@app.route("/logout/")
@validate_session()
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))

@app.route("/file/<filename>/")
@validate_session()
def file(filename):
    time.sleep(1)
    file_path=os.path.join(os.path.dirname(__file__),"files",filename+".pdf")
    with open(file_path, 'rb') as bites:
        return send_file(
            io.BytesIO(bites.read()),
            download_name=filename+".pdf",
            mimetype='application/pdf'
        )


if __name__ == "__main__":
    app.run(debug=True, port=3000) 