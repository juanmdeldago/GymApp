from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form.get('usuario')
    password = request.form.get('password')
    
    if usuario == "admin" and password == "1234":
        # Contraseña correcta: lo mandamos al panel
        return render_template('dashboard.html', usuario=usuario)
    else:
        # Contraseña incorrecta: recarga el login mostrando un error en rojo
        return render_template('login.html', error="Usuario o contraseña incorrectos.")

if __name__ == '__main__':
    app.run(debug=True)
