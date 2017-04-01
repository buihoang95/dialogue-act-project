import codecs
import os
import csv
import re
dialogueList = []

def convertDataToNormalizeData(fileName):
    result = []
    with open(fileName, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            row[0].lower()
            label = 'chunk=b-' + row[0].lower() + ":i-" + row[0].lower() +':'+row[0].lower()
            result.append(label)
        file = open('data/convertLabel.txt' ,'w')
        file.write('\n'.join(result))
        file.close()



def main():
    convertDataToNormalizeData('data/label.txt')

if __name__ == '__main__':
    main()
