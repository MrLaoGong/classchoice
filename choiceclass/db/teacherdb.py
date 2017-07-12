__author__ = 'Mr.Bool'
import pickle
import os
if os.path.isfile(os.path.dirname(__file__)+r'\teacher.txt'):
    pass
else:
    f=open(os.path.dirname(__file__)+r'\teacher.txt','w')
    f.close()
'读取老师'
def duteacher():
     with open(os.path.dirname(__file__)+r"\teacher.txt",'rb+') as rf:
        if os.path.getsize(os.path.dirname(__file__)+r"\teacher.txt")==0:
            print('还没有老师被创建')
            return []
        else:
            return pickle.load(rf)
'写老师'
def xieteacher(teacher):
    with open(os.path.dirname(__file__)+r"\teacher.txt",'wb') as wf:
        pickle.dump(teacher,wf)