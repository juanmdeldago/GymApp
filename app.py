from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # Esto le dice al sistema que muestre el archivo HTML que creamos
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Acá capturamos lo que el usuario escribe en la pantalla
    usuario = request.form.get('usuario')
    password = request.form.get('password')
    
    # Validamos el ingreso
    if usuario == "admin" and password == "1234":
        return f"¡Bienvenido {usuario}! Pronto acá veremos el panel de turnos."
    else:
        return "Usuario o contraseña incorrectos. Volvé atrás e intentá de nuevo."

if __name__ == '__main__':
    app.run(debug=True)
