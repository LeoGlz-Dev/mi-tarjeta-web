from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>¡Hola! Soy Leonardo Gonzalez Quijada</h1>
    <p>Estudio en: Universidad del Valle de Mexico </p>
    <p>Me gusta: Programar y Jugar Videojuegos </p>
    <p><em>"Cualquier problema tiene un solucion todo depende de la forma en que actues"</em></p>
    """

if __name__ == "__main__":
    app.run(debug=True)
