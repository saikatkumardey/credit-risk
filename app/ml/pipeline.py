from app.ml.data_prep import data_pipeline_for_training
from app.ml import modelling
from app.ml import utils

def train(monthEnd=101,classifierName = 'random-forest',path_to_save='data/models/model'):
    #get data and split into train-test
    X_train,X_test,y_train,y_test = data_pipeline_for_training(monthEnd)
    #train model
    classifier = modelling.models.get(classifierName)
    if classifierName is None:
        raise Exception("Incorrect Model Name specified")
    model = classifier(X_train,y_train)
    #run cross-validation
    utils.run_cv(model,X_train,y_train)
    #get model evaluation report
    utils.get_model_evaluation_report(model,X_test,y_test)
    #save model to disk
    utils.save_model(model,path_to_save)
    utils.save_feature_names(X_train.columns.tolist(),monthEnd)
    return model



