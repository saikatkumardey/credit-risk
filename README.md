# Predicting Credit Risk

This project uses Machine Learning to predict which loans are at risk depending on the features of the client and loan features.


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

        > python train.py classifierName -n numberOfSamples modelName

Example:

    > python train.py random-forest -n 10000 rf10000

Here, classifier = random-forest, modelName = rf10000

The model will get saved at data/models/rf10000.model
The features will get saved at data/features/rf10000.features

You can run other classifiers by changing the name of the classifier to one from {decision-tree,random-forest,logistic-regression,xgboost}.


For help, run:
        
        python train.py -h


## Running the web-service


**Make sure that you have a pretrained model ready**

**You need to provide the model path. You can modify the default values at ml/config.py or provide it by setting environment variable**

run:

        set MODEL_FILENAME="rf10000" #this will load the model from data/models/rf10000.model
        python wsgi.py #this will run the webservice at port 5000



## How to consume the Web Service ?

Endpoint: http://0.0.0.0:5000/api/predict-batches?monthEnd=101

It has 2 query arguments: monthEnd

monthEnd is the month for which you want to predict.

Response:

### For successful response, statusCode=200

```json
{
  "data": [
    {
      "LoanCode": 0, 
      "bad": 0.0, 
      "good": 100.0
    }, 
    {
      "LoanCode": 1, 
      "bad": 23.0, 
      "good": 77.0
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