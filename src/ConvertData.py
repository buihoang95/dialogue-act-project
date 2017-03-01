import codecs
import csv
import re
dialogueList = []

def readCSVData():
    content = codecs.open('data/sampleData.csv', 'r', 'utf-8').read()
    return content


def convertDataToNormalizeData(fileName):
    result = []
    with open('data/' + fileName + '.csv', 'rb') as csvfile:
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
        file = open('data/Normalized' + fileName + '.csv','w')
        file.write('Data')
        file.write('\n')
        file.write('\n'.join(result))
        file.close()



def main():
    # # convertRawData2()
    convertDataToNormalizeData('trains-1-gold')
    convertDataToNormalizeData('trains-2-gold')
    convertDataToNormalizeData('trains-3-gold')
    convertDataToNormalizeData('dbox-washington')
    convertDataToNormalizeData('dbox-diana')
    convertDataToNormalizeData('sw00-0004')
    convertDataToNormalizeData('sw01-0105')
    convertDataToNormalizeData('sw02-0224')
    convertDataToNormalizeData('q1ec6')
    convertDataToNormalizeData('q1ec7')



if __name__ == '__main__':
    main()
