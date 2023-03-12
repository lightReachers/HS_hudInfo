
import os
import sys
sys.path.append("/opt/homebrew/lib/python3.11/site-packages/cv2")
import cv2
import uuid
import numpy as np
import hou
from . import constant


class getData:
    def __init__(self, hudCamera=None, objectNode=None, solverNode=None):
        # Initialize instance variables
        self.solver_type = None
        self.solver_set = False
        if objectNode: self.object_node = objectNode 
        if solverNode: self.solver_node = solverNode
        if solverNode: self.solver_type = solverNode.type().nameComponents()[2]

        # Check if the solver is supported and set the solver_set flag accordingly
        if self.solver_type in constant.SUPPORTED_SOLVERS:
            self.solver_set = True

        if hudCamera:
            self.camera = hudCamera  
        self.set_parm_attr()      

    def get_parm_type(self, parm):
        return parm.parmTemplate().type()

    def trim_number(self, number):
        result = number
        if type(number) is float:
            result =  "%.3f" % number
        if  type(number) is list or type(number) is tuple:
            result = ["%.3f" % i for i in number]
        return result    
            

    def set_parm_attr(self):
        if self.solver_type == 'pyrosolver_sparse':                   # Set attributes for Pyro solver type, very imp
            self.pyro_sim_parm = constant.PYRO_PARM_SIMULATION        # As  hudObject = hudinfo.getData(hudCamera=hudCamera, objectNode=objNode, solverNode=solverNode)
            self.pyro_flame_parm = constant.PYRO_PARM_FLAMES          # data = hudObject.get_parm_value(hudObject.pyro_sim_parm)
            self.pyro_shape_parm = constant.PYRO_PARM_SHAPE
            self.pyro_color_parm = constant.PYRO_PARM_COLOR
            self.pyro_advance_parm = constant.PYRO_PARM_ADVANCED

    def eval_parm(self, parm):
        """
        This function return evaluated dict 
        :param parm: hou.Parm
        :return: dict
        """

        result = dict()
        ui_name = parm.description()
        result["ui_name"] = ui_name

        raw_value = parm.eval()
        result["raw_value"] = raw_value

        parm_type = self.get_parm_type(parm)
        result["parm_type"] = parm_type
        result["value"] = raw_value
        # If the parameter type is a ramp, format the value list as [time, value]
        if parm.parmTemplate().interfaceType() == 'ramp_float':
            value = [[self.trim_number(list(raw_value.keys())[i]), self.trim_number(list(raw_value.values())[i])] for i in range(len(list(raw_value.keys())))] 
        elif parm.parmTemplate().interfaceType() == 'direction':
            value = [self.trim_number(list(raw_value)[i]) for i in range(len(raw_value))]
        elif parm.parmTemplate().interfaceType() == 'float':    
            value = self.trim_number(raw_value)
        elif parm.parmTemplate().interfaceType() == 'ordered_menu':
            value = parm.evalAsString()
        else:
            value = parm.eval()

        result["value"] = value   

        result["is_default"] = parm.isAtDefault()
        result["is_animated"] = parm.isTimeDependent()


        return result

    def get_parm_value(self, parms=list()):
        result = dict()
        self.set_parm_attr() 
        target_nodes = [self.object_node, self.solver_node]
        all_parms_path = list()
        all_parms_path = [ os.path.join(target_nodes[i].path(), parms[j])  for i in range(len(target_nodes)) for j in range(len(parms))]
        for parm_path in all_parms_path:
            parm = hou.parm(parm_path)
            if parm:
                parm_result = self.eval_parm(parm)
                if not parm_result["is_default"]:
                    value = parm_result["value"] 
                    #print(f"{ parm.description() } : {value}")
                    result[parm.description()] = value     
            else:
                parm = hou.parmTuple(parm_path)
                if parm:
                    parm_result = self.eval_parm(parm)
                    if not parm_result["is_default"]:
                        value = parm_result["value"] 
                        #print(f"{ parm.description() } : {value}")
                        result[parm.description()] = value 
        #print(result.items())                    
        return result

    def get_temp_path(self):
        houdini_temp_root = hou.getenv("HOUDINI_TEMP_DIR")
        hip_name = hou.getenv("HIPNAME") 
        node_name = hou.node(".").name()
        if  hou.hipFile.isNewFile():
            hip_name = "new_file"
        temp_path = os.path.join(houdini_temp_root, hip_name, node_name)
        return temp_path








