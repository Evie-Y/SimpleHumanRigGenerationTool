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
        self.resize(225, 250)
        self._mk_win_layout()
        self._connect_signals()
        # TODO: add connectors
        # TODO: cb functionality
        # TODO: extra- add seperators

    def _connect_signals(self):
        self.rig_btn.clicked.connect(self.generate)

    @QtCore.Slot()
    def generate(self):
        self.rigGen.build()

    def _mk_win_layout(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        # Text layout
        self._mk_basic_rig_text_labels()
        self._mk_generate_rig_button()
        # Color layout
        self._add_color_layout()
        # IK/FK layout
        self._add_ik_fk_layout()
        # Unique Controls Layout
        self._add_unique_controls_layout()
        self.setLayout(self.main_layout)
    
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
        self._mk_right_colors_labels()
        self._mk_right_colors_combo_box()
        self._mk_center_colors_label()
        self._mk_center_colors_combo_box()
        self._mk_left_colors_labels()
        self._mk_left_colors_combo_box()
        self.main_layout.addLayout(self.color_layout)

    def _mk_con_color_check_box(self):
        # Checkbox: 'Same color for IK' (if on, ik/fk same colors)
        self.enable_ik_color_cb = QtWidgets.QCheckBox('Same Color for IK')
        self.main_layout.addWidget(self.enable_ik_color_cb)

    def _mk_right_colors_labels(self):
        self.r_lbl_layout = QtWidgets.QHBoxLayout()
        self.r_fk_lbl = QtWidgets.QLabel('Right FK Color')
        self.r_ik_lbl = QtWidgets.QLabel('Right IK Color')
        self.r_lbl_layout.addWidget(self.r_fk_lbl)
        self.r_lbl_layout.addWidget(self.r_ik_lbl)
        self.main_layout.addLayout(self.r_lbl_layout)

    def _mk_right_colors_combo_box(self):
        self.r_cbx_layout = QtWidgets.QHBoxLayout()
        # QComboBox: 'Right FK/ Color: ' (LIST)
        self.r_fk_cbx = QtWidgets.QComboBox()
        self._build_control_colors_list(self.r_fk_cbx)
        # placeholder text: 'pink'
        self.r_fk_cbx.setCurrentIndex(29)
        # QComboBox: 'Right IK/ Color: ' (LIST) (disabled if cb on)
        self.r_ik_cbx = QtWidgets.QComboBox()
        self._build_control_colors_list(self.r_ik_cbx)
        # placeholder text: 'red'
        self.r_ik_cbx.setCurrentIndex(12)
        self.r_cbx_layout.addWidget(self.r_fk_cbx)
        self.r_cbx_layout.addWidget(self.r_ik_cbx)
        self.main_layout.addLayout(self.r_cbx_layout)

    def _mk_center_colors_label(self):
        self.c_lbl_layout = QtWidgets.QHBoxLayout()
        # QComboBox: 'Center / Color: ' (LIST)
        self.c_lbl = QtWidgets.QLabel('Center Control Color')
        self.c_lbl_layout.addWidget(self.c_lbl)
        self.main_layout.addLayout(self.c_lbl_layout)

    def _mk_center_colors_combo_box(self):
        self.c_cbx_layout = QtWidgets.QHBoxLayout()
        # QComboBox: 'Center / Color: ' (LIST)
        self.c_cbx = QtWidgets.QComboBox()
        self._build_control_colors_list(self.c_cbx)
        # placeholder text: 'yellow'
        self.c_cbx.setCurrentIndex(16)
        self.c_cbx_layout.addWidget(self.c_cbx)
        self.main_layout.addLayout(self.c_cbx_layout)

    def _mk_left_colors_labels(self):
        self.l_lbl_layout = QtWidgets.QHBoxLayout()
        self.l_fk_lbl = QtWidgets.QLabel('Left FK Color')
        self.l_ik_lbl = QtWidgets.QLabel('Left IK Color')
        self.l_lbl_layout.addWidget(self.l_fk_lbl)
        self.l_lbl_layout.addWidget(self.l_ik_lbl)
        self.main_layout.addLayout(self.l_lbl_layout)

    def _mk_left_colors_combo_box(self):
        self.l_cbx_layout = QtWidgets.QHBoxLayout()
        # QComboBox: 'Right FK/ Color: ' (LIST)
        self.l_fk_cbx = QtWidgets.QComboBox()
        self._build_control_colors_list(self.l_fk_cbx)
        # placeholder text: 'light blue'
        self.l_fk_cbx.setCurrentIndex(17)
        # QComboBox: 'Right IK/ Color: ' (LIST) (disabled if cb on)
        self.l_ik_cbx = QtWidgets.QComboBox()
        self._build_control_colors_list(self.l_ik_cbx)
        # placeholder text: 'blue'
        self.l_ik_cbx.setCurrentIndex(5)
        self.l_cbx_layout.addWidget(self.l_fk_cbx)
        self.l_cbx_layout.addWidget(self.l_ik_cbx)
        self.main_layout.addLayout(self.l_cbx_layout)

    def _build_control_colors_list(self, cbx):
        # 31 colors
        self.con_colors = ['Black', 'Grey', 'Light Gray', 'Dark Red',
            'Dark Blue', 'Blue', 'Green', 'Dark Purple', 'Pink', 'Brown',
            'Dark Brown', 'Red-Brown', 'Red', 'Light Green', 'Turquoise',
            'White', 'Yellow', 'Light Blue', 'Mint', 'Peach', 'Orange', 
            'Pale Yellow', 'Mute Green', 'Dark Orange', 'Fern', 'Grass Green',
            'Blue Mint', 'Mute Blue', 'Purple', 'Light Pink']
        for color in self.con_colors:
            cbx.addItem(color)
        
    def _add_ik_fk_layout(self):
        self.ik_fk_layout = QtWidgets.QVBoxLayout()
        self._mk_ik_fk_check_box()
        self._mk_ik_fk_spin_box()
        self._mk_ik_fk_buttons()
        self.main_layout.addLayout(self.ik_fk_layout)

    def _mk_ik_fk_check_box(self):
        # Checkbox: 'Unique Shapes ON: ' (if off, controls are circle crv)
        self.enable_shapes_cb = QtWidgets.QCheckBox('Unique Shapes ON')
        self.main_layout.addWidget(self.enable_shapes_cb)

    def _mk_ik_fk_spin_box(self):
        self.size_layout = QtWidgets.QHBoxLayout()
        self.size_lbl = QtWidgets.QLabel('Control Size: ')
        # SpinBox: 'Control Size: ' (Min=.1, Max=100)
        self.size_dsnbx = QtWidgets.QDoubleSpinBox()
        self.size_dsnbx.setValue(1)
        self.size_dsnbx.setMaximum(100)
        self.size_dsnbx.setMinimum(.1)
        self.size_layout.addWidget(self.size_lbl)
        self.size_layout.addWidget(self.size_dsnbx)
        self.main_layout.addLayout(self.size_layout)

    def _mk_ik_fk_buttons(self):
        self.buttons_layout = QtWidgets.QHBoxLayout()
        # Buttons: 'FK', 'IK', 'IK/FK' (creates ik/fk)
        self.fk_btn = QtWidgets.QPushButton('FK')
        self.ik_btn = QtWidgets.QPushButton('IK')
        self.ik_fk_btn = QtWidgets.QPushButton('IK/FK')
        self.buttons_layout.addWidget(self.fk_btn)
        self.buttons_layout.addWidget(self.ik_btn)
        self.buttons_layout.addWidget(self.ik_fk_btn)
        self.main_layout.addLayout(self.buttons_layout)

    def _add_unique_controls_layout(self):
        self.unique_controls_layout = QtWidgets.QVBoxLayout()
        self._mk_unique_controls_labels()
        self._mk_unique_controls_combo_box()
        self._mk_unique_controls_button()
        self.main_layout.addLayout(self.unique_controls_layout)

    def _mk_unique_controls_labels(self):
        self.ctrls_layout = QtWidgets.QHBoxLayout()
        self.ctrls_lbl = QtWidgets.QLabel('Create: ')
        self.ctrls_lbl.setAlignment(Qt.AlignRight)
        self.ctrls_layout.addWidget(self.ctrls_lbl)

    def _mk_unique_controls_combo_box(self):
        # QComboBox: 'Unique Controls: ' (LIST)
        self.ctrls_cbx = QtWidgets.QComboBox()
        self._build_unique_controls_list(self.ctrls_cbx)
        self.ctrls_layout.addWidget(self.ctrls_cbx)
        self.main_layout.addLayout(self.ctrls_layout)

    def _build_unique_controls_list(self, cbx):
        # 32 colors
        self.con_shapes = ['Sqaure', 'Rectangle', 'Triangle', 'Diamond',
            'Arrow', 'Flexible Arrow', 'Left, Up, Right Arrow', 'Quad Arrow',
            'Sphere']
        for shape in self.con_shapes:
            cbx.addItem(shape)

    def _mk_unique_controls_button(self):
        # Button: 'Create' (To create unique curves, not rigged.)
        self.con_btn = QtWidgets.QPushButton('Create')
        self.main_layout.addWidget(self.con_btn)

class RigGen():
    def __init__(self):
        # figure out how to link colors lsit to numbers
        self.same_color = False
        self.right_fk_color = 0
        self.right_ik_color = 1
        self.center_con_color = 6
        self.left_fk_color = 29
        self.left_ik_color = 27
        self.unique_shapes = True
        self.con_size = 1
        self.create_control_shape = 0
        pass

    def mk_ctrl_shapes(self):
        # Make unique controls
            # either make w/ python or import based on complexity
                # square
                # rectangle
                # triangle
                # diamond
                # arrow (variants)
                # sphere?
        pass

    def mk_ctrl_square(self, name='bob'):
        cmds.file('Square.ma', i=True)
        cmds.select('square', replace=True, hierarchy=True)
        con = cmds.rename(f'{name}')
        return con
    
    def mk_ctrl_rectangle(self, name='bob'):
        cmds.file('Rectangle.ma', i=True)
        cmds.select('rectangle', replace=True, hierarchy=True)
        con = cmds.rename(f'{name}')
        return con
    
    def mk_ctrl_triangle(self, name='bob'):
        cmds.file('Triangle.ma', i=True)
        cmds.select('triangle', replace=True, hierarchy=True)
        con = cmds.rename(f'{name}')
        return con
    
    def mk_ctr_semi_circle(self, name='bob'):
        cmds.file('SemiCircle.ma', i=True)
        cmds.select('semiCircle', replace=True, hierarchy=True)
        con = cmds.rename(f'{name}')
        return con
    
    def mk_ctrl_sphere(self, name='bob'):
        cmds.file('Sphere.ma', i=True)
        cmds.select('sphere', replace=True, hierarchy=True)
        con = cmds.rename(f'{name}')
        return con
    
    def mk_ctrl_diamond(self, name='bob'):
        cmds.file('Diamond.ma', i=True)
        cmds.select('diamond', replace=True, hierarchy=True)
        con = cmds.rename(f'{name}')
        return con
    
    def mk_ctrl_arrow(self, name='bob'):
        cmds.file('ZpointingArrow.ma', i=True)
        cmds.select('ZpointingArrow', replace=True, hierarchy=True)
        con = cmds.rename(f'{name}')
        return con
    
    def mk_ctrl_flexible_arrow(self, name='bob'):
        cmds.file('ZpointingFlexibleArrow.ma', i=True)
        cmds.select('ZpointingFlexibleArrow', replace=True, hierarchy=True)
        con = cmds.rename(f'{name}')
        return con
    
    def mk_ctrl_quad_arrow(self, name='bob'):
        cmds.file('QuadArrow.ma', i=True)
        cmds.select('quadArrow', replace=True, hierarchy=True)
        con = cmds.rename(f'{name}')
        return con

    def mk_ik_rig(self):
        # Make IK rig functional
        pass

    def mk_fk_rig(self):
        # Make FK rig functional
        self.con_list = []
        self.grp_list = []
        # rig_grp = cmds.group(n='rig_GRP')
        # con_grp.append(rig_grp)
        for jnt in cmds.ls(sl=True):
            con, shape = cmds.circle(n=jnt.replace('_JNT', '_CON'))
            grp = cmds.group(con, n=jnt.replace('_JNT', "_GRP"))
            cmds.delete(cmds.parentConstraint(jnt, grp))
            cmds.parentConstraint(con, jnt)
            # TODO: group groups to con
            # cmds.parent(grp, con_grp[-1])
            self.con_list.append(con)
            self.grp_list.append(grp)
        self.mk_group_parent_structure()

    def mk_group_parent_structure(self):
        grp_seq = 1
        con_seq = 0
        for con in self.con_list:
            cmds.parent(self.grp_list[grp_seq], self.con_list[con_seq])
            con_seq += 1
            grp_seq += 1

    def mk_ikfk_switch(self):
        # Make IK/FK switch functional
        pass

    def mk_spline_rig(self):
        # Make a spline rig functional
        pass

    def edit_ctrl_color(self):
        # Make controls change color based on L/R naming
        pass

    def edit_ctrl_bold(self):
        # Make controls change boldness based on the control's function
        pass

    def generate(self):
        # select joints
        # if joints dont have "JNT" suffix; 'select joints w suff'
        # if pressed 'generate'
        # generate loop (only for neck down)
        # for joint in ls:
        # mk_fkik
        # add corresponding shape&color
        # bold if ikfk switch
        # mk spline to 'spine' joints
        pass

    def create(self):
        # select joints
        # if joints dont have "JNT" suffix; 'select joints w suff'
        # if pressed 'create
        # create loop (only for neck down)
        # for joint in ls:
        # mk_fkik
        # add picked shape&color
        # bold if ikfk switch
        # mk spline to 'spine' joints
        pass
        
    def build(self):
        self.mk_fk_rig()
        self.mk_ctr_semi_circle(name='funny')
        self.mk_ctrl_flexible_arrow()
        pass