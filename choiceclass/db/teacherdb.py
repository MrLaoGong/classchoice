__author__ = 'Mr.Bool'
import pickle

'读取老师'
def duteacher():
    with open('teacher.txt','rb') as rf:
        return pickle.load(rf)
'写老师'
def xieteacher(teacher):
    with open('teacher.txt','wb') as wf:
        pickle.dump(teacher,wf)