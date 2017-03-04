import csv


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
    with open('data/' + fileName + '.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            break
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
        file.write('\n'.join(features))

def main():
    featureGeneration('Normalizeddbox-diana')
    featureGeneration('Normalizeddbox-washington')
    featureGeneration('Normalizedq1ec6')
    featureGeneration('Normalizedq1ec7')
    featureGeneration('Normalizedsw00-0004')
    featureGeneration('Normalizedsw01-0105')
    featureGeneration('Normalizedsw02-0224')
    featureGeneration('Normalizedtrains-1-gold')
    featureGeneration('Normalizedtrains-2-gold')
    featureGeneration('Normalizedtrains-3-gold')

    #
    # featureGeneration('Normalizeddiana')
    # featureGeneration('Normalizedeleanor')
    # featureGeneration('Normalizedq1ec6')
    # featureGeneration('Normalizedsw00-0004')
    # featureGeneration('Normalizedsw01-0105')
    # featureGeneration('Normalizedsw02-0224')
    # featureGeneration('NormalizedTRAINS-1-gold')
    # featureGeneration('NormalizedTRAINS-2-gold')
    # featureGeneration('NormalizedTRAINS-3-gold')
    # featureGeneration('Normalizedvenus')
    # featureGeneration('Normalizedwashington')

if __name__ == '__main__':
    main()
