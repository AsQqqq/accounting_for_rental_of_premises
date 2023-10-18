from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QTimer
from PyQt5.QtWidgets import (
    QHBoxLayout, QLabel, QPushButton, QWidget, QVBoxLayout, QListWidget,
    QListWidgetItem, QMessageBox, QFormLayout, QGroupBox, QScrollArea, QInputDialog
)
import sys
from database import mainBase as db

from designe import main, main2, login

class CommonApp(QWidget):
    def __init__(self, parent=None) -> None:
        super(CommonApp, self).__init__(parent)
        self.m_drag: bool = False
        self.m_DragPosition: QPoint = QPoint()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self,
            blurRadius=10.0,
            color=QtGui.QColor(255, 255, 255),
            offset=QtCore.QPointF(0, 0)
        )
        self.setGraphicsEffect(self.shadow)

    def hideWindow(self) -> None:
        self.showMinimized()

    def closeWindow(self) -> None:
        self.close()

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event) -> None:
        if event.buttons() & Qt.LeftButton and self.m_drag:
            self.move(event.globalPos() - self.m_DragPosition)
            event.accept()

    def mouseReleaseEvent(self, event) -> None:
        self.m_drag = False


class LoginForm(CommonApp, login.Ui_Form):
    swithToMain = pyqtSignal()

    def __init__(self, parent=None) -> None:
        super(LoginForm, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.hideButton.clicked.connect(self.hideWindow)
        self.closeButton.clicked.connect(self.closeWindow)
        self.connected()
    

    def connected(self) -> None:
       """Подключение кнопок"""
       self.login.textChanged.connect(self.getLogin)
       self.password.textChanged.connect(self.getPassword)
       self.signup.clicked.connect(self.pressSignup)
    

    def getLogin(self, text) -> None:
        """Добовление стелей к полю ввода"""
        current_style = self.login.styleSheet()

        if len(text) >= 3:
            new_style = f"{current_style} * {{border-bottom-color: green;}} *:focus {{border-bottom-color: green;}}"
            self.login.setStyleSheet(new_style)
        else:
            new_style = f"{current_style} * {{border-bottom-color: red;}} *:focus {{border-bottom-color: #fd413c;}}"
            self.login.setStyleSheet(new_style)
    

    def getPassword(self, text) -> None:
        """Добовление стелей к полю ввода"""
        current_style = self.password.styleSheet()

        if len(text) >= 4:
            new_style = f"{current_style} * {{border-bottom-color: green;}} *:focus {{border-bottom-color: green;}}"
            self.password.setStyleSheet(new_style)
        else:
            new_style = f"{current_style} * {{border-bottom-color: red;}} *:focus {{border-bottom-color: #fd413c;}}"
            self.password.setStyleSheet(new_style)
    

    def pressSignup(self) -> None:
        """Вход в аккаунт"""
        if len(self.login.text()) >= 3 and len(self.password.text()) >= 4:

            if db().checkSignUp(login=self.login.text(), password=self.password.text()) == True:
                self.swithToMain.emit()
            else:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setStyleSheet("* {\n"
                                    "color: white;\n"
                                    "background-color: #2d3035;\n"
                                    "}\n"
                                    "*:hover {\n"
                                    "border-color: #DBDBDB;\n"
                                    "}\n")
                msgBox.setWindowTitle("Ошибка!")
                msgBox.setText("Неверный логин или пароль")
                msgBox.exec_()
        else:
            if len(self.login.text()) < 3 and len(self.password.text()) >= 4:
                current_style = self.login.styleSheet()
                new_style = f"{current_style} * {{border-color: yellow;}} *:focus {{border-bottom-color: #fd413c;}}"
                self.login.setStyleSheet(new_style)

                # Задача таймера вадача возвести виджет в исходное состояние, через 2 секунды
                QTimer.singleShot(1000, lambda: self.login.setStyleSheet(current_style))
            elif len(self.password.text()) < 4 and len(self.login.text()) >= 3:
                current_style = self.password.styleSheet()
                new_style = f"{current_style} * {{border-color: yellow;}} *:focus {{border-bottom-color: #fd413c;}}"
                self.password.setStyleSheet(new_style)

                # Задача таймера вадача возвести виджет в исходное состояние, через 2 секунды
                QTimer.singleShot(1000, lambda: self.password.setStyleSheet(current_style))
            else:
                current_style = self.login.styleSheet()
                current_style = self.password.styleSheet()
                new_style = f"{current_style} * {{border-color: yellow;}} *:focus {{border-bottom-color: #fd413c;}}"
                self.login.setStyleSheet(new_style)
                self.password.setStyleSheet(new_style)
                
                # Задача таймера вадача возвести виджет в исходное состояние, через 2 секунды
                QTimer.singleShot(1000, 
                    lambda: (
                        self.login.setStyleSheet(current_style),
                        self.password.setStyleSheet(current_style)))
            


class MainForm(CommonApp, main.Ui_Form):
    swithToLoginForMain = pyqtSignal()
    swithToMain2ForMain = pyqtSignal()

    def __init__(self, parent=None) -> None:
        super(MainForm, self).__init__(parent)
        self.setupUi(self)
        
        self.setGraphicsEffect(self.shadow)

        self.setFixedSize(self.size())
        
        self.buttons = dict()

        self.hideButton.clicked.connect(self.hideWindow)
        self.closeButton.clicked.connect(self.closeWindow)
        self.connected()


    

    def connected(self) -> None:
       """Подключение кнопок"""
       self.exit.clicked.connect(self.exitAccount)
       self.rented.clicked.connect(self.swithMain2)

    
    def exitAccount(self) -> None:
        """Выход из аккаунта"""
        db().exit()
        self.swithToLoginForMain.emit()
    

    def swithMain2(self) -> None:
        """Открываем другое окно"""
        self.swithToMain2ForMain.emit()

    
    def zapolnenitTest(self) -> None:
        self.formLayout = QFormLayout()
        groupBox = QGroupBox()
        
        
        for i in db().selectNonePri():
            labelList = QLabel(f"{i[0]}, {i[2]}, {i[3]}")

            button = QPushButton("Добавить")
            self.buttons[button] = labelList
            button.clicked.connect(self.deleteLine)
            button.setProperty('row', f"{i[0]}, {i[2]}, {i[3]}")

            button.setStyleSheet("color: white;\n"
            "background-color: #2d3035;\n"
            "border: 2px solid #878787;\n"
            "border-radius: 15px;\n"
            "width: 10px;\n"
            "}\n"
            "\n"
            "*:hover {\n"
            "border: 2px solid #DBDBDB;\n"
            "}\n"
            "\n"
            "*:focus {\n"
            "border-color: green;\n"
            "border-color: red;\n"
            "}\n"
            "")

            buttonList = button

            self.formLayout.addRow(labelList, buttonList)

        groupBox.setLayout(self.formLayout)
        scroll = self.scroll
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedWidth(630)
        scroll.setFixedHeight(200)


        layout = QVBoxLayout()
        layout.addWidget(scroll)

        self.setLayout(layout)


    def deleteLine(self):
        la = False
        i, okPressed = QInputDialog.getInt(self, "Enter integer","Number:", 0, 0, 600, 1)
        if okPressed:
            if int(i) > 0:
                sender = self.sender()  # Получение объекта, который отправил сигнал
                widget = self.buttons[sender]  # Получаем виджет по кнопке

                line = sender.property('row')
                loc = line.split(',')[:3]
                location = f"{loc[0]},{loc[1]},{loc[2]}"

                # Находим индекс строки в QFormLayout
                index = self.formLayout.getWidgetPosition(widget)[0]

                self.formLayout.removeRow(index)  # Удаляем строку
                db().changeLine(location=location, val=i)
                la = True
            else: la = False
        else: la = False
        if la == False:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setStyleSheet("* {\n"
                                "color: white;\n"
                                "background-color: #2d3035;\n"
                                "}\n"
                                "*:hover {\n"
                                "border-color: #DBDBDB;\n"
                                "}\n")
            msgBox.setWindowTitle("Ошибка!")
            msgBox.setText("Введи значение.")
            msgBox.exec_()



class Main2Form(CommonApp, main2.Ui_Form):
    swithToLoginForMain2 = pyqtSignal()
    swithToMainForMain2 = pyqtSignal()

    def __init__(self, parent=None) -> None:
        super(Main2Form, self).__init__(parent)
        self.setupUi(self)
        
        self.setGraphicsEffect(self.shadow)

        self.setFixedSize(self.size())
        
        self.buttons = dict()

        self.hideButton.clicked.connect(self.hideWindow)
        self.closeButton.clicked.connect(self.closeWindow)
        self.connected()

    

    def connected(self) -> None:
        """Подключение кнопок"""
        self.exit.clicked.connect(self.exitAccount)
        self.unoccupied.clicked.connect(self.swithMain)


        """TEST"""
        self.zapolnenitTest()

    
    def exitAccount(self) -> None:
        """Выход из аккаунта"""
        db().exit()
        self.swithToLoginForMain2.emit()
    
    
    def swithMain(self) -> None:
        """Открываем другое окно"""
        self.swithToMainForMain2.emit()
    

    def zapolnenitTest(self) -> None:
        self.formLayout = QFormLayout()
        groupBox = QGroupBox()
        
        
        for i in db().selectFullPri():
            labelList = QLabel(f"{i[0]}, {i[2]}, {i[3]}, {i[4]}")

            button = QPushButton("Удалить")

            self.buttons[button] = labelList
            button.clicked.connect(self.deleteLine)
            button.setProperty('row', f"{i[0]}, {i[2]}, {i[3]}, {i[4]}")

            button.setStyleSheet("color: white;\n"
            "background-color: #2d3035;\n"
            "border: 2px solid #878787;\n"
            "border-radius: 15px;\n"
            "width: 10px;\n"
            "}\n"
            "\n"
            "*:hover {\n"
            "border: 2px solid #DBDBDB;\n"
            "}\n"
            "\n"
            "*:focus {\n"
            "border-color: green;\n"
            "border-color: red;\n"
            "}\n"
            "")

            buttonList = button

            self.formLayout.addRow(labelList, buttonList)

        groupBox.setLayout(self.formLayout)
        scroll = self.scroll
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedWidth(630)
        scroll.setFixedHeight(200)

        layout = QVBoxLayout()
        layout.addWidget(scroll)

        self.setLayout(layout)
    
    def deleteLine(self):
        sender = self.sender()  # Получение объекта, который отправил сигнал
        widget = self.buttons[sender]  # Получаем виджет по кнопке

        line = sender.property('row')
        loc = line.split(',')[:3]
        location = f"{loc[0]},{loc[1]},{loc[2]}"

        # Находим индекс строки в QFormLayout
        index = self.formLayout.getWidgetPosition(widget)[0]

        self.formLayout.removeRow(index) 
        db().changeLine(location=location, val=None)


class MainApp(QtWidgets.QApplication):
    def __init__(self, sys_argv) -> None:
        super(MainApp, self).__init__(sys_argv)
    
        self.loginForm = LoginForm()
        self.MainForm = MainForm()
        self.Main2Form = Main2Form()

        self.loginForm.swithToMain.connect(self.swithToMain)
        self.MainForm.swithToLoginForMain.connect(self.swithToLoginForMain)
        self.MainForm.swithToMain2ForMain.connect(self.swithToMain2ForMain)
        self.Main2Form.swithToLoginForMain2.connect(self.swithToLoginForMain2)
        self.Main2Form.swithToMainForMain2.connect(self.swithToMainForMain2)
        
        if db().join():
            self.MainForm.zapolnenitTest()
            self.MainForm.show()
        else:
            self.loginForm.show()
    

    def getPosition(self):
        """Здесь мы получаем место положения окна,
        для того что бы потом новое окно поставить на его место"""
        if self.activeWindow() is not None:
            return self.activeWindow().pos()
        else:
            return QtCore.QPoint(0, 0)


    def swithToMain(self) -> None:
        windowPos = self.getPosition()
        self.MainForm.move(windowPos)
        self.MainForm.show()
        self.loginForm.close()
    
    
    def swithToLoginForMain(self) -> None:
        windowPos = self.getPosition()
        self.loginForm.move(windowPos)
        self.loginForm.show()
        self.MainForm.close()
    
    
    def swithToLoginForMain2(self) -> None:
        windowPos = self.getPosition()
        self.loginForm.move(windowPos)
        self.loginForm.show()
        self.Main2Form.close()
    
    
    def swithToMainForMain2(self) -> None:
        windowPos = self.getPosition()
        self.MainForm.zapolnenitTest()
        self.MainForm.move(windowPos)
        self.MainForm.show()
        self.Main2Form.close()
    
    
    def swithToMain2ForMain(self) -> None:
        windowPos = self.getPosition()
        self.Main2Form.zapolnenitTest()
        self.Main2Form.move(windowPos)
        self.Main2Form.show()
        self.MainForm.close()

if __name__ == "__main__":
    import sys
    app = MainApp(sys.argv)
    sys.exit(app.exec())