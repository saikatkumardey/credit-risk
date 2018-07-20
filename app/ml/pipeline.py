from app.ml.data_prep import data_pipeline_for_training
from app.ml import modelling
from app.ml import utils

def train(classifierName = 'random-forest',numSamples=10000,modelFileName='myModel.model'):
    #get data and split into train-test
    X_train,X_test,y_train,y_test = data_pipeline_for_training(numSamples=numSamples)
    #train model
    classifier = modelling.models.get(classifierName)
    if classifierName is None:
        raise Exception("Incorrect Model Name specified")
    print("training model")
    model = classifier(X_train,y_train)
    #run cross-validation
    print("running cross-validation")
    utils.run_cv(model,X_train,y_train)
    #get model evaluation report
    utils.get_model_evaluation_report(model,X_test,y_test)
    #save model to disk
    print("saving model to disk")
    utils.save_model(model,modelFileName) # saves to MODEL_DIR/MODEL_FILENAME.model
    utils.save_feature_names(X_train.columns.tolist(),modelFileName) #saves to FEATURE_DIR/MODEL_FILENAME.features
    return model



