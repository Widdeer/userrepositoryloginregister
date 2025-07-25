#archivo register
from flask import request
from RW_Json import comparar_datos_login
def procesar_register():
    if request.method == 'POST':
        return comparar_datos_login('write',
                                    request.form['username'], 
                                    request.form['password'], 
                                    request.form['email'], 
                                    request.form['confirm_password'])