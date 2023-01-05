from flask import Flask
from src.routes.routes import registerRoutes

def appConfig():
    app = Flask(__name__)
    return app

app = appConfig()

registerRoutes(app)

if __name__ == "__main__": 
    host = "0.0.0.0"
    port = 5000 
    app.run(host=host, port=port, debug=True)
