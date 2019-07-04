#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys
from PyQt5.QtWidgets import (QWidget,QApplication,QPushButton,QMessageBox,QMainWindow,
                             QTextEdit,QAction,QFileDialog,QGridLayout)
from PyQt5.QtCore import QCoreApplication,QRect
import excel_repivot_spending


# In[2]:


class Excel_Pandas_Tools(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(100,100,600,400)
        self.setWindowTitle("Excel Pandas Tools")
        self.show()
        
        sbtn = QPushButton('select a file',self)# 创建选择文件按钮 
        sbtn.setObjectName('sbtn')
        sbtn.clicked.connect(self.select_file)
        
        self.textEdit = QTextEdit(self) # 添加文本框输入filename
        
        rbtn = QPushButton('run the procedure',self)# 创建运行程序按钮
        rbtn.setObjectName('rbtn')
        rbtn.clicked.connect(lambda:excel_repivot_spending.main(self.filename))
        
        qbtn = QPushButton('quit', self)# 创建退出按钮
        qbtn.setObjectName('qbtn')
        qbtn.clicked.connect(self.close)
        
        grid = QGridLayout()
        grid.setSpacing(10)
         
        grid.addWidget(sbtn,1,0,2,1)
        grid.addWidget(self.textEdit,1,1,2,1)
        grid.addWidget(rbtn,4,0,2,1)
        grid.addWidget(qbtn,4,1,2,1)
        
        self.setLayout(grid) 

        
    def select_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '.')
        filename = fname[0]
        if filename:
            self.textEdit.setText(filename)
            self.filename = filename
        print(self.textEdit)
        print(type(self.textEdit))
#         print(self.textEdit.text())
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Excel_Pandas_Tools()
    sys.exit(app.exec_())


# In[ ]:




