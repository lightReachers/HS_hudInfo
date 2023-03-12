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


#-------------------------python sop test code ------------------
import os
frame = $F

import sys
sys.path.append("/opt/homebrew/lib/python3.11/site-packages/cv2")
import cv2
import uuid
import numpy as np
import os
import hudinfo
import hou
node = hou.node("../../")
print(node.path())
import importlib
importlib.reload(hudinfo)

print(node.evalParm("hudCamera"))
objNode = hou.node(node.evalParm("solverObject"))
solverNode = hou.node(node.evalParm("solverNode"))
hudCamera = node.parm("hudCamera").evalAsNode()
print(hudCamera)
hudObject = hudinfo.getData(hudCamera=hudCamera, objectNode=objNode, solverNode=solverNode)

    


print("start")
data = (hudObject.get_parm_value(hudObject.pyro_sim_parm))
#print(data)

print(frame)
print(hou.pwd())

#hou.pwd().cook(force=True)
import uuid
id = "Unique ID is {}".format(uuid.uuid4())
#print(id)
start_x = 10
start_y = 100
image = np.zeros((858,2048,4),np.uint8)

imgroot = hudObject.get_temp_path()
if not os.path.exists(imgroot):
    os.makedirs(imgroot)
random_name = str(uuid.uuid4())
imagepath = os.path.join(imgroot, random_name) + '.png' 
print(imagepath)
for i in data.items():
    text = f'{i[0]} : {i[1]}'
    cv2.putText(image, text, (start_x,start_y),cv2.FONT_HERSHEY_SIMPLEX,.7,(0,0,255,255))
    start_y = start_y +22
#for file in os.listdir(imgroot):
#    os.remove(os.path.join(imgroot,file))
    
cv2.imwrite(imagepath,image)
if os.path.exists(imagepath):
    hudCamera.parm("fgimage").set(imagepath)

print("end")







