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
    last1FS = ''
    last2FS = ''
    features = []
    with open('data/normallized/' + fileName + '.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            break
        skip_first_line = False
        for row in spamreader:
            rawSentence = row[0].split(':::')[0]
            sentence = "^ " + row[0].split(':::')[0] + " $"
            label = row[0].split(':::')[1].split(":")[0]
            contextPredicate = scanFeature(sentence)[0]
            feature = ''
            if(last1FS != ''):
                if(last2FS != ''):
                    feature += ' '.join(contextPredicate) + ' l-1:' + ' l-1:'.join(last1FS.split(" ")) +' l-2:' +' l-2:'.join(last2FS.split(" ")) + ' ' + label
                else:
                    feature += ' '.join(contextPredicate) + ' l-1:' + ' l-1:'.join(last1FS.split(" ")) + ' ' + label
            print rawSentence + ":::::" +last1FS +":::::" + last2FS
            last2FS = last1FS
            last1FS = rawSentence
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
