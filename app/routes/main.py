from flask import Flask, request, jsonify, make_response, render_template,flash
from app.ml import utils
from app.ml import prediction
import traceback
from flask_bootstrap import Bootstrap
from app.routes.forms import LoanForm


app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/",methods=['GET','POST'],strict_slashes=False)
def index():

    form = LoanForm()
    if form.validate_on_submit():
        form_dict = request.form.to_dict()
        del form_dict['csrf_token'], form_dict['submit_button']
        print(form_dict)
        try:
            prediction_data = prediction.make_predictions_for_single_data(form_dict)
            good_pct = prediction_data.get('good')
            bad_pct = prediction_data.get('bad')       
            return render_template('index.html',form=form,good_pct=good_pct,bad_pct=bad_pct)
        except Exception:
            error = traceback.format_exc()
            flash(error)
            return render_template('index.html',form=form)
    return render_template('index.html',form=form)


@app.route("/api/predict-single",methods=['POST'],strict_slashes=False)
def predict_single():
    return "predictions for single loan."

@app.route("/api/predict-batches",methods=['GET'],strict_slashes=False)
def get_predictions():
    monthEnd = request.args.get('monthEnd',101)
    try:
        prediction_data = prediction.make_predictions(monthEnd)
        response = {
            'status': 'successful',
            'data': prediction_data
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