# app.py
from flask import Flask
from app.routes.usuarios_routes import usuarios_bp
from app.routes.vuelos_routes import vuelos_bp

app = Flask(__name__)

# Registrar blueprints para rutas
app.register_blueprint(usuarios_bp, url_prefix='/usuarios')
app.register_blueprint(vuelos_bp, url_prefix='/vuelos')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
