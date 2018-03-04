#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 02:49:14 2018

@author: irfan
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget

   
app = QApplication(sys.argv)

w = QWidget()
w.resize(250, 150)
w.move(500, 500)
w.setWindowTitle('Simple')
w.show()

sys.exit(app.exec_())