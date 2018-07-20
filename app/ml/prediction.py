from app.ml.utils import load_model, predict_batches, save_prediction_to_csv
from app.ml.data_prep import data_pipeline_for_prediction,prepare_data
from app.ml import config
from app.ml.utils import read_features_from_disk
import pandas as pd

model = load_model()
features = read_features_from_disk()

def make_predictions(monthEnd):

    # get monthEnd data

    model_features = read_features_from_disk()

    data = data_pipeline_for_prediction(monthEnd, model_features)

    # predict
    prediction_df = predict_batches(model, data)

    prediction_df = prediction_df.reset_index()

    prediction_df = prediction_df.rename(columns={'index': 'LoanCode'})

    prediction_df['LoanCode'] = prediction_df['LoanCode'].astype('int64').astype('str')

    return prediction_df.to_dict(orient='records')


def make_predictions_for_single_data(data_dict):

    keys_to_float = ['average_Overdue_days','amount_Credit_Request']
    keys_to_int = ['familyMembers']

    for key in keys_to_float:
        if key in data_dict:
            data_dict[key] = float(data_dict[key])
    
    for key in keys_to_int:
        if key in data_dict:
            data_dict[key] = int(data_dict[key])

    dataframe = pd.DataFrame([data_dict])

    print("data dict ",data_dict)
    print(dataframe.info())
    print(dataframe.head())

    model_features = read_features_from_disk()
    data = prepare_data(dataframe,mode='test',model_features=model_features)
    prediction_df = predict_batches(model,data)
    print(prediction_df.head())
    return prediction_df.to_dict(orient='records')[0]