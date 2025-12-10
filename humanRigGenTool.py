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
        self.resize(50, 50)
        self._mk_win_layout()
        self.connect_signals()
        # TODO: add connectors
        # TODO: cb functionality
        # TODO: extra- add seperators

    def connect_signals(self):
        self.fk_btn.clicked.connect(self.fk_generate)
        self.ik_btn.clicked.connect(self.ik_generate)
        self.con_btn.clicked.connect(self.control_generate)

    @QtCore.Slot()
    def fk_generate(self):
        self._update_properties()
        self.rigGen.create_fk()

    @QtCore.Slot()
    def ik_generate(self):
        self._update_properties()
        self.rigGen.create_ik()

    @QtCore.Slot()
    def control_generate(self):
        self._update_properties()
        self.rigGen.generate_single_control()
    
    def _update_properties(self):
        self.rigGen.__init__()
        self.rigGen.current_control_shape = str(self.ctrls_cbx.currentText())
        self.rigGen.unique_shapes = self.enable_shapes_cb.isChecked()
        self.rigGen.con_size = self.size_dsnbx.value()

    def _mk_win_layout(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        # Text layout
        self._mk_basic_rig_text_labels()
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
        
    def _add_ik_fk_layout(self):
        self.ik_fk_layout = QtWidgets.QVBoxLayout()
        self._mk_ik_fk_check_box()
        self._mk_ik_fk_spin_box()
        self._mk_ik_fk_buttons()
        self.main_layout.addLayout(self.ik_fk_layout)

    def _mk_ik_fk_check_box(self):
        self.adjustments_layout = QtWidgets.QHBoxLayout()
        # Checkbox: 'Unique Shapes ON: ' (if off, controls are circle crv)
        self.enable_shapes_cb = QtWidgets.QCheckBox('Unique Shapes ON')
        self.adjustments_layout.addWidget(self.enable_shapes_cb)

    def _mk_ik_fk_spin_box(self):
        self.size_lbl = QtWidgets.QLabel('Control Size: ')
        # SpinBox: 'Control Size: ' (Min=.1, Max=100)
        self.size_dsnbx = QtWidgets.QDoubleSpinBox()
        self.size_dsnbx.setValue(1)
        self.size_dsnbx.setMaximum(100)
        self.size_dsnbx.setMinimum(.1)
        self.adjustments_layout.addWidget(self.size_lbl)
        self.adjustments_layout.addWidget(self.size_dsnbx)
        self.main_layout.addLayout(self.adjustments_layout)

    def _mk_ik_fk_buttons(self):
        self.buttons_layout = QtWidgets.QHBoxLayout()
        # Buttons: 'FK', 'IK', 'IK/FK' (creates ik/fk)
        self.fk_btn = QtWidgets.QPushButton('FK')
        self.ik_btn = QtWidgets.QPushButton('IK')
        self.buttons_layout.addWidget(self.fk_btn)
        self.buttons_layout.addWidget(self.ik_btn)
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

    def _build_unique_controls_list(self, cbx):
        # 32 colors
        self.ui_con_shapes_list =['Square', 'Rectangle', 'Triangle', 'Diamond',
            'Arrow', 'Flexible Arrow', 'Quad Arrow', 'Sphere', 'SemiCircle']
        for shape in self.ui_con_shapes_list:
            cbx.addItem(shape)

    def _mk_unique_controls_button(self):
        # Button: 'Create' (To create unique curves, not rigged.)
        self.con_btn = QtWidgets.QPushButton('Create')
        self.ctrls_layout.addWidget(self.con_btn)
        self.main_layout.addLayout(self.ctrls_layout)

class RigGen():
    def __init__(self):
        # figure out how to link colors lsit to numbers
        self.color = 0
        self.unique_shapes = True
        self.con_size = 1
        self.current_control_shape = "Square"
        pass

    def mk_ctrl_square(self, name='square_control'):
        cmds.file('Square.ma', i=True)
        cmds.select('square', replace=True, hierarchy=True)
        cmds.rename(f'{name}')
        con = cmds.ls(selection=True)
        cmds.scale(self.con_size, self.con_size, self.con_size)
        return con
    
    def mk_ctrl_rectangle(self, name='rectangle_control'):
        cmds.file('Rectangle.ma', i=True)
        cmds.select('rectangle', replace=True, hierarchy=True)
        cmds.rename(f'{name}')
        con = cmds.ls(selection=True)
        cmds.scale(self.con_size, self.con_size, self.con_size)
        return con
    
    def mk_ctrl_triangle(self, name='triangle_control'):
        cmds.file('Triangle.ma', i=True)
        cmds.select('triangle', replace=True, hierarchy=True)
        cmds.rename(f'{name}')
        con = cmds.ls(selection=True)
        cmds.scale(self.con_size, self.con_size, self.con_size)
        return con
    
    def mk_ctrl_semi_circle(self, name='semi_circle_control'):
        cmds.file('SemiCircle.ma', i=True)
        cmds.select('semiCircle', replace=True, hierarchy=True)
        cmds.rename(f'{name}')
        con = cmds.ls(selection=True)
        cmds.scale(self.con_size, self.con_size, self.con_size)
        return con
    
    def mk_ctrl_sphere(self, name='sphere_control'):
        cmds.file('Sphere.ma', i=True)
        cmds.select('sphere', replace=True, hierarchy=True)
        cmds.rename(f'{name}')
        con = cmds.ls(selection=True)
        cmds.scale(self.con_size, self.con_size, self.con_size)
        return con
    
    def mk_ctrl_diamond(self, name='diamond_control'):
        cmds.file('Diamond.ma', i=True)
        cmds.select('diamond', replace=True, hierarchy=True)
        cmds.rename(f'{name}')
        con = cmds.ls(selection=True)
        cmds.scale(self.con_size, self.con_size, self.con_size)
        return con
    
    def mk_ctrl_arrow(self, name='arrow_control'):
        cmds.file('ZpointingArrow.ma', i=True)
        cmds.select('ZpointingArrow', replace=True, hierarchy=True)
        cmds.rename(f'{name}')
        con = cmds.ls(selection=True)
        cmds.scale(self.con_size, self.con_size, self.con_size)
        return con
    
    def mk_ctrl_flexible_arrow(self, name='flexible_arrow_control'):
        cmds.file('ZpointingFlexibleArrow.ma', i=True)
        cmds.select('ZpointingFlexibleArrow', replace=True, hierarchy=True)
        cmds.rename(f'{name}')
        con = cmds.ls(selection=True)
        cmds.scale(self.con_size, self.con_size, self.con_size)
        return con
    
    def mk_ctrl_quad_arrow(self, name='quad_arrow_control'):
        cmds.file('QuadArrow.ma', i=True)
        cmds.select('quadArrow', replace=True, hierarchy=True)
        cmds.rename(f'{name}')
        con = cmds.ls(selection=True)
        cmds.scale(self.con_size, self.con_size, self.con_size)
        return con

    def mk_ik_rig(self):
        # Make IK rig functional
        selection = cmds.ls(selection=True)
        shoulder = selection[0]
        elbow = selection[1]
        wrist = selection[2]
        self.mk_idh_and_con(shoulder, wrist)
        self.mk_pv(shoulder, elbow, wrist)
        self.mk_pv_constraint()

    def mk_pv_constraint(self):
        cmds.select(self.pv_con[1], self.ikh[0], replace=True)
        cmds.PoleVectorConstraint(self.pv_con[1], self.ikh[0])
        cmds.delete(self.crv)

    def mk_pv(self, shoulder, elbow, wrist):
        # build curv
        # build pv
        shoulder_pos = cmds.xform(shoulder, q=1, ws=1, t=1)
        elbow_pos = cmds.xform(elbow, q=1, ws=1, t=1)
        wrist_pos = cmds.xform(wrist, q=1, ws=1, t=1)
        self.crv = cmds.curve(d=1, p=(shoulder_pos, elbow_pos, wrist_pos),
            k=(0, 1, 2), n=shoulder.replace('JNT', 'CRV'))
        cmds.moveVertexAlongDirection(self.crv + '.cv[1]', n=4)
        cv_pos = cmds.xform(self.crv + '.cv[1]', q=1, ws=1, t=1)
        self.pv_con = self.mk_ctrl_semi_circle(elbow.replace('JNT', 'PV_CON'))
        pv_grp = cmds.group(self.pv_con[1], n=wrist.replace('JNT', 'PV_GRP'))
        cmds.xform(pv_grp, ws=True, t=cv_pos)

    def mk_idh_and_con(self, shoulder, wrist):
        # build an IK handle + control
        name = wrist.replace('JNT', 'IKH')
        self.ikh = cmds.ikHandle(startJoint=shoulder, n=name, ee=wrist)
        con = self.mk_ctrl_diamond(wrist.replace('JNT', 'CON'))
        grp = cmds.group(con, n=wrist.replace('JNT', 'GRP'))
        pos = cmds.xform(wrist, ws=True, t=True, q=True)
        cmds.xform(grp, ws=True, t=pos)
        cmds.parent(self.ikh[0], con[1])
        cmds.setAttr(self.ikh[0] + '.v', 0)
        cmds.orientConstraint(con[1], wrist, maintainOffset=True)

    def mk_fk_rig_circle(self):
        # Make FK rig functional
        for jnt in cmds.ls(sl=True):
            con = cmds.circle(n=jnt.replace('JNT', '_ON'))
            grp = cmds.group(con, n=jnt.replace('JNT', "GRP"))
            cmds.delete(cmds.parentConstraint(jnt, grp))
            cmds.parentConstraint(con, jnt)
            self.con_list.append(con)
            self.grp_list.append(grp)
        self.mk_group_parent_structure()

    def mk_fk_rig_regular(self):
        # Make FK rig functional
        for jnt in cmds.ls(sl=True):
            con = self.mk_ctrl_sphere(jnt.replace('JNT', 'CON'))
            grp = cmds.group(con, n=jnt.replace('JNT', "GRP"))
            cmds.delete(cmds.parentConstraint(jnt, grp))
            cmds.parentConstraint(con, jnt)
            self.con_list.append(con)
            self.grp_list.append(grp)
        self.mk_group_parent_structure()

    def mk_group_parent_structure(self):
        self.grp_seq = 1
        self.con_seq = 0
        for con in self.con_list:
            cmds.parent(self.grp_list[self.grp_seq],
                        self.con_list[self.con_seq])
            self.con_seq += 1
            self.grp_seq += 1

    def create_shapes_list(self):
        self.con_shape_list = ['Square', 'Rectangle', 'Triangle', 'Diamond',
            'Arrow', 'Flexible Arrow', 'Quad Arrow', 'Sphere', 'SemiCircle']
        self.create_con_shape_list = [self.mk_ctrl_square,
            self.mk_ctrl_rectangle, self.mk_ctrl_triangle,
            self.mk_ctrl_diamond, self.mk_ctrl_arrow,
            self.mk_ctrl_flexible_arrow, self.mk_ctrl_quad_arrow,
            self.mk_ctrl_sphere, self.mk_ctrl_semi_circle]
        return self.con_shape_list, self.create_con_shape_list

    def link_shapes(self):
        str_list, funct_list = self.create_shapes_list()
        self.index = str_list.index(self.current_control_shape)
        funct_list[self.index]()

    def create_fk(self):
        self.con_list = []
        self.grp_list = []
        if self.unique_shapes == True:
            self.mk_fk_rig_regular()
        else:
            self.mk_fk_rig_circle()

    def create_ik(self):
        self.mk_ik_rig()
        
    def generate_single_control(self):
        self.link_shapes()
