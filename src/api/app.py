from flask import Flask
from src.routes.DICARoutes import registerRoutes

from src.config.definitions import loggerConfig
from src.config.configs import credentials

def appConfig():
    app = Flask(__name__)
    return app

app = appConfig()

registerRoutes(app)

if __name__ == "__main__": 
    loggerConfig()
    host = credentials["flaskServerHost"]
    port = int(credentials["flaskServerPort"])
    print("I'm inside main")
    app.run(host=host, port=port, debug=True)
