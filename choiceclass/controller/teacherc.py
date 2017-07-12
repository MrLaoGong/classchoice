__author__ = 'Mr.Bool'
from classpackage import school
from classpackage import classes
from classpackage import school
from classpackage import student
from classpackage import teacher
from db import studentdb
from db import schooldb
from db import classesdb
from db import classroomdb
from db import teacherdb
schools=[]
teachers=[]
banjis=[]
kechengs=[]

def start():
    teachername=input("请输入您的名字")
    print("1.选择上课班级")
    print("2.查看班级成员")
    print("3.修改学生成绩")
    no=input("请输入你要选择的功能")
    if no.strip()=='1':
        xuanzebanji(teachername)
        pass
    elif no.strip()=='2':
        chakanchengyuan(teachername)
        pass
    elif no.strip()=='3':
        xiugaichengji()
        pass
    else:
        print("错误输入！")
'选择上课班级'
def xuanzebanji(teachername):
    banjis=classroomdb.duclassroom()
    for b in banjis:
        if teachername==b.teacher:
            print(b.classname)
            banji=b
    classname=input('请输入你选择上课的班级')
    print(teachername,'正在给',classname,'上',banji.classes)
    pass

'查看班级成员'
def chakanchengyuan(teachername):
     banjis=classroomdb.duclassroom()
     banji=''
     for b in banjis:
          if teachername==b.teacher:
            print(b.classname)
     students=studentdb.readstu()
     banjiname=input('请输入你想查看的班级')
     print('班级成员：')
     for s in students:
         if s.banji==banjiname:
             print(s.name)

'修改学生成绩'
def xiugaichengji():
    stuname=input('请输入学生名字')
    students=studentdb.readstu()
    for s in students:
         if s.name==stuname:
            print('现在该学生成绩为',s.chengji)
            chengji=input('请输入学生成绩')
            s.chengji=chengji
    studentdb.zhucestu(students)