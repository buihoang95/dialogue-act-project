import codecs
import os
import csv
import re
import random

dialogueList = []

def convertDataToNormalizeData():
    result = []
    with open('data/feature.tagged', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            result.append(row[0])
        random.shuffle(result)
        testSize = len(result)/5
        head=0
        for i in range(1,6):
            random.shuffle(result)
            fileTrain = open('data/crossValidationData/train'+ str(i) +'.tagged','w')
            fileTest = open('data/crossValidationData/test'+ str(i) +'.tagged','w')

            fileTest.write('\n'.join(result[head:testSize+head]))
            train = result[0:head]+result[testSize+head:]
            fileTrain.write('\n'.join(train))
            head+=testSize




def main():
    convertDataToNormalizeData()

if __name__ == '__main__':
    main()
