import itertools

import os
import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.externals import joblib
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score
from app.ml.config import FEATURE_DIR

np.set_printoptions(precision=2)


def plot_confusion_matrix(cm,
                          classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.gray_r):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    fig, ax = plt.subplots(figsize=(15, 8))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


def print_classification_report(y_true, y_pred, target_names):

    print(classification_report(y_true, y_pred, target_names=target_names))


def run_cv(model, X_train, y_train):

    cv_score = cross_val_score(estimator=model,
                               X=X_train,
                               y=y_train,
                               n_jobs=-1,
                               cv=5,
                               scoring='f1_weighted')
    print("mean = {}, std = {}".format(cv_score.mean(), cv_score.std()))
    return cv_score


def get_model_evaluation_report(model, X_test, y_test):

    y_pred = model.predict(X_test)

    cnf_matrix = confusion_matrix(y_test, y_pred)

    print_classification_report(
        y_true=y_test, y_pred=y_pred, target_names=model.classes_)

    plot_confusion_matrix(cnf_matrix, classes=model.classes_, normalize=True)


def predict_batches(model,data):

    probabilities = model.predict_proba(data)
    class_names = model.classes_
    pred_df = pd.DataFrame(probabilities,columns= class_names)
    return pred_df

def load_model(path):
    model = joblib.load(path)
    print("model loaded from {}".format(path))
    return model

def save_model(model,path):
    joblib.dump(model,path,compress=True)
    print("model saved to {}".format(path))


def save_prediction_to_csv(df,path):
    df.to_csv(path,index=False)
    print("predictions written to {} successfully!".format(path))


def save_feature_names(features,monthEnd):
    filename = "features-{}".format(monthEnd)
    filepath = os.path.join(FEATURE_DIR,filename)
    with open(filepath,'w') as file:
        json.dump(features,file)
    print("Features written to {}".format(filepath))


def read_features_from_disk(monthEnd):
    filename = "features-{}".format(monthEnd)
    filepath = os.path.join(FEATURE_DIR,filename)
    features = []
    with open(filepath) as file:
        features = json.load(file)
    return features