import logging
from flask import jsonify, request
import json

from src.services.kafkaService.producer import sendToTopic

SUCCESS_REQUEST_CODE = 200
SERVER_ERROR_CODE = 500
BAD_REQUEST_CODE = 400


def registerRoutes(app):
    @app.route("/upload", methods = ["POST"])
    def uploadFileForIngestion():
        try:
            file = request.files['file']
            data = json.loads(file.read())

            if data:
                sendToTopic(data)
                return jsonify({'message' : 'File uploaded Successfully and Sent to Kafka'}), SUCCESS_REQUEST_CODE
        
            return jsonify({'message' : 'File is empty'}), SUCCESS_REQUEST_CODE
        
        except ValueError as error:
            logging.exception(error)

            return jsonify({'error' : str(error)}), BAD_REQUEST_CODE
        
        except Exception as error:
            logging.exception(error)

            return jsonify({'error' : str(error)}), SERVER_ERROR_CODE