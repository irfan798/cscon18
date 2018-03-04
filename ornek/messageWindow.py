#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 21:42:58 2018

@author: irfan
"""

import sys
import random
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.oynat = 40
        
        self.setGeometry(300, 300, 250, 150)        
        self.setWindowTitle('Message box')    
        self.show()
        self.setWindowOpacity(0.5)
        self.setMouseTracking(True)
        

    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
    def mouseMoveEvent(self, event):
        print(event.x(), event.y())
        print(event.globalX(), event.globalY())
        
        #self.width
        #self.height
        
        yeni_x = self.x() + random.randint(-self.oynat,self.oynat)
        yeni_y = self.y() + random.randint(-self.oynat,self.oynat)
        
        
        self.move(yeni_x, yeni_y)

    def enterEvent(self, event):
        print(event.x, event.y)        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
