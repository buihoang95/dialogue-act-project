import codecs
import csv
import re
dialogueList = []

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

    # convertDataToNormalizeData('diana')
    # convertDataToNormalizeData('eleanor')
    # convertDataToNormalizeData('q1ec6')
    # convertDataToNormalizeData('sw00-0004')
    # convertDataToNormalizeData('sw01-0105')
    # convertDataToNormalizeData('sw02-0224')
    # convertDataToNormalizeData('TRAINS-1-gold')
    # convertDataToNormalizeData('TRAINS-2-gold')
    # convertDataToNormalizeData('TRAINS-3-gold')
    # convertDataToNormalizeData('venus')
    # convertDataToNormalizeData('washington')


if __name__ == '__main__':
    main()
