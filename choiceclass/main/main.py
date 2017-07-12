__author__ = 'Mr.Bool'
import sys
import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from controller import adminc
from controller import studentc
from controller import teacherc
while True:
    print("1.学生入口")
    print("2.讲师入口")
    print("3.管理员入口")
    num=input("请输入您选择的序号入口，输入b退出")
    if num.strip()=='1':
        '学生入口'
        studentc.start()
        pass
    elif num.strip()=='2':
        '讲师入口'
        teacherc.start()
        pass
    elif num.strip()=='3':
        '管理员入口'
        adminc.start()
        pass
    elif num.strip()=='b':
        sys.exit()
    else:
        print("错误序号！！！")