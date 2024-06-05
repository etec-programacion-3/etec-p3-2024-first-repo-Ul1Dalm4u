from flask import Flask

app=Flask(__name__)

@app.route("/hola")
def hola():
    return "hola mundo"

@app.route("/chau")
def goodbay():
    return "chau"

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"Hola {nombre}"

@app.route("/saludo/<nombre>/<apellido>")
def saludo2(nombre, apellido):
    return f"Hola {nombre} {apellido}"

app.run()