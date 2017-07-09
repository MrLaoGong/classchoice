__author__ = 'Mr.Bool'
import pickle


'注册学生'
def zhucestu(stu):
    wf=open(r'student.txt','w+')
    pickle.dump(stu,wf)
    wf.close()
'读取注册的学生'
def readstu():
    rf=open(r'student.txt','r')
    stus=pickle.load(rf)
    return stus