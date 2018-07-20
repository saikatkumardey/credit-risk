import os
MODEL_DIR = os.environ.get("MODEL_PATH",'data/models')
MODEL_FILENAME = os.environ.get("MODEL_FILENAME",'rf') # modify this or the environment variable
FEATURE_DIR = os.environ.get("FEATURE_DIR",'data/features')
TRAINING_MONTH = int(os.environ.get("TRAINING_MONTH",100))