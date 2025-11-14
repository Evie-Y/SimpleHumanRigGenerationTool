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
    
    # UI 
    # Text: 'Make sure joints have the '_JNT' suffix'
    # Text: 'Select Joints to be Rigged'
    # Button: 'Generate' (the standard settings and generates the whole human rig)

    # QComboBox: 'Right FK/ Color: ' (LIST)
    # Checkbox: 'Same color for IK: ' (if on, ik/fk same colors)
    # QComboBox: 'Right IK/ Color: ' (LIST) (disabled if cb on)
    # QComboBox: 'Center / Color: ' (LIST)
    # QComboBox: 'Left FK/ Color: ' (LIST)
    # QComboBox: 'Left IK / Color: ' (LIST) (disabled if cb on)

    # Checkbox: 'Unique Shapes ON: ' (if off, controls are circle crv)
    # SpinBox: 'Control Size: ' (Min=.1, Max=100)
    # Buttons: 'FK', 'IK', 'IK/FK' (creates ik/fk)

    # QComboBox: 'Unique Controls: ' (LIST)
    # Button: 'Create' (To create unique curves, not rigged.)
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