# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\designer\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(670, 410)
        Form.setStyleSheet("* {\n"
"    background-color: 0;\n"
"    border: 0;\n"
"    border-radius: 0;\n"
"}\n"
"*:hover {\n"
"    background-color: 0;\n"
"    border: 0;\n"
"    border-radius: 0;\n"
"}")
        self.rented = QtWidgets.QPushButton(Form)
        self.rented.setGeometry(QtCore.QRect(140, 20, 101, 31))
        self.rented.setStyleSheet("* {\n"
"color: white;\n"
"background-color: #2d3035;\n"
"border: 2px solid #878787;\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"*:hover {\n"
"border: 2px solid #DBDBDB;\n"
"}\n"
"\n"
"*:disabled {\n"
"    background-color: #555A62;\n"
"    color: gray;\n"
"    border-color: gray;\n"
"}\n"
"\n"
"")
        self.rented.setObjectName("rented")
        self.closeButton = QtWidgets.QPushButton(Form)
        self.closeButton.setGeometry(QtCore.QRect(610, 20, 21, 21))
        self.closeButton.setStyleSheet("* {\n"
"background-image: url(:/close/image/close.png);\n"
"}\n"
"\n"
"*:hover {\n"
"background-image: url(:/close/image/close-red.png);\n"
"}")
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.hideButton = QtWidgets.QPushButton(Form)
        self.hideButton.setGeometry(QtCore.QRect(580, 21, 21, 21))
        self.hideButton.setStyleSheet("* {\n"
"background-image: url(:/hide/image/hide.png);\n"
"}\n"
"\n"
"*:hover {\n"
"background-image: url(:/hide/image/hide-gray.png);\n"
"}")
        self.hideButton.setText("")
        self.hideButton.setObjectName("hideButton")
        self.choose = QtWidgets.QLabel(Form)
        self.choose.setGeometry(QtCore.QRect(20, 60, 121, 30))
        self.choose.setStyleSheet("color: white;\n"
"font: 8pt \"Montserrat\";")
        self.choose.setObjectName("choose")
        self.unoccupied = QtWidgets.QPushButton(Form)
        self.unoccupied.setEnabled(False)
        self.unoccupied.setGeometry(QtCore.QRect(30, 20, 101, 31))
        self.unoccupied.setStyleSheet("* {\n"
"color: white;\n"
"background-color: #2d3035;\n"
"border: 2px solid #878787;\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"*:hover {\n"
"border: 2px solid #DBDBDB;\n"
"}\n"
"\n"
"*:disabled {\n"
"    background-color: #555A62;\n"
"    color: gray;\n"
"    border-color: gray;\n"
"}\n"
"")
        self.unoccupied.setObjectName("unoccupied")
        self.exit = QtWidgets.QPushButton(Form)
        self.exit.setGeometry(QtCore.QRect(585, 378, 75, 20))
        self.exit.setStyleSheet("* {\n"
"color: gray;\n"
"}\n"
"*:hover {\n"
"color: red;\n"
"}")
        self.exit.setObjectName("exit")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 651, 391))
        self.frame.setStyleSheet("background-color: #212529;\n"
"border-radius: 20px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.scroll = QtWidgets.QScrollArea(self.frame)
        self.scroll.setGeometry(QtCore.QRect(10, 80, 631, 281))
        self.scroll.setStyleSheet("* {\n"
"background-color: #212529;\n"
"color: white;\n"
"}")
        self.scroll.setWidgetResizable(True)
        self.scroll.setObjectName("scroll")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 631, 281))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scroll.setWidget(self.scrollAreaWidgetContents)
        self.frame.raise_()
        self.rented.raise_()
        self.hideButton.raise_()
        self.choose.raise_()
        self.unoccupied.raise_()
        self.exit.raise_()
        self.closeButton.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.rented.setText(_translate("Form", "арендованные"))
        self.choose.setText(_translate("Form", "Выберите квартиру"))
        self.unoccupied.setText(_translate("Form", "незанятые"))
        self.exit.setText(_translate("Form", "выйти"))
import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
