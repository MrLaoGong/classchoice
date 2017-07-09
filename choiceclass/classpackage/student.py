__author__ = 'Mr.Bool'
'''学生'''

class student(object):
    def __init__(self,name,password):
        self.name=name
        self.password=password
        self.xuefei='no'
        self.banji='no'
    def show(self):
        print("学生：",self.name,"学费:",self.xuefei,"班级：",self.banji)