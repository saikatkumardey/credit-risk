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
    
    print("Columns: ",data.columns)

    cols_to_drop = ['Status','deliquency','pkMonthEnd','clientCode','CreditLineCode']
    for col in cols_to_drop:
        if col in data.columns:
            data = data.drop(col,axis=1)

    print_shape(data)

    if 'pkLoanCode' in data.columns:
        data['pkLoanCode']= data['pkLoanCode'].astype('int64').astype('str')
        data = data.set_index('pkLoanCode')

    X = data

    if 'pkLoanDeliquency' in data.columns:
        X = data.drop('pkLoanDeliquency', axis=1)

    if 'label' in data.columns:
        X = data.drop('label',axis=1)

    print("columns now: ",X.columns)

    not_categorical = ['familyMembers', 'amount_Credit_Request']

    categorical = [col for col in X.columns if col not in not_categorical]

    print("Categorical ",categorical)
    print("Numerical ",not_categorical)

    X_cat_encoded = pd.get_dummies(X, columns=categorical)
    print("After categorical encoding, number of columns = ",
          X_cat_encoded.columns.shape[0])

    if mode == 'train':
        y = data['label']
        print("class distribution : ")
        print(y.value_counts())
        return X_cat_encoded, y
    else:
        # print("Model features ",model_features)
        # print("Current Features",X_cat_encoded.columns)
        print("diff: ",set(X_cat_encoded) - set(model_features))
        X_cat_encoded = fix_columns(X_cat_encoded,model_features)
        # X_cat_encoded = X_cat_encoded[common_columns]
        print("Kept only the features present in the model.")
        print_shape(X_cat_encoded)
        return X_cat_encoded

def fix_columns(df,model_columns):

    df = df.copy()

    current_cols = set(df.columns)
    model_columns = set(model_columns)

    model_cols_not_present_in_current = model_columns - current_cols
    cols_extra = current_cols - model_columns

    print("not present ",model_cols_not_present_in_current)
    print("extra ",cols_extra)

    #drop extra columns
    for col in cols_extra:
        df = df.drop(col,axis=1)
        # print("dropped ",col)

    #add columns not present
    for col in model_cols_not_present_in_current:
        df[col] = 0
        # print("added ",col)

    return df



def split_data(X, y, test_size=0.20):

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=2018)
    return X_train, X_test, y_train, y_test


def print_shape(data):
    rows, cols = data.shape
    print("{} rows and {} cols.".format(rows, cols))


def data_pipeline_for_training(numSamples=10000):

    print("Fetching data")

    bad_loans_sql = sql.get_sql_for_bad_loans(num_rows=numSamples//2)
    good_loans_sql = sql.get_sql_for_good_loans(num_rows=numSamples//2)

    bad_loans_data = db_utils.get_data_from_sqlserver(bad_loans_sql)
    good_loans_data = db_utils.get_data_from_sqlserver(good_loans_sql)

    bad_loans_data['label'] = "bad"
    good_loans_data['label'] = "good" 

    data = pd.concat([bad_loans_data,good_loans_data])
    data = data.sample(frac=1)

    print_shape(data)

    X,y = prepare_data(data,mode='train')

    X_train, X_test, y_train, y_test = split_data(X, y)
    
    return X_train, X_test, y_train, y_test


def data_pipeline_for_prediction(monthEnd,model_features):

    print("Fetching data")
    sql_str = sql.get_sql_for_fetching_data(monthEnd=monthEnd)
    data = db_utils.get_data_from_sqlserver(sql_str)
    X = prepare_data(data,mode='test',model_features=model_features)
    return X