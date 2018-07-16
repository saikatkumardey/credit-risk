# Predicting Credit Risk

This project uses Machine Learning to predict which loans are at risk depending on the features of the client and loan features.

It contains scripts to 

# Requirements:

    Anaconda
    python 3.6+


# How to install?

+ Download and install Anaconda from 

    For windows: https://repo.anaconda.com/archive/Anaconda3-5.2.0-Windows-x86_64.exe


+ Create a virtual environment

    conda create -n credit-risk python=3.6

+ Activate virtual environment

    activate credit-risk # for windows

+ Install all the dependencies

    pip install -r requirements.txt #assuming that you are in creditrisk directory


# How to run it?

There are two options:
+ training the model
+ running the web-service to make predictions

But first, we must set the appropriate environment variables.

## Most important Step

Set appropriate Environment Variables. The given values are the default ones.

        SERVER = "localhost"
        USERNAME = "sa"
        PASSWORD = "reallyStrongPwd123"
        DATABASE = "DW_AccessBI"
        PORT = 1433

**You can also go to app/utils/db_utils.py and modify the defaults**

For windows, you can set an environment variable by running,

        set KEY=VALUE


## Training the model

To train the models, run:

        > python train.py monthEndValue classifierName pathToSaveModel

Example:

    > python train.py 101 random-forest data/models/rf-model

Here, monthEnd = 101, classifier = random-forest, path = data/models/rf-model

You can run other classifiers by changing the name of the classifier to one from {decision-tree,random-forest,logistic-regression,xgboost}.


For help, run:
        
        python train.py -h


## Running the web-service


**Make sure that you have a pretrained model ready**

**You need to provide the model path. You can modify the default values at ml/config.py or provide it by setting environment variable**

run:

        set MODEL_PATH="data/models/rf-87.model" #for windows
        python wsgi.py #this will run the webservice at port 5000



## How to consume the Web Service ?

Endpoint: http://0.0.0.0:5000/api/predict?monthEnd=101&trainingMonth=100

It has 2 query arguments: monthEnd and trainingMonth.

monthEnd is the month for which you want to predict.
trainingMonth is the month for which you had trained your model.

So, according to the endpoint, we've trained a model for month=100 and we want to predict for month=101, hence, trainingMonth=100 and monthEnd=101.

Response:

### For successful response, statusCode=200

```json
{
  "data": [
    {
      "LoanCode": 0.0, 
      "bad": 0.0, 
      "good": 1.0
    }, 
    {
      "LoanCode": 1.0, 
      "bad": 0.0, 
      "good": 1.0
    }
  ],
  "status": "successful",
}
```

### For unsuccssful response, statusCode = 500

```json
{
  "data": [],
  "status": "unsuccessful",
  "error": "details of error that happened"
}

```