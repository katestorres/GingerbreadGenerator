import pymel.core as pm
import maya.cmds as mc
import random

#check if window exists
window_name = 'Gingergen'
if mc.window(window_name, exists=True):
    mc.deleteUI(window_name)
    
#Generate house

def buildHouse(basec, doorc, chimc, username):
    #pm.system.importFile("C: /Users/ktorres/Documents/maya/projects/default/assets/Gingerbread_models/ChimneyPipe.mb")
    #Create Chimney
    if chimc == "No Preference":
        choicec = ["Cube", "Cylinder", "Pipe"]
        chimc = random.choice(choicec)
    #pm.system.importFile("C: /Users/ktorres/Downloads/Gingerbread/BaseCube.mb")
    if chimc == "Cube":
        pm.system.importFile("C: /Users/%s/Documents/maya/projects/default/assets/Gingerbread/ChimneyCube.mb" % username)
    elif chimc == "Cylinder":
        pm.system.importFile("C: /Users/%s/Documents/maya/projects/default/assets/Gingerbread/ChimneyCylinder.mb" % username)
    elif chimc == "Pipe":
        pm.system.importFile("C: /Users/%s/Documents/maya/projects/default/assets/Gingerbread/ChimneyPipe.mb" % username)
    #Create door
    if doorc == "No Preference":
        choiced =["Rectangle", "Arc", "Circle"]
        doorc = random.choice(choiced)
    if doorc == "Rectangle":
        pm.system.importFile("C: /Users/%s/Documents/maya/projects/default/assets/Gingerbread/DoorSquare.mb" % username)
    elif doorc == "Arc":
        pm.system.importFile("C: /Users/%s/Documents/maya/projects/default/assets/Gingerbread/DoorArc.mb" % username)
    elif doorc == "Circle":
        pm.system.importFile("C: /Users/%s/Documents/maya/projects/default/assets/Gingerbread/DoorHobbit.mb" % username)

    #Create base
    if basec == "No Preference":
        choiceb = ["Cube", "Semi Sphere", "Cylinder"]
        basec = random.choice(choiceb)
    if basec == "Cube":
        pm.system.importFile("C: /Users/%s/Documents/maya/projects/default/assets/Gingerbread/BaseCube.mb" % username)
    elif basec == "Semi Sphere":
        pm.system.importFile("C: /Users/%s/Documents/maya/projects/default/assets/Gingerbread/BaseIgloo.mb" % username)
    elif basec == "Cylinder":
        pm.system.importFile("C: /User/%s/Documents/maya/projects/default/assets/Gingerbread/BaseCylinder.mb" % username)

  
#Retrieve answers and pass to buildHouse
def collectAns(*args):
    baseC = mc.optionMenuGrp('basep', query=True, value=True)
    doorC = mc.optionMenuGrp('doorp', query=True, value=True)
    chimC = mc.optionMenuGrp('chimp', query=True, value=True)
    userN = mc.textFieldGrp(userName, query=True, text=True)
    buildHouse(baseC, doorC, chimC, userName)
        
#create window
win = pm.window(window_name, title='Gingerbread House Generator')
winlay = pm.columnLayout()
titleText = pm.text(label='Welcome to the Gingerbread House Generator!')

#Get user name
userPrompt = pm.text(label='Please enter your user name')
userName = mc.textFieldGrp()

#Choose base type
baseChoice = mc.optionMenuGrp('basep', label='Base Preference')
mc.menuItem(label='No Preference')
mc.menuItem(label='Cube')
mc.menuItem(label='Cylinder')
mc.menuItem(label='Semi Sphere')


#Choose door type
doorChoice = mc.optionMenuGrp('doorp', label='Door Preference')
mc.menuItem(label='No Preference')
mc.menuItem(label='Rectangle')
mc.menuItem(label='Arc')
mc.menuItem(label='Circle')

#Choose chimney type
chmChoice = mc.optionMenuGrp('chimp', label='Chimney Preference')
mc.menuItem(label='No Preference')
mc.menuItem(label='Cube')
mc.menuItem(label='Cylinder')
mc.menuItem(label='Pipe')


#Accept
button = pm.button(label='Generate', command=collectAns)
win.show()

