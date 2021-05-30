from  PyQt5 import  QtGui,QtWidgets,QtCore
import  sys 
from  Ui_ui import  Ui_MainWindow
from  Ui_dlg_setting import Ui_Dlg_Setting

import random
import os 

from  functools import  partial
import datetime
import json 


class SettingDlg(QtWidgets.QDialog):
    sigAccepted = QtCore.pyqtSignal(int,int)
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dlg_Setting()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.a)
    
    def a(self):
        # 
        rows = self.ui.spinBox_rows.value()
        cols = self.ui.spinBox_cols.value()
        self.sigAccepted.emit(rows,cols)
        self.accept()



class MyMain(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.init_game)
        self.cols = 5
        self.rows = 5
        
        self.mines_layout = QtWidgets.QGridLayout(self.ui.frame)
        self.ui.frame.setLayout(self.mines_layout)
        self.buttons = []
        self.idx = 0
        self.run = False
        self.t0 = 0

        self.dlg_setting = SettingDlg()
        self.ui.actionsetting.triggered.connect(self.dlg_setting.show)
        self.dlg_setting.sigAccepted.connect(self.setting)
        


    def setting(self,rows,cols):
        self.cols = cols
        self.rows = rows

    def btn_click(self,idx):
        if self.run:
            if self.idx == self.data[idx]:
                self.buttons[idx].setStyleSheet('background:#6DDF6D')
                self.idx += 1
                
            if self.idx >= self.rows * self.cols:
                self.timer.stop()
                self.run = False 
                self.ui.actionsetting.setEnabled(True)
                self.log()

            pass # if self
        


    def init_game(self):

        self.mines = self.cols * self.rows

        self.buttons = []
        
        self.data = list(range(self.cols * self.rows))

        random.shuffle(self.data)

        for i in range(self.mines_layout.count()):
	        self.mines_layout.itemAt(i).widget().deleteLater()

        s = self.ui.frame.size()
        w = s.width()
        h =s.height()
        fontsize = min(w / self.cols // 2,h / self.rows//2)
        
        self.ui.actionsetting.setEnabled(False)

        for i in range(self.mines):
            btn = QtWidgets.QPushButton(self.ui.frame)
            btn.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            btn.setText(str(self.data[i]))
            font = QtGui.QFont()
            font.setPointSize(fontsize)
            btn.setFont(font)
            btn.clicked.connect(partial(self.btn_click,i))
            
            self.mines_layout.addWidget(btn,i // self.cols,i % self.cols)
            self.buttons.append(btn)

        self.idx = 0
        self.t0 = 0
        self.run = True 
        self.timer = QtCore.QTimer()
        self.timer.start(100)
        self.timer.timeout.connect(self.tick)
    
    def tick(self):
        self.t0 += 0.1
        self.ui.label_time.setText('{:.1f}'.format(self.t0))

    def log(self):
        t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        curdir = os.path.split(__file__)[0]

        fn = os.path.join(curdir,'log.log')
        with open(fn,'a',encoding='utf8') as f:
            f.write('{},{:.1f}\n'.format(t,self.t0))
 

                    
    
app = QtWidgets.QApplication(sys.argv)
main = MyMain()
main.show()
app.exec_()