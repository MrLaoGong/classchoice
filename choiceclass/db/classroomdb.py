__author__ = 'Mr.Bool'
import pickle
import os
if os.path.isfile(os.path.dirname(__file__)+r'\classroom.txt'):
    pass
else:
    f=open(os.path.dirname(__file__)+r'\classroom.txt','w')
    f.close()
def xieclassroom(classroom):
    with open(os.path.dirname(__file__)+r'\classroom.txt','wb') as wf:
        pickle.dump(classroom,wf)
def duclassroom():
      with open(os.path.dirname(__file__)+r"\classroom.txt",'rb+') as rf:
        if os.path.getsize(os.path.dirname(__file__)+r"\classroom.txt")==0:
            print('还没有班级被创建')
            return []
        else:
            return pickle.load(rf)