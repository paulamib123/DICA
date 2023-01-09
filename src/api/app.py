from flask import Flask
from src.routes.kafkaNifiRoutes import registerRoutes
from src.config.definitions import loggerConfig

def appConfig():
    app = Flask(__name__)
    return app

app = appConfig()

registerRoutes(app)

if __name__ == "__main__": 
    loggerConfig()
    host = "0.0.0.0"
    port = 5000 
    app.run(host=host, port=port, debug=True)
