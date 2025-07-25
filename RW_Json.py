#archivo que lee
from loadloginread import readlogin
from flask import redirect, url_for
import json
import sqlite3
import os

def comparar_datos_login(RW, usernamep, passwordp, emailp, confpassword):

    if RW == "read":
        verificacion = readlogin(usernamep, passwordp)
        return verificacion
        
    elif RW == "write":

        if passwordp != confpassword:
            return redirect(url_for("nopasswordconfirm"))       

        conn = sqlite3.connect("databaseregister.db")
        cursor = conn.cursor()
        #abre un proceso para saber si el email o el nombre de usuario ya existe
        cursor.execute(
            '''SELECT nombreusuario, email FROM dt_usuarios WHERE nombreusuario = ? OR email = ?''',
            (usernamep, emailp)
            )
        
        informacion_sql_verificacion = cursor.fetchone()
        
        if informacion_sql_verificacion:
            conn.close()
            return redirect(url_for("user_exists"))
        #cierra el proceso de verificacion del nombre de usuario o email si existen
        
            
        cursor.execute(
            '''INSERT INTO dt_usuarios(nombreusuario, email, contraseña) VALUES (?, ?, ?)''',
            (usernamep, emailp, passwordp)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("success"))
    else:
        return "error" #retorna error