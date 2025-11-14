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
        self._mk_win_layout()

    def cancel(self):
        self.close()

    @QtCore.Slot()
    def build(self):
        self.rigGen.build()

    def _mk_win_layout(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        # Text layout
        self._mk_basic_rig_text_labels()
        self._mk_generate_rig_button()
        # Color layout
        # IK/FK layout
        # Unique Controls Layout
        self.setLayout(self.main_layout)
        pass
    
    def _mk_basic_rig_text_labels(self):
        self.suff_lbl = QtWidgets.QLabel('Make sure joints '
            'have the "_JNT" suffix')
        self.suff_lbl.setAlignment(Qt.AlignCenter)
        self.suff_lbl.setStyleSheet('font: bold')
        # Text: 'Make sure joints have the '_JNT' suffix'
        self.sel_lbl = QtWidgets.QLabel('Select Joints to be Rigged:')
        self.sel_lbl.setAlignment(Qt.AlignCenter)
        self.sel_lbl.setStyleSheet('font: bold')
        # Text: 'Select Joints to be Rigged'
        self.main_layout.addWidget(self.suff_lbl)
        self.main_layout.addWidget(self.sel_lbl)

    def _mk_generate_rig_button(self):
        # Button: 'Generate' (the standard settings)
        self.rig_btn = QtWidgets.QPushButton('Generate')
        self.main_layout.addWidget(self.rig_btn)
        pass

    def _mk_con_colors_layout(self):
        # Checkbox: 'Same color for IK: ' (if on, ik/fk same colors)
        # QComboBox: 'Right FK/ Color: ' (LIST)
        # QComboBox: 'Right IK/ Color: ' (LIST) (disabled if cb on)
        # QComboBox: 'Center / Color: ' (LIST)
        # QComboBox: 'Left FK/ Color: ' (LIST)
        # QComboBox: 'Left IK / Color: ' (LIST) (disabled if cb on)
        pass

    def _mk_ik_fk_layout(self):
        # Checkbox: 'Unique Shapes ON: ' (if off, controls are circle crv)
        # SpinBox: 'Control Size: ' (Min=.1, Max=100)
        # Buttons: 'FK', 'IK', 'IK/FK' (creates ik/fk)
        pass

    def _mk_seperate_unique_controls_layout(self):
        # QComboBox: 'Unique Controls: ' (LIST)
        # Button: 'Create' (To create unique curves, not rigged.)
        pass

class RigGen():
    def __init__(self):
        # Make unique controls
        # Make IK rig functional
        # Make FK rig functional
        # Make IK/FK switch functional
        # Make a spline rig functional
        # Make controls change color based on L/R naming
        # Make controls change boldness based on the control's function
        pass

    def build(self):
        pass