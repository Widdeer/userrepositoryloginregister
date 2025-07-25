import sqlite3
import time
def readlogin(nombrep, contraseñap):
    conn = sqlite3.connect("databaseregister.db")
    cursor = conn.cursor()

    # Buscamos el usuario por nombre o email
    cursor.execute(
        '''SELECT contraseña FROM dt_usuarios WHERE nombreusuario = ? OR email = ?''',
        (nombrep, nombrep)
    )

    usuario_impuro = cursor.fetchone()
    conn.close()

    time.sleep(0.5)

    if usuario_impuro is None:
        return False
    
    datos_usuario = tuple(str(x) for x in usuario_impuro)
  

    contraseña_en_bd = datos_usuario[0]  # Asegurate de que índice 3 sea 'contraseña'
    if contraseña_en_bd == contraseñap:
        return True  # Login correcto
    else:
        return False