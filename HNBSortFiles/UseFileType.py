import filetype
from enum import Enum

class HnbFileType(Enum):
    HnbV = 1
    HnbP = 2
    HnbUnknow = 3
    
def getFileType(fileFullPath):
    kind = filetype.guess(fileFullPath)
    if kind is None:
        print(fileFullPath + " unknow")
    else:
        mimeType = kind.mime
        if "video" in mimeType:
            return HnbFileType.HnbV
        elif "jpeg" in mimeType:
            return HnbFileType.HnbP
        else:
            return HnbFileType.HnbUnknow
