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



import sys
sys.path.append("C:/ProgramData/miniconda3/Lib/site-packages/cv2")

import os
import hou
import cv2
import numpy as np 

import uuid
id = "Unique ID is {}".format(uuid.uuid1())
#print(id)
parm = hou.node('/obj/geo1/transform1').evalParm("tx")
text = "Solver Div : " + str(parm)
image = np.zeros((858,2048,4),np.uint8)
cv2.putText(image, text, (10,100),cv2.FONT_HERSHEY_SIMPLEX,.7,(0,0,255,255))
imgpath = 'D:/test/image2.' + str(int(hou.frame())).zfill(4) + '.png' 

if os.path.exists(imgpath):
    os.remove(imgpath)
    #print(imgpath)
cv2.imwrite(imgpath,image)


