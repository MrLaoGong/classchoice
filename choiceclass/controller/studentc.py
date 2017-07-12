__author__ = 'Mr.Bool'
import pickle
from classpackage import student
from db import studentdb
from db import schooldb
from db import classesdb
from db import classroomdb
stuname=''
stus=[]
def login(func):
    def test():
            name = input("请输入名字")
            password=input("请输入密码")
            stus=studentdb.readstu()
            if len(stus)==0:
                pass
            else:
                for stu in stus:
                    if name==stu.name and stu.password==password:
                        stu.show()
                        stuname=stu.name
            func()

    return test
'交学费'

def jiaoxuefei(stuname):
    stus=studentdb.readstu()
    for s in stus:
        if stuname==s.name:
            s.xuefei='yes'
    studentdb.zhucestu(stus)
    print(stuname,'缴费成功')
'注册'
def zhuce(name,password):
    stus=studentdb.readstu()
    stu=student.student(name,password)
    stus.append(stu)
    studentdb.zhucestu(stus)
    print('注册成功')
'选择班级'

def xuanzebanji(stuname):
    schools=schooldb.duxuexiao()
    for school in schools:
        print(school.place)
    place=input("请输入逆选择的学校地址")
    classes=classesdb.duclasses()
    for classe in classes:
        print(classe.classname)
    classe=input("请输入逆选择的课程")
    classrooms=classroomdb.duclassroom()
    for classroom in classrooms:
        if classroom.classes==classe:
            print(classroom.classname,'老师是',classroom.teacher)
    classroom=input("请输入逆选择的班级")
    stus=studentdb.readstu()
    for s in stus:
        if s.name==stuname:
            s.school=place
            s.classes=classes
            s.banji=classroom
    studentdb.zhucestu(stus)
def test():
    name = input("请输入名字")
    password=input("请输入密码")
    stus=studentdb.readstu()
    print(len(stus))
    if len(stus)==0:
        pass
    else:
        for stu in stus:
            if name==stu.name and stu.password==password:
                stu.show()
                stuname=stu.name
                return stu
            else:
                print('登录失败')
def start():
    print('1.注册')
    print('2.交学费')
    print("3.选择班级")
    num=input('请输入你的选择')
    if num=='1':
        '注册学生'
        name=input('请输入名字')
        password=input("请输入密码")
        zhuce(name,password)
        pass
    elif num=='2':
        '交学费需要先登录'
        stu=test()
        jiaoxuefei(stu.name)
        pass
    elif num=='3':
        "先登录选择学校课程班级"
        stu=test()
        xuanzebanji(stu.name)
        pass
    else:
        print("错误的输入！")



