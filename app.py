import os
from datetime import datetime
from mysql import MySQL
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, send_file
from flask_cors import CORS
from dotenv import load_dotenv
from text_reader import text_to_audio

load_dotenv()


DATABASE_HOST = os.environ['DATABASE_HOST']
DATABASE_NAME = os.environ['DATABASE_NAME']
DATABASE_USER = os.environ['DATABASE_USER']
DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']

Database = MySQL(DATABASE_HOST, DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD)
CURRENTFOLDER = os.path.dirname(__file__)

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
        userfound=Database.run_sql(f"select * from user where name='{user}' AND password='{password}'")

        if userfound:
            session["user"]=user
            session["id"]=userfound[0]['id']
            return redirect(url_for('index'))
        else:
            return render_template('index.html', error="Invalid credentials")    

@app.route("/")
@validate_session()
def index():
    user_id=session.get("id","")
    files=Database.run_sql(f"select * from file where id_user={user_id}")
    print(files)
    return render_template('library.html', files=files)

@app.route("/logout/")
@validate_session()
def logout():
    session.pop("user",None)
    session.pop("id",None)
    return redirect(url_for("login"))

@app.route('/convert/', methods=["GET", "POST"])
@validate_session()
def upload_file():
    if request.method=="GET":           
        return render_template('convert.html')
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            user_id=session.get("id","")
            file_storage_name=file.filename
            filefound=Database.run_sql(f"select * from file where name='{file_storage_name}' and id_user={user_id}")
            if filefound:
                return render_template('convert.html', error="There's a file with the same name")
            else:
                date=datetime.now()
                query = f"INSERT INTO file (name, content, page, date, id_user) VALUES ('{file_storage_name}', '{file.filename.rsplit('.', 1)[1]}', 0, '{date}',{user_id})"
                Database.run_sql(query)
                os.makedirs(os.path.join(CURRENTFOLDER,'files',f'{user_id}'), exist_ok=True)
                file.save(os.path.join(CURRENTFOLDER,'files',f'{user_id}', file_storage_name))
                return redirect(url_for(f'index'))  
        else:
           return render_template('convert.html', error="Invalid File")  
        
def allowed_file(filename):
    return '.' in filename and 'pdf' == filename.rsplit('.', 1)[1] and len(filename)<=150

@app.route("/player/<string:filename>")
@validate_session()
def player(filename):
    user_id=session.get("id","")
    filefound=Database.run_sql(f"select * from file where name='{filename}' and id_user={user_id}")
    page = filefound[0]['page']
    print(filename)
    print(page)
    file_path = os.path.join(CURRENTFOLDER,'files', f'{user_id}',  filename)
    print(file_path)
    text_to_audio.convert_book(file_path, filename, page, str(user_id))
    filename = filename.replace(".pdf", "")    
    audioname = f'{filename} {page}-{page+1}'
    audioname += '.mp3'
    audio_path = f'/audios/{user_id}/{audioname}'
    print(audio_path)
    return render_template('player.html', audio_path=audio_path)

if __name__ == "__main__":
    app.run(debug=True) 