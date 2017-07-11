__author__ = 'Mr.Bool'
import pickle
def xieclassroom(classroom):
    with open("classroom.txt",'wb') as wf:
        pickle.dump(classroom,wf)
def duclassroom():
    with open("classroom.txt",'rb') as rf:
        return pickle.load(rf)