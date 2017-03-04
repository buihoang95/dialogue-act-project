# -*- coding: utf-8 -*-
import os

CSV_PATH = '../data'
NORMALLIZED_PATH = '../normallized'

LABEL_DATA = ['question', 'propositionalQuestion', 'setQuestion', 'checkQuestion', 'choiceQuestion', 'inform', 'agreement', 'disagreement', 'correction', 'answer', 'confirm', 'disconfirm', 'promise', 'offer','addressRequest', 'acceptRequest', 'declineRequest', 'addressSuggest', 'acceptSuggest', 'declineSuggest','request', 'instruct', 'addressOffer', 'suggest', 'acceptOffer', 'declineOffer', 'autoPositive', 'autoNegative', 'alloPositive', 'alloNegative', 'feedbackElicitation', 'turnAccept', 'turnAssign', 'turnGrab', 'turnKeep', 'turnRelease', 'turnTake', 'stalling', 'pausing', 'interactionStructuring', 'opening', 'selfError', 'retraction', 'selfCorrection', 'completion', 'correctMisspeaking', 'initialGreeting', 'returnGreeting', 'initialSelfIntroduction', 'returnSelfIntroduction', 'apology', 'acceptApology', 'thanking', 'acceptThanking', 'initialGoodbye', 'returnGoodbye', 'guess', 'confirm', 'closing', 'congratulation']

LABEL_COUNT = [0] * len(LABEL_DATA)

def normallize(csv_path, normallized_path):
    for file in os.listdir(csv_path):
        if file.endswith('.csv'):
            file_name = file[:-4]
            normallize_one('%s/%s'%(CSV_PATH, file), '%s/%s'%(NORMALLIZED_PATH, file))
    for index, label in enumerate(LABEL_DATA):
	print label, LABEL_COUNT[index]

def normallize_one(csv_path, normallized_path):
    fi = open(csv_path, 'rb')
    fo = open(normallized_path, 'wb')
    contents = fi.readlines()
    for index, content in enumerate(contents):
        if index == 0 or index == 1:
            continue
        # split content in csv
        line_arr = content.split(',')
        # concat all labels
        label_arr = []
        for label in line_arr[5:-1]:
    	    label = label.strip()
            if label != '':
                label_index = LABEL_DATA.index(label)
                LABEL_COUNT[label_index] += 1
                label_arr.append(label)
        if len(label_arr) == 0:
            continue
        labels = ':'.join(label_arr)
        # get functional segment
        fs = line_arr[4].lower().strip()
        if fs.endswith('.') and fs[-2] != '.':
            fs = fs[:-1]
        # remove turn description
        line_arr = line_arr[0:3]
        line_arr.append(fs)
        line_arr.append(labels)
        new_line = ','.join(line_arr) + '\n'
        fo.write(new_line)

    fi.close()
    fo.close()

if __name__ == '__main__':
    normallize(CSV_PATH, NORMALLIZED_PATH)
