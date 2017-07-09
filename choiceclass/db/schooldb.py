__author__ = 'Mr.Bool'
import pickle
def chuangjianxuexiao(xuexiao):
    with open("xuexiao.txt",'w') as wf:
        pickle.dump(xuexiao,wf)


def duxuexiao():
    with open("xuexiao.txt",'r') as rf:
        return pickle.load(rf)