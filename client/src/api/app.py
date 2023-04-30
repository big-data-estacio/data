from flask import Flask
from routes.bebidas import bebidas_bp
from routes.clientes import clientes_bp

app = Flask(__name__)
app.register_blueprint(bebidas_bp)
app.register_blueprint(clientes_bp)

if __name__ == '__main__':
    app.run(debug=True)