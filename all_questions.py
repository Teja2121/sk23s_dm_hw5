import pytest
from all_questions import *
import pickle



#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    # P(B=good) * P(F=empty) * P(G=empty∣B=good,F=empty) * P(S=yes∣B=good,F=empty) = 0.9 * 0.2 * 0.8 * 0.2
    answers['(a)'] = 0.0288

    # type: float
    # Calculate the probability.
    # P(B=bad) * P(F=empty) * P(G=notempty∣B=bad,F=empty) * P(S=no∣B=bad,F=empty) = 0.1 * 0.2 * 0.1 * 1.0
    answers['(b)'] = 0.002

    # type: float
    # Calculate the probability.
    # we have to calculate P(S=yes|B=bad) = P(S=yes|B=bad,F=empty) + P(S=yes|B=bad,F=notempty) = 0 + 0.1
    answers['(c)'] = 0.1
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = True

    # type: False
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] = True

    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.
    # forumula in terms of p is: (1/2) * (ln((1-p)/p)) = 0.5 * ln((1-0.3)/0.3) = 0.4236489301936019
    p = 0.3
    # proper expression on python is ((1/2)) * math.log((1 - p) / p))
    answers['(c) Weight update'] = '((1/2)) * ln((1 - p) / p))'
    print(answers['(c) Weight update'])
    # type: float
    # the answer should be correct to 3 significant digits
    # 1 * e^(0.42364893019360184)
    answers['(d) Weight influence'] = 1.5275252
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = 'No, I do not agree'

    # type: explain_string
    answers['Explain'] = 'In this case, each coin flip has an error rate of 0.5 and 1000 flips is considered an ensemble of independent classifiers here. Though it is true that ensemble of independent classifiers could potentially get better prediction only if the error rate is less than 0.5. The ground probability would not change.'
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = False

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = 'iii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = 'i'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = 'ii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = 'iv'
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = None  

    # type: eval_float
    answers['(a) C2-TPR'] = None

    # type: eval_float
    answers['(a) C1-FPR'] = None

    # type: eval_float
    answers['(a) C2-FPR'] = None

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = None

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = None

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = None

    # type: explain_string
    answers['(c) explain'] = None
    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = None

    # type: explain_string
    answers['(i) Best classifier, explain'] = None

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = None

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = None

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = None

    # type: explain_string
    answers['(iii) best classifier, explain'] = None
    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] = None

    # type: eval_float
    answers['(a) recall for C0'] = None

    # type: eval_float
    answers['(b) F-measure of C0'] = None

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = None

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = None
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    #recall = tp/(tp+fn) = 80/(80+70) = 0.533333333333333333
    #precision = tp/(tp+fp) = 80/(80+50) = 0.61538461538461538
    #f-measure =  2 * ((precison * recall)/(precison + recall)) = 2 * ((0.61538461538461538 * 0.533333333333333333)/(0.61538461538461538 + 0.533333333333333333)) = 0.571428571428571428571
    #accuracy = (tp+tn)/(tp+tn+fp+fn) = (80+800) / 1000 = 0.88
    answers['(i) metrics'] = {'recall' : 0.533333333333333333, 'precision' : 0.61538461538461538, 'F-measure' : 0.571428571428571428571, 'accuracy' : 0.88}

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = 'F-measure'

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'accuracy'

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = 'There is a class imbalance in this case where there are less positive cases and more negative cases, so accuracy is not good and in this situation F-1 measure is better.'
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = 'T1'

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = 'T2'

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = 'TPR/FPR'

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = 'TPR/FPR is better because in this case, class imbalance (skew) is not known. T2 also has lower FPR but the same TPR.'

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = 'If there is class imbalance case and lets say if there is an email service for filtering spam email, using TPR/FPR might not be good because even if FPR is low, many emails get misclassified to spam even if they might be legit. So F1 score is better because it balances catching as many spam emails as possible (high recall) with not marking good emails as spam (high precision)'
    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
