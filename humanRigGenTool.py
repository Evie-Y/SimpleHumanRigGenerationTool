from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Qt
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance

import maya.cmds as cmds

# Boilerplate code, just copy and keep handy somewhere.
# import riggen
# import importlib
# importlib.reload(riggen)

# win = riggen.RigGenWin()
# win.show()

def get_maya_main_win():
    main_win = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_win), QtWidgets.QWidget)

class RigGenWin(QtWidgets.QDialog):
    def __init__(self):
        # runs the init code of the parent QDialog class
        super().__init__(parent=get_maya_main_win())
        self.rigGen = RigGen()
        self.setWindowTitle("Simple Humanoid Rig Generator")
        self.resize(250, 500)

    #Checkbox for fk, ik, or both with a switch.
    #Button for standard humanoid rig generation.
    #Buttons to create unique curves, not rigged.
    pass

class RigGen():
    # Make unique controls
    # Make IK rig functional
    # Make FK rig functional
    # Make IK/FK switch functional
    # Make a spline rig functional
    # Make controls change color based on L/R naming
    # Make controls change boldness based on the control's function
    pass