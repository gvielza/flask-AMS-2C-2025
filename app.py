from flask import Flask, render_template, request


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
    return render_template("resultado.html", dni=dni, usuario=usuario)