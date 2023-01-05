import os
import sys
import uuid
import tempfile
import hou

def getOverlayDir():
    if hou.hipFile().isNewFile():
        # get the temp dir path
        return tempfile.gettempdir()
    else:
        # get the path to the Houdini hipfile folder
        hipfileFolder = hou.getenv('HIP')
        # generate a new UUID and use it as the name of a directory in the Houdini hipfile folder
        dirName = str(uuid.uuid4())
        dirPath = Path(hipfileFolder) / dirName
        # create the directory
        dirPath.mkdir(exist_ok=True)
        return str(dirPath)


