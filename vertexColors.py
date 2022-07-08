import maya.cmds as cmds
import random

def selector(percents):
    RandomSelection = []
    mySel = cmds.ls(sl=1)
    random.shuffle(mySel)
    
    start = 0
    cumul = 0
    for cur in percents:
        cumul += cur
        end = cumul * len(mySel) // 100
        RandomSelection.append(mySel[start:end])
        start = end
    
    cmds.polyColorPerVertex(RandomSelection[0],rgb=(1, 0, 0), cdo=1 )
    cmds.polyColorPerVertex(RandomSelection[1],rgb=(0, 1, 0), cdo=1 )
    cmds.polyColorPerVertex(RandomSelection[2],rgb=(0, 0, 1), cdo=1 )
    cmds.polyColorPerVertex(RandomSelection[3],rgb=(1, 0.6, 0), cdo=1 )
    

selector([60, 20, 10, 10])
