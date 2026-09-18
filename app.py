import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 1. Configuración de la base de datos
# Reemplazá el texto de abajo con la External Database URL de Render
url_base_datos = "postgresql://jmapp_user:Xap9Boywu9bwUoRbRSW7hP4uaVJcFEpX@dpg-daml17ek1f9s739f1ekg-a/jmapp"

# Pequeño ajuste técnico: SQLAlchemy requiere que empiece con postgresql://
if url_base_datos.startswith("postgres://"):
    url_base_datos = url_base_datos.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = url_base_datos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 2. Definimos la estructura de la tabla de Usuarios
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(20), nullable=False) # Roles: admin, profesor, alumno

# 3. Creamos las tablas automáticamente al iniciar
with app.app_context():
    db.create_all()
    # Si la tabla está vacía, cargamos los usuarios iniciales de prueba
    if not Usuario.query.first():
        db.session.add(Usuario(usuario="admin", password="123", nombre="Administrador", rol="admin"))
        db.session.add(Usuario(usuario="profe_juan", password="123", nombre="Juan Pablo", rol="profesor"))
        db.session.add(Usuario(usuario="alumno_mati", password="123", nombre="Matías", rol="alumno"))
        db.session.commit()

# 4. Rutas de la aplicación
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    usuario_ingresado = request.form.get('usuario')
    password_ingresado = request.form.get('password')
    
    # Ahora buscamos al usuario en la base de datos REAL
    usuario_db = Usuario.query.filter_by(usuario=usuario_ingresado).first()
    
    if usuario_db and usuario_db.password == password_ingresado:
        return render_template('dashboard.html', usuario=usuario_db.nombre, rol=usuario_db.rol)
    else:
        return render_template('login.html', error="Usuario o contraseña incorrectos.")

if __name__ == '__main__':
    app.run(debug=True)
