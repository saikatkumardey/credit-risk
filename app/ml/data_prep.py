from app.utils import db_utils
from app.utils import sql
import pandas as pd
from sklearn.model_selection import train_test_split

def prepare_data(data,mode='train',model_features=[]):
    '''
    data preparation pipeline.
    if mode = 'train', then returns Feature/Label
    if mode = 'test', then returns only the features
    '''

    if mode == 'test' and len(model_features) == 0:
        raise Exception("You must specify the model features!")

    print_shape(data)

    data = data.dropna()  # remove rows having null
    data = data.drop('Status', axis=1)  # drop status
    data = data.drop('Deliquency', axis=1)  # drop deliquency column
    # the column pkMonthEnd is useless as well, let's remove it
    data = data.drop('pkMonthEnd', axis=1)
    data = data.drop('clientCode', axis=1)
    data = data.drop('CreditLine',axis=1)
    print_shape(data)

    data['LoanCode']= data['LoanCode'].astype('str')
    data = data.set_index('LoanCode')

    X = data.drop('pkLoanDeliquency', axis=1)

    if mode=='train':
        y = data.pkLoanDeliquency
        class_map = {i: "good" if i <= 3 else "bad" for i in range(1, 6)}
        y = y.map(class_map)
        print("class distribution : ")
        print(y.value_counts())

    not_categorical = ['average_Overdue_days',
                       'familyMembers', 'amount_Credit_Request']

    categorical = [col for col in X.columns if col not in not_categorical]

    X_cat_encoded = pd.get_dummies(X, columns=categorical)
    print("After categorical encoding, number of columns = ",
          X_cat_encoded.columns.shape[0])

    if mode == 'train':
        return X_cat_encoded, y
    else:
        X_cat_encoded = X_cat_encoded[model_features]
        print("Kept only the features present in the model.")
        print_shape(X_cat_encoded)
        return X_cat_encoded


def split_data(X, y, test_size=0.20):

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=2018)
    return X_train, X_test, y_train, y_test


def print_shape(data):
    rows, cols = data.shape
    print("{} rows and {} cols.".format(rows, cols))


def data_pipeline_for_training(monthEnd):

    print("Fetching data")

    sql_str = sql.get_sql_for_fetching_data(monthEnd=monthEnd)
    data = db_utils.get_data_from_sqlserver(sql_str)
    X, y = prepare_data(data,mode='train')
    X_train, X_test, y_train, y_test = split_data(X, y)
    return X_train, X_test, y_train, y_test


def data_pipeline_for_prediction(monthEnd,model_features):

    print("Fetching data")
    sql_str = sql.get_sql_for_fetching_data(monthEnd=monthEnd)
    data = db_utils.get_data_from_sqlserver(sql_str)
    X = prepare_data(data,mode='test',model_features=model_features)
    return X