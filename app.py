# Importaciones necesarias de Flask y otras librerías
from flask import Flask, render_template, request, url_for, flash, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from conexion import conectar  # Función personalizada para conectarse a la base de datos

# Crear la aplicación Flask
app = Flask(__name__)

# Clave secreta para permitir el uso de sesiones y mensajes flash
app.secret_key = "1234"

# ───────────────────────────────────────────────────────────────
# Ruta principal del sitio ('/') para iniciar sesión
@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        # Obtener los datos enviados desde el formulario
        username = request.form['username']
        password = request.form['password']

        try:
            # Conexión a la base de datos
            conexion = conectar()
            cursor = conexion.cursor()

            # Buscar el usuario por su nombre
            cursor.execute("SELECT id_usuario, gmail FROM usuario WHERE nombre = %s", (username,))
            usuario = cursor.fetchone()

            if not usuario:
                flash('Usuario no encontrado')  # Mensaje si el usuario no existe
                return redirect(url_for('inicio'))

            id_usuario = usuario[0]  # Obtener el ID del usuario encontrado

            # Buscar la contraseña encriptada en la tabla credencial
            cursor.execute("SELECT password_hash FROM credencial WHERE fk_id_usuario = %s", (id_usuario,))
            credencial = cursor.fetchone()

            # Verificar si la contraseña ingresada coincide con la almacenada
            if not credencial or not check_password_hash(credencial[0], password):
                flash('Contraseña incorrecta')
                return redirect(url_for('inicio'))

            # Si todo está bien, guardar el nombre de usuario en la sesión
            session['usuario'] = username
            flash('Inicio de sesión exitoso')
            return redirect(url_for('pagina'))  # Redirigir a la página protegida

        except Exception as e:
            flash(f'Error al iniciar sesión: {e}')
            return redirect(url_for('inicio'))

    # Si es un GET, mostrar el formulario de inicio de sesión
    return render_template('inicio.html')


# ───────────────────────────────────────────────────────────────
# Página protegida que solo se muestra si el usuario está logueado
@app.route('/pagina')
def pagina():
    if 'usuario' in session:
        # Si hay un usuario en la sesión, mostrar la página
        return render_template('pagina.html', usuario=session['usuario'])
    else:
        # Si no está logueado, redirigir al inicio
        flash("Tenés que iniciar sesión para acceder al perfil.")
        return redirect(url_for('inicio'))


# ───────────────────────────────────────────────────────────────
# Página de recuperación de contraseña (sólo la vista)
@app.route('/recuperar')
def recuperar():
    return render_template('recuperar.html')


# ───────────────────────────────────────────────────────────────
# Registro de nuevos usuarios
@app.route('/registrarse', methods=['GET', 'POST'])
def registrarse():
    if request.method == 'POST':
        # Obtener los datos del formulario de registro
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Verificar que ambas contraseñas coincidan
        if password != confirm_password:
            flash('Las contraseñas no coinciden')
            return redirect(url_for('registrarse'))

        try:
            # Conectarse a la base de datos
            conexion = conectar()
            cursor = conexion.cursor()

            # Verificar si el correo ya está registrado
            cursor.execute("SELECT id_usuario FROM usuario WHERE gmail = %s", (email,))
            usuario_existente = cursor.fetchone()

            if usuario_existente:
                flash('Ya existe un usuario registrado con ese correo.')
                return redirect(url_for('registrarse'))

            # Insertar nuevo usuario en la tabla usuario
            cursor.execute("""
                INSERT INTO usuario (nombre, gmail)
                VALUES (%s, %s)
                RETURNING id_usuario;
            """, (nombre, email))
            id_usuario = cursor.fetchone()[0]  # Obtener el ID generado

            # Encriptar la contraseña ingresada
            password_hash = generate_password_hash(password)

            # Insertar la credencial del usuario (contraseña encriptada)
            cursor.execute("""
                INSERT INTO credencial (fk_id_usuario, password_hash)
                VALUES (%s, %s);
            """, (id_usuario, password_hash))

            # Confirmar los cambios en la base de datos
            conexion.commit()
            cursor.close()
            conexion.close()

            flash('Registro exitoso. Ya puedes iniciar sesión.')
            return redirect(url_for('inicio'))

        except Exception as e:
            flash(f'Error al registrar el usuario: {e}')
            return redirect(url_for('registrarse'))

    # Si es un GET, mostrar el formulario de registro
    return render_template('registrarse.html')

if __name__ == "__main__":
    app.run(debug=True)