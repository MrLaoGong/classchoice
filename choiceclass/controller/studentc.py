__author__ = 'Mr.Bool'
import pickle
from classpackage import student
from db import studentdb
from db import schooldb
from db import classesdb
from db import classroomdb
stu=''
stus=''
print('1.注册')
print('2.交学费')
print("3.选择班级")
num=input('请输入你的选择')
def login(func):
    def test():
        name = input("请输入名字")
        password=input("请输入密码")
        stus=studentdb.readstu()
        for stu in stus:
            if name==stu.name and stu.password==password:
                stu.show()
        func()
    return test
'交学费'
@login
def jiaoxuefei():
    for s in stus:
        if stu.name==s.name:
            s.xuefei='yes'
    studentdb.zhucestu(stus)
    print(stu.name,'缴费成功')
'注册'
def zhuce(name,password):
    stu=student(name,password)
    studentdb.zhucestu(stu)
    print('注册成功')
'选择班级'
@login
def xuanzebanji():
    schools=schooldb.duxuexiao()
    for school in schools:
        print(school.place)
    place=input("请输入逆选择的学校地址")
    classes=classesdb.duclasses()
    for classe in classes:
        print(classes.classname)
    classe=input("请输入逆选择的课程")
    classrooms=classroomdb.duclassroom()
    for classroom in classrooms:
        print(classroom.classno,'老师是',classroom.teacher)
    classroom=input("请输入逆选择的班级")
    for s in stus:
        if s.name==stu.name:
            s.school=place
            s.classes=classes
            s.banji=classroom
    studentdb.zhucestu(stus)


if num=='1':
    '注册学生'
    name=input('请输入名字')
    password=input("请输入密码")
    zhuce(name,password)
    pass
elif num=='2':
    '交学费需要先登录'
    jiaoxuefei()
    pass
elif num=='3':
    "先登录选择学校课程班级"
    xuanzebanji()
    pass
else:
    print("错误的输入！")



