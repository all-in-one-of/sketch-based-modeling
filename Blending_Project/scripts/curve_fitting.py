import maya.api.OpenMaya as om
import maya.cmds as cmds
from PySide2 import QtCore, QtGui, QtWidgets
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
import math,sys

sys.path.append('/usr/lib64/python2.7/site-packages')
sys.path.append('./.local/lib/python2.7/site-packages')
import numpy


def maya_useNewAPI():
    pass


def maya_main_window():
    main_window_ptr=omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr),QtWidgets.QWidget)
    
             
class CurveFittingWindowUI(QtWidgets.QMainWindow):
    
    def __init__(self,parent=maya_main_window()):
        super(CurveFittingWindowUI,self).__init__(parent)
        
        self.setWindowTitle("Generalized Ellipse")
        self.setMinimumSize(900,650)
        self.setObjectName("generalizedEllipseWin")
        self.setWindowFlags(QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
               
        self.create_widgets()   
        self.create_layout()
        self.create_connection()
        
        #self.canvas.installEventFilter()
                    
            
    def create_widgets(self):
        self.button_generate=QtWidgets.QPushButton('Generate')
        self.button_generate.setObjectName('generate_button')
        self.button_generate.setFixedWidth(100)
        self.button_save=QtWidgets.QPushButton('Save')
        self.button_save.setObjectName('save_button')
        self.button_save.setFixedWidth(100)
        
        self.standardEllipse_checkBox=QtWidgets.QCheckBox('standard ellipse')
        self.standardEllipse_checkBox.setChecked(False)
        self.standardEllipse_checkBox.setFixedWidth(200)
        self.standardEllipse_checkBox.setObjectName('standardEllipse_checkBox')
        
        self.generalizedEllipse_checkBox=QtWidgets.QCheckBox('generalized ellipse')
        self.generalizedEllipse_checkBox.setChecked(False)
        self.generalizedEllipse_checkBox.setFixedWidth(200)
        self.generalizedEllipse_checkBox.setObjectName('generalizedEllipse_checkBox')
        
        self.J_spinBox=QtWidgets.QSpinBox()
        self.J_spinBox.setValue(10)
        self.J_spinBox.setFixedWidth(200)
        self.J_spinBox.setMinimum(1)
        self.J_spinBox.setSingleStep(1)
        
        self.Ea_LineEdit=QtWidgets.QLineEdit()
        self.Ea_LineEdit.setFixedWidth(200)

        self.Em_LineEdit=QtWidgets.QLineEdit()
        self.Em_LineEdit.setFixedWidth(200)
        
        self.canvas=Canvas()       
        #self.label_standardEllipse=QtWidgets.QLabel(':')


    def create_layout(self):            
        widget_layout_central=QtWidgets.QWidget()
        self.setCentralWidget(widget_layout_central)
        main_layout=QtWidgets.QHBoxLayout(widget_layout_central)
                
        # create layout for canvas
        left_layout=QtWidgets.QVBoxLayout()
        
        left_layout.addWidget(self.canvas)
        left_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)        
              
        # create layout for parameters and operation buttons
        right_layout=QtWidgets.QVBoxLayout()
        right_layout.addWidget(self.standardEllipse_checkBox)
        right_layout.addWidget(self.generalizedEllipse_checkBox)
        #right_layout.addWidget(self.J_spinBox)
        # add a spacer
        spacer=QtWidgets.QSpacerItem(0,100)
        right_layout.addSpacerItem(spacer)
        

        right_layout.addWidget(self.button_generate)
        right_layout.addWidget(self.button_save)
        
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)
        

    def create_connection(self):
        self.button_generate.clicked.connect(self.createEllipse)
        self.standardEllipse_checkBox.clicked.connect(self.drawMode_standardEllipse)
        self.generalizedEllipse_checkBox.clicked.connect(self.drawMode_generalizedEllipse)
        
          
    def createEllipse(self):
        print "ellipse created"
    
        
    def drawMode_standardEllipse(self):
        if cmds.control('standardEllipse'+'_checkBox',exists=True):
            ptr=omui.MQtUtil.findControl('standardEllipse_checkBox')
            checkBox=wrapInstance(long(ptr),QtWidgets.QCheckBox)
            value=checkBox.isChecked()
            if value==True:
                self.drawStandardEllipse()
            else:
                pass
            
            
    def drawMode_generalizedEllipse(self):
        if cmds.control('generalizedEllipse'+'_checkBox',exists=True):
            ptr=omui.MQtUtil.findControl('generalizedEllipse_checkBox')
            checkBox=wrapInstance(long(ptr),QtWidgets.QCheckBox)
            value=checkBox.isChecked()
            if value==True:
                self.drawGeneralizedEllipse()
            else:
                pass
        
                
    def drawStandardEllipse(self):
        print "draw standard ellipse"             


    def drawGeneralizedEllipse(self):
        print "draw generalized ellipse"


class Canvas(QtWidgets.QWidget):
    backgroundColor=QtCore.Qt.white
    def __init__(self,parent=None):
        super(Canvas,self).__init__(parent)
        self.setMinimumSize(600,600)
        
    def paintEvent(self,evt):
        painter=QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing,True)
        # Draw the background
        painter.setBrush(Canvas.backgroundColor)
        painter.drawRect(self.rect())
           

if __name__=="__main__":
    # Check to see if the UI already exists and if so, delete
    if cmds.window("generalizedEllipseWin",exists=True):
        cmds.deleteUI("generalizedEllipseWin",wnd=True)
        
    w=CurveFittingWindowUI()
    w.show()  
    #w.raise_() 


    
#cmds.flushUndo()
#cmds.scriptEditorInfo(clearHistory=True)