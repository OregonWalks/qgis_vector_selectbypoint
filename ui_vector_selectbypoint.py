# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_vector_selectbypoint.ui'
#
# Created: Mon Apr  7 00:34:57 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_vector_selectbypoint(object):
    def setupUi(self, vector_selectbypoint):
        vector_selectbypoint.setObjectName(_fromUtf8("vector_selectbypoint"))
        vector_selectbypoint.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(vector_selectbypoint)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.txtFeedback = QtGui.QTextBrowser(vector_selectbypoint)
        self.txtFeedback.setGeometry(QtCore.QRect(10, 10, 381, 201))
        self.txtFeedback.setObjectName(_fromUtf8("txtFeedback"))
        self.chkActivate = QtGui.QCheckBox(vector_selectbypoint)
        self.chkActivate.setGeometry(QtCore.QRect(10, 220, 89, 31))
        self.chkActivate.setObjectName(_fromUtf8("chkActivate"))

        self.retranslateUi(vector_selectbypoint)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), vector_selectbypoint.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), vector_selectbypoint.reject)
        QtCore.QMetaObject.connectSlotsByName(vector_selectbypoint)

    def retranslateUi(self, vector_selectbypoint):
        vector_selectbypoint.setWindowTitle(QtGui.QApplication.translate("vector_selectbypoint", "vector_selectbypoint", None, QtGui.QApplication.UnicodeUTF8))
        self.chkActivate.setText(QtGui.QApplication.translate("vector_selectbypoint", "Activate\n"
" (Check)", None, QtGui.QApplication.UnicodeUTF8))

