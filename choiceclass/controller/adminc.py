__author__ = 'Mr.Bool'
from classpackage import school
from classpackage import classes
from classpackage import student
from classpackage import teacher
from classpackage import classroom
from db import studentdb
from db import schooldb
from db import classesdb
from db import classroomdb
from db import teacherdb
schools=[]
teachers=[]
banjis=[]
kechengs=[]
sch=''#学校
banji=''#班级
kecheng=''#课程
'创建学校'
def chuangjianxuexiao():
    schools=schooldb.duxuexiao()
    if len(schools)==0:
        pass
    else:
        for s in schools:
            print('现有学校',s.place)
    schoolname=input("请输入学校名字")
    sch=school.school(schoolname)
    schools.append(sch)
    schooldb.chuangjianxuexiao(schools)
    pass
'创建讲师'
def chuangjianjiangshi():
    teachers=teacherdb.duteacher()
    name=input("请输入讲师名称")
    kechengs=classesdb.duclasses()
    print('目前开设的课程')
    for k in kechengs:
        print(k.classname)
    kecheng=input("请输入讲师教授的课程")
    print('当前可以选择的学校')
    schools=schooldb.duxuexiao()
    for s in schools:
        print(s.place)
    schoolstr=input('请输入你进入的学校')
    jiangshi=teacher.teacher(name,schoolstr,kecheng)
    teachers.append(jiangshi)
    teacherdb.xieteacher(teachers)
    pass
'创建班级'
def chuangjianbanji():
    banjis=classroomdb.duclassroom()
    if len(banjis)==0:
        pass
    else:
        print('目前的班級有')
        for b in banjis:
            print(b.classname)
    classname=input("请输入班级的名称")
    classes=input('请输入班级教授的课程')
    teachername=input('请输入班级的老师')
    banji=classroom.classroom(classname,teachername,classes)
    banjis.append(banji)
    classroomdb.xieclassroom(banjis)
    pass
'创建课程'
def chuangjiankecheng():
    kechengs=classesdb.duclasses()
    if len(kechengs)==0:
        pass
    else:
        print('现有课程')
        for k in kechengs:
            print(k.classname)
    classname=input("请输入你要创建的班级名")
    place=input('请输入开班的学校')
    ke=input('教授的课程')
    cycle=input('开班的周期')
    money=input('学费多少')
    kecheng=classes.classes(classname,place,ke,cycle,money)
    kechengs.append(kecheng)
    classesdb.xieclasses(kechengs)
    pass

'开始'
def start():
    print("1.创建学校")
    print("2.创建讲师")
    print("3.创建班级")
    print("4.创建课程")
    no=input("请输入你选择的功能")

    if no.strip()=='1':
        chuangjianxuexiao()
        pass
    elif no.strip()=='2':
        chuangjianjiangshi()
        pass
    elif no.strip()=='3':
        chuangjianbanji()
        pass
    elif no.strip()=='4':
        chuangjiankecheng()
        pass
    else:
        print("错误序号")
