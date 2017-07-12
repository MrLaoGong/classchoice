__author__ = 'Mr.Bool'
import pickle
import os
if os.path.isfile(os.path.dirname(__file__)+r'\student.txt'):
    pass
else:
    f=open(os.path.dirname(__file__)+r'\student.txt','w')
    f.close()

'注册学生'
def zhucestu(stu):
    wf=open(os.path.dirname(__file__)+r'\student.txt','wb+')
    pickle.dump(stu,wf)
    wf.close()
'读取注册的学生'
def readstu():
    with open(os.path.dirname(__file__)+r"\student.txt",'rb+') as rf:
        if os.path.getsize(os.path.dirname(__file__)+r"\student.txt")==0:
            print('还没有学生被创建')
            return []
        else:
            return pickle.load(rf)