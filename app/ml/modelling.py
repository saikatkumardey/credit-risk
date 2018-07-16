from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
import pandas as pd


def train_decision_tree_classifier(X_train,y_train):
    
    dt = DecisionTreeClassifier()
    dt.fit(X_train,y_train)
    return dt

def train_random_forest_classifier(X_train,y_train):

    rf = RandomForestClassifier(n_estimators=100,n_jobs=-1)
    rf.fit(X_train,y_train)
    return rf

def train_logistic_regression_classifier(X_train,y_train):

    lr= LogisticRegression(class_weight='balanced',n_jobs=-1,max_iter=1000,C=100)
    lr.fit(X_train, y_train)
    return lr

def train_xgboost_classifier(X_train,y_train):

    xgb = XGBClassifier()
    xgb.fit(X_train,y_train)
    return xgb

models = {
    'decision-tree': train_decision_tree_classifier,
    'random-forest': train_random_forest_classifier,
    'logistic-regression': train_logistic_regression_classifier,
    'xgboost': train_xgboost_classifier
}