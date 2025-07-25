#archivo principal
from flask import Flask, redirect, request, jsonify, render_template, url_for
from login import procesar_login
from register import procesar_register

app = Flask(__name__)
#renderiza la pagina principal para seleccionar una de las dos opciones que hay
@app.route('/')
def Inicio():
    return render_template('index.html') #el usuario deberá seleccionar una de las dos opciones para ser redirigido

#proceso deregistro del usuario

@app.route("/user_exists")
def user_exists():
    return render_template("userexists.html")

#renderiza el html de /register que contiene un formulario con la accion de llevar al usuario al proceso para registrar esos datos
@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template('register.html')

#procesa los datos del formulario enviado por el usuario
@app.route("/register_processing", methods=['GET', 'POST'])
def register_processing():
    return procesar_register() #una vez finalizado la funcion, el usuario es dirigido a la pagina para que haga un inicio de sesion con los datos registrados

@app.route("/nopasswordconfirm", methods=["GET", "POST"])
def nopasswordconfirm():
    return render_template("nopasswordconfirm.html")

#Termina el proceso de registro del usuario


#Proceso que el usuario inicio la sesion

#renderiza elhtml de /login que contiene un formulario con la accion de llevar al usuario a /login processing
@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html')

#compara los datos enviados por el usuario a travez del formulario con los datos registrado por el usuario para ver si son las mismas personas
@app.route("/login_processing", methods=['GET', 'POST'])
def login_processing():
    return procesar_login() #una vez finalizado la funcion, el usuario es dirigido a /inicio

#Terminó el proceso que el usuario inicio la sesion


# renderiza La pagina de inicio una vez ingresado los datos correcto del usuario
@app.route("/inicio", methods=['GET', 'POST'])
def home():
    return render_template('inicio.html')

@app.route("/success", methods=['GET','POST'])
def success():
    return render_template('success.html')

# si los datos son incorrectos, el usuario será dirigido a /error_login para informarle del error y que lo vuelva a intentar
@app.route("/error_login")
def error_login():
    return render_template('errorlogincredential.html')


if __name__ == '__main__':
    app.run(debug=True)