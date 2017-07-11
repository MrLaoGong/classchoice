__author__ = 'Mr.Bool'
import pickle
def chuangjianxuexiao(xuexiao):
    with open("xuexiao.txt",'wb') as wf:
        pickle.dump(xuexiao,wf)


def duxuexiao():
    with open("xuexiao.txt",'rb') as rf:
        return pickle.load(rf)