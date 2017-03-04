import codecs
import os
import csv
import re
dialogueList = []

def convertDataToNormalizeData(fileName):
    result = []
    with open('data/raw/' + fileName + '.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            break
        for row in spamreader:
            row[3]=row[3].strip("/. , ; / ( ) / { }[\" ] # $ @ ! % ^ & * +/-\ _ /")
            row[3]=row[3].strip(' \t\n\r')
            row[3]=row[3].lstrip()
            row[3]=row[3].rstrip()
            for item in row[4:]:
                if item!='' and item!=' ':
                    result.append(row[3]+':::'+item.split(' ')[0])
                    break
        print len(result)
        file = open('data/normallized/' + fileName + '.csv','w')
        file.write('Data')
        file.write('\n')
        file.write('\n'.join(result))
        file.close()



def main():
    for file in os.listdir('./data/raw'):
        if file.endswith('.csv'):
            file_name = file[:-4]
            convertDataToNormalizeData(file_name)

if __name__ == '__main__':
    main()
