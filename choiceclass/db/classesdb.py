__author__ = 'Mr.Bool'
import pickle

def xieclasses(classes):
    with open("classes.txt",'wb') as wf:
        pickle.dump(classes,wf)
def duclasses():
    with open('classes.txt','rb') as rf:
        return pickle.load(rf)
