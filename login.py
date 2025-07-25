#archivo login.py
from flask import request, redirect, url_for
from RW_Json import comparar_datos_login
#el inicio de la sesion
def procesar_login():
    #agarra fromulario con metodo POST que se envio en el momento
    if request.method == 'POST': 
        #comienza a comparar los datos ingresados por el usuario y luego abre el archivo .json con modo lectura y los compara
        valor_de_comparacion = comparar_datos_login('read', request.form['username'], request.form['password'], None, None)
        if valor_de_comparacion == True:
            print(valor_de_comparacion)
            return redirect(url_for('home'))
        else:
            print('a', valor_de_comparacion)
            return redirect(url_for('error_login'))