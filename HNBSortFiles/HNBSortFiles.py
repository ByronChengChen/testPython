from ast import NotIn
from curses import flash
from fileinput import filename
from genericpath import exists
from hashlib import new
from importlib.metadata import files
import os
from pickle import FALSE
import shutil
from sre_parse import FLAGS
import string
from tabnanny import filename_only
from tracemalloc import start
import time

desPath = '/Users/chengkang/Desktop/testPythonDes'
srcPath = '/Users/chengkang/Desktop/testPythonSrc'
desExists = os.path.exists(desPath)
srcExists = os.path.exists(srcPath)
if(desExists == FALSE or srcExists == FALSE):
    exit
for fileName in os.listdir(srcPath):
    fileFullPath = os.path.join(srcPath,fileName)
    if os.path.isfile(fileFullPath):
        fileSt = os.stat(fileFullPath)
        fileCtime = fileSt.st_birthtime
        timeArray = time.localtime(fileCtime)
        timeStr = time.strftime("%Y_%m",timeArray)
        print(fileName)
        fileNameMonth = timeStr
        # 生成新目录
        newDir = os.path.join(desPath,fileNameMonth)
        if(os.path.exists(newDir)):
            print(newDir)
        else:
            os.mkdir(newDir)
        # 将文件移动到新的文件夹下
        shutil.move(fileFullPath,os.path.join(desPath,fileNameMonth))
    else:
        continue

print("end")
