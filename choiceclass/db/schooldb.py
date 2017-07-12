__author__ = 'Mr.Bool'
import pickle
import os
# import sys
# BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
#C:\Users\Mr.Bool\Desktop\python作业\classchoice\classchoice\choiceclass\db
if os.path.isfile(os.path.dirname(__file__)+r'\xuexiao.txt'):
    pass
else:
    f=open(os.path.dirname(__file__)+r'\xuexiao.txt','w')
    f.close()
def chuangjianxuexiao(xuexiao):
    with open(os.path.dirname(__file__)+r"\xuexiao.txt",'wb+') as wf:
        print(xuexiao)
        pickle.dump(xuexiao,wf)


def duxuexiao():
    with open(os.path.dirname(__file__)+r"\xuexiao.txt",'rb+') as rf:
        if os.path.getsize(os.path.dirname(__file__)+r"\xuexiao.txt")==0:
            print('还没有学校被创建')
            return []
        else:
            return pickle.load(rf)