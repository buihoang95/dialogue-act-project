import csv
import os

file = open('data/feature' + '.tagged','w')

def scanFeature(sentence):
    contextPredicates = []
    tokens = sentence.split(' ')
    tokenLengh = len(tokens)
    for i in range(tokenLengh):
        #1-gram
        cp = tokens[i]
        if (i != 0) and (i != tokenLengh - 1):
            # if (i != tokenLengh - 1):
            contextPredicates.append(cp)

        #2-gram
        if (i < tokenLengh - 1):
            cp = tokens[i] + ':' + tokens[i+1]
            contextPredicates.append(cp)

        #3-gram
        if (i < tokenLengh - 2):
            cp = tokens[i] + ':' + tokens[i+1] + ':' + tokens[i+2]
            contextPredicates.append(cp)

        #4-gram
        if (i < tokenLengh - 3):
            cp = tokens[i] + ':' + tokens[i+1] + ':' + tokens[i+2] + ':' + tokens[i+3]
            contextPredicates.append(cp)

    return [contextPredicates]

def featureGeneration(fileName):
    last1Lable = ''
    last2Lable = ''
    features = []
    with open('data/normallized/' + fileName + '.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            break
        skip_first_line = False
        for row in spamreader:
            sentence = "^ " + row[0].split(':::')[0] + " $"
            label = row[0].split(':::')[1].split(":")[0]
            contextPredicate = scanFeature(sentence)[0]
            feature = ''
            if(last1Lable != ''):
                if(last2Lable != ''):
                    feature += ' '.join(contextPredicate) + ' l-1:' + last1Lable +' l-2:'+last2Lable + ' ' + label
                else:
                    feature += ' '.join(contextPredicate) + ' l-1:' + last1Lable + ' ' + label
            last2Lable = last1Lable
            last1Lable = label
            # feature += ' '.join(contextPredicate) + ' ' + label
            features.append(feature)
            file.write(feature)
            if skip_first_line == False:
                skip_first_line = True
                continue
            file.write('\n')

def main():
    for file in os.listdir('./data/normallized'):
        if file.endswith('.csv'):
            file_name = file[:-4]
            featureGeneration(file_name)

if __name__ == '__main__':
    main()
