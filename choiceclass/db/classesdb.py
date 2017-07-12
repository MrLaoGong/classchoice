__author__ = 'Mr.Bool'
import pickle
import os
print('classes：路径',os.path.dirname(__file__))
if os.path.isfile(os.path.dirname(__file__)+r'\classes.txt'):
    pass
else:
    f=open(os.path.dirname(__file__)+r'\classes.txt','w')
    f.close()
def xieclasses(classes):
    with open(os.path.dirname(__file__)+r'\classes.txt','wb') as wf:
        pickle.dump(classes,wf)
def duclasses():
      with open(os.path.dirname(__file__)+r"\classes.txt",'rb+') as rf:
        if os.path.getsize(os.path.dirname(__file__)+r"\classes.txt")==0:
            print('还没有课程被创建')
            return []
        else:
            return pickle.load(rf)

