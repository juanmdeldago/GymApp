from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola! El sistema del gimnasio está en línea."

if __name__ == '__main__':
    app.run(debug=True)
