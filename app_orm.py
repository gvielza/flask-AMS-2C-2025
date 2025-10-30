from models import Alumno, db
from flask import Flask, request,jsonify
from dotenv import load_dotenv
import os

load_dotenv()

app=Flask(__name__)

user=os.getenv("DB_USER")
password=os.getenv("DB_PASSWORD")
host=os.getenv("DB_HOST")
port=os.getenv("DB_PORT")
db_name=os.getenv("DB_NAME")

app.config["SQLALCHEMY_DATABASE_URI"]=f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False


db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "Flask & SQLALCHEMY"


@app.route("/alumnos", methods=["GET"])
def listar_alumnos():
    alumnos=Alumno.query.all()
    return jsonify([{"id":a.id,  "nombre": a.nombre, "apellido":a.apellido, "email": a.email} for a in alumnos])

@app.route("/alumnos", methods=["POST"])
def agregar_alumno():
    data=request.get_json()
    nuevo=Alumno(nombre=data.get("nombre"),
             apellido=data.get("apellido"),
             email=data.get("email")   
                
                )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({"mensaje": "Alumno agregado correctamente", "id":nuevo.id}), 201
