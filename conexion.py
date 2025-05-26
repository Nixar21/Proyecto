import psycopg2

#Coneccion de la base de datos
def conectar():
    #Correccion de errores "try"
    try:
        conexion = psycopg2.connect(
            #Nombre de local host
            host = "localhost",
            #Nombre de la base de datos
            database = "proyecto",
            #Nombre de usuario
            user= "postgres",
            #Contraseña de postgre
            password= "nose",
            #Numero del puerto
            port= "5432"
        )
        return conexion
    except Exception as e:
        print(f"Erorr a conectar con la base de datos {e}")
        return None
#if __name__ == "__main__":
#    conn = conectar()  # Definís conn llamando a la función
#
#    if conn:
#        print("esta bien")
#        conn.close()
#    else:
#        print("esta mal")