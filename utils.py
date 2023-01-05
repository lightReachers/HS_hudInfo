import os
import sys
import uuid
import tempfile
import hou

def getOverlayDir():
    dirName = str(uuid.uuid1())
    if hou.hipFile.isNewFile():
        # get the temp dir path
        dirPath = '{}/{}'.format(tempfile.gettempdir(), dirName)
         
    else:
        # get the path to the Houdini hipfile folder
        hipfileFolder = hou.getenv('HIP')
        dirPath = '{}/{}'.format(hipfileFolder, dirName)
        # create the directory
    os.mkdir(dirPath)
    return str(dirPath)

