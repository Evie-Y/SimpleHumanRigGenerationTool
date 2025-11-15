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
        self._add_color_layout()
        # IK/FK layout
        # Unique Controls Layout
        self.setLayout(self.main_layout)
        pass
    
    def _mk_basic_rig_text_labels(self):
        # Text: 'Make sure joints have the '_JNT' suffix'
        self.suff_lbl = QtWidgets.QLabel('Make sure joints '
            'have the "_JNT" suffix')
        self.suff_lbl.setAlignment(Qt.AlignCenter)
        self.suff_lbl.setStyleSheet('font: bold')
        # Text: 'Select Joints to be Rigged'
        self.sel_lbl = QtWidgets.QLabel('Select Joints to be Rigged:')
        self.sel_lbl.setAlignment(Qt.AlignCenter)
        self.sel_lbl.setStyleSheet('font: bold')
        self.main_layout.addWidget(self.suff_lbl)
        self.main_layout.addWidget(self.sel_lbl)

    def _mk_generate_rig_button(self):
        # Button: 'Generate' (the standard settings)
        self.rig_btn = QtWidgets.QPushButton('Generate')
        self.main_layout.addWidget(self.rig_btn)

    def _add_color_layout(self):
        self.color_layout = QtWidgets.QVBoxLayout()
        self._mk_con_color_check_box()
        self._mk_right_colors_combo_box()
        self.main_layout.addLayout(self.color_layout)
    
    def _mk_con_color_check_box(self):
        # Checkbox: 'Same color for IK' (if on, ik/fk same colors)
        self.enable_ik_color_cb = QtWidgets.QCheckBox('Same Color for IK')
        self.color_layout.addWidget(self.enable_ik_color_cb)

    def _mk_right_colors_combo_box(self):
        self.r_fk_cbx_layout = QtWidgets.QHBoxLayout()
        # QComboBox: 'Right FK/ Color: ' (LIST)
        self.r_fk_lbl = QtWidgets.QLabel('Right FK Color')
        self.r_fk_cbx = QtWidgets.QComboBox()
        self.r_fk_cbx.insertItem(1, 'Red')
        # QComboBox: 'Right IK/ Color: ' (LIST) (disabled if cb on)
        # QComboBox: 'Center / Color: ' (LIST)
        # QComboBox: 'Left FK/ Color: ' (LIST)
        # QComboBox: 'Left IK / Color: ' (LIST) (disabled if cb on)
        self.r_fk_cbx_layout.addWidget(self.r_fk_cbx)
        self.main_layout.addLayout(self.r_fk_cbx_layout)

    def _build_control_colors_list(self):
        # 32 colors
        self.con_colors = ['Black', 'Grey', 'Light Gray', 'Dark Red',
            'Dark Blue', 'Blue', 'Green', 'Dark Purple', 'Pink', 'Brown',
            'Dark Brown', 'Red-Brown', 'Red', 'Light Green', 'Turquoise',
            'White', 'Yellow', 'Light Blue', 'Mint', 'Peach', 'Orange', 
            'Pale Yellow', 'Mute Green', 'Dark Orange', 'Fern', 'Grass Green',
            'Blue Mint', 'Mute Blue', 'Purple', 'Light Pink']

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