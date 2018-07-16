import plac
import sys
from app.ml.modelling import models
from pathlib import Path


@plac.annotations(
    monthEnd=("The monthEnd for which data should be fetched",'positional',None,int),
    classifier=("Name of the classifier",'positional',None,str,list(models.keys())),
    path = ("Path where the model should be saved",'positional',None,Path)
)
def main(monthEnd,classifier,path):
    '''
    example: python cli.py 101 random-forest data/models/rf-model
    '''

    from app.ml.pipeline import train
    train(monthEnd=monthEnd,classifierName=classifier,path_to_save=path)


if __name__ == '__main__':
    plac.call(main)