from ast import NotIn
from curses import flash
from fileinput import filename
from genericpath import exists
import getopt
from hashlib import new
from importlib.metadata import files
import os
from pickle import FALSE
import shutil
from sre_parse import FLAGS
import sys
from tabnanny import filename_only
from tracemalloc import start
import time
import UseFileType

def sortFile(desPath):
    desExists = os.path.exists(desPath)
    if(desExists == False):
        exit

    vPath = os.path.join(desPath,"video")
    pPath = os.path.join(desPath,"picture")
    if os.path.exists(vPath) is False:
        os.makedirs(vPath)
    if os.path.exists(pPath) is False:
        os.makedirs(pPath)
        
    for fileName in os.listdir(desPath):
        fileFullPath = os.path.join(desPath,fileName)
        if os.path.isfile(fileFullPath):
            fileSt = os.stat(fileFullPath)
            fileCtime = fileSt.st_birthtime
            timeArray = time.localtime(fileCtime)
            timeStr = time.strftime("%Y_%m",timeArray)

            # 按文件类型生成新目录 path + video/picture + year_month + _p/_v
            dirVP = None
            yearMonthVP = None
            hnbType = UseFileType.getFileType(fileFullPath)
            if(hnbType is UseFileType.HnbFileType.HnbV):
                dirVP = vPath
                yearMonthVP = timeStr + "_v"
            elif(hnbType is UseFileType.HnbFileType.HnbP):
                dirVP = pPath
                yearMonthVP = timeStr + "_p"
            else:
                print("srcFile:" + __file__ + ",line:" + str(sys._getframe().f_lineno) + "\n" + fileName + " file unknow type")
                continue
            newDir = os.path.join(dirVP,yearMonthVP)
            if(os.path.exists(newDir) is False):
                os.makedirs(newDir)

            # 将文件移动到新的文件夹下
            shutil.move(fileFullPath,newDir)
        else:
            continue

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(sys.argv) > 1:
        try:
            opts, args = getopt.getopt(args, "-i:-h", ['--input', '--help'])
            for opt_name, opt_value in opts:
                if opt_name in ('-i', '--input'):
                    input_file = opt_value
                    sortFile(input_file)
            print("main end")
        except getopt.GetoptError:
            print("")
    else:
        print("use -i or --input to inject data.json file")