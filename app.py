from flask import Flask, render_template, request, jsonify
from base_datos.conexion import Conexion

from flask_cors import CORS


app =Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("formulario.html")

@app.route("/<saludo>")
def saludo(saludo):
    return f"Hola {saludo}"


@app.route("/resultado", methods=['POST'])
def resultado():
    dni=request.form['dni']
    usuario=request.form['usuario']
    contrasenna=request.form['contrasena']
    conexion=Conexion('base_datos/mi_app.db')
    conexion.crear_tabla_usuario()
    if dni!=None and usuario!=None and contrasenna!=None:
        conexion.agregar_usuario(dni,usuario,contrasenna)
        clientes=conexion.mostrar_clientes()
        conexion.cerrar_conexion()
        return render_template("resultado.html", dni=dni,usuario=usuario,clientes=clientes)
    else:
        return render_template("resultado.html")
    
@app.route("/api/enviar-datos", methods=['POST'])
def recibir_datos():
    datos=request.get_json()
    dni=datos.get('dni')
    usuario=datos.get('usuario')
    contrasenna=datos.get('contrasenna')
    
    mi_conexion=Conexion("base_datos/mi_app.db")
    mi_conexion.agregar_usuario(dni, usuario, contrasenna)
    mi_conexion.cerrar_conexion()

    return jsonify({
        'status':'ok',
        'mensaje':f"Recibido  dni={dni}, usuario={usuario}" 
    }),200

    