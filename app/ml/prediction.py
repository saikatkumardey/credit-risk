from app.ml.utils import load_model, predict_batches, save_prediction_to_csv
from app.ml.data_prep import data_pipeline_for_prediction
from app.ml import config
from app.ml.utils import read_features_from_disk

model = load_model(config.MODEL_PATH)


def make_predictions(monthEnd,trainingMonth):

    # get monthEnd data

    model_features = read_features_from_disk(trainingMonth)

    data = data_pipeline_for_prediction(monthEnd, model_features)

    # predict
    prediction_df = predict_batches(model, data)

    prediction_df = prediction_df.reset_index()

    prediction_df = prediction_df.rename(columns={'index': 'LoanCode'})

    return prediction_df.to_dict(orient='records')
