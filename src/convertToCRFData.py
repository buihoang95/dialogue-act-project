import codecs
import os
import csv
import re
dialogueList = []
file = open('data/normallizedCRF/' + "CRFdata" + '.csv','wb')

def convertDataToNormalizeData(fileName):
    overallData=[]
    with open('data/normallized/' + fileName + '.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            break
        data=[]
        count = 0
        for row in spamreader:
            item=row[0].split(':::');
            item[1]=item[1].split(':')[0]
            data.append('<'+item[1]+'>'+item[0]+'</'+item[1]+'>')
            count+=1
            if(count == 15):
                overallData.append(' '.join(data))
                data=[]
                count=0
        file.write('Data')
        file.write('\n')
        file.write('\n'.join(overallData))



def main():
    for file in os.listdir('./data/normallized'):
        if file.endswith('.csv'):
            file_name = file[:-4]
            convertDataToNormalizeData(file_name)

if __name__ == '__main__':
    main()
