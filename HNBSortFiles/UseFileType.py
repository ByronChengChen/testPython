import filetype
import os
import sys
from enum import Enum

class HnbFileType(Enum):
    HnbV = 1
    HnbP = 2
    HnbUnknow = 3
    
def getFileType(fileFullPath):
    kind = filetype.guess(fileFullPath)
    if kind is None:
        print("srcFile:" + __file__ + ",line:" + str(sys._getframe().f_lineno) + "\n" + fileFullPath + " unknow")
    else:
        mimeType = kind.mime
        if "video" in mimeType:
            return HnbFileType.HnbV
        elif "image" in mimeType:
            return HnbFileType.HnbP
        else:
            return HnbFileType.HnbUnknow
