from flask import Flask, request, jsonify, make_response
from app.ml import utils
from app.ml import prediction
import traceback

app = Flask(__name__)


@app.route("/api/predict",methods=['GET'],strict_slashes=False)
def get_predictions():
    monthEnd = request.args.get('monthEnd',101)
    trainingMonth = request.args.get('trainingMonth')
    try:
        prediction_filename = prediction.make_predictions(monthEnd,trainingMonth)
        response = {
            'status': 'successful',
            'data': prediction_filename
        }
        return jsonify(response)
    except Exception:
        error = traceback.format_exc()
        response = {
            'status': 'unsuccessful',
            'error': error,
            'data': []
        }
        return jsonify(response),500