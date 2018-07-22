import plac
import sys
from app.ml.modelling import models
from pathlib import Path


@plac.annotations(
    classifier=("Name of the classifier",'positional',None,str,list(models.keys())),
    filename = ("Name of the model file",'positional',None,str),
    numSamples = ("Number of training samples.",'option',None,int,None,'n'),
)
def main(classifier,filename,numSamples=10000):
    '''
    example: python train.py random-forest -n 10000 rf
    '''

    from app.ml.pipeline import train
    train(classifierName=classifier,numSamples=numSamples,modelFileName=filename)


if __name__ == '__main__':
    plac.call(main)