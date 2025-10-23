from flask import Flask, render_template, request
from base_datos.conexion import Conexion


app =Flask(__name__)

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