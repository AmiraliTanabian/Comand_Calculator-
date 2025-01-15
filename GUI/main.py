
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(250, 200)
        Form.setMinimumSize(QtCore.QSize(250, 200))
        Form.setMaximumSize(QtCore.QSize(250, 200))
        Form.setStyleSheet("background-color:#202020;")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setStyleSheet("color:white;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.input2 = QtWidgets.QLineEdit(parent=Form)
        self.input2.setStyleSheet("color:white;")
        self.input2.setObjectName("input2")
        self.verticalLayout.addWidget(self.input2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plus = QtWidgets.QPushButton(parent=Form)
        self.plus.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.plus.setStyleSheet("background-color:#3C3C3C;\n"
"color:white;\n"
"")
        self.plus.setObjectName("plus")
        self.verticalLayout_2.addWidget(self.plus)
        self.divide = QtWidgets.QPushButton(parent=Form)
        self.divide.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.divide.setStyleSheet("background-color:#3C3C3C;\n"
"color:white;")
        self.divide.setObjectName("divide")
        self.verticalLayout_2.addWidget(self.divide)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.sub = QtWidgets.QPushButton(parent=Form)
        self.sub.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.sub.setStyleSheet("background-color:#3C3C3C;\n"
"color:white;")
        self.sub.setObjectName("sub")
        self.verticalLayout_3.addWidget(self.sub)
        self.multiplication = QtWidgets.QPushButton(parent=Form)
        self.multiplication.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.multiplication.setStyleSheet("background-color:#3C3C3C;\n"
"color:white;\n"
"\n"
"\n"
"")
        self.multiplication.setObjectName("multiplication")
        self.verticalLayout_3.addWidget(self.multiplication)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.output = QtWidgets.QLineEdit(parent=Form)
        self.output.setStyleSheet("color:white;")
        self.output.setObjectName("output")
        self.verticalLayout.addWidget(self.output)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.plus.clicked.connect(self.sum)
        self.divide.clicked.connect(self.calcDivide)
        self.sub.clicked.connect(self.calcSub)
        self.multiplication.clicked.connect(self.calcMulti)


        numValidator = QtGui.QIntValidator()
        self.lineEdit_3.setValidator(numValidator)
        self.input2.setValidator(numValidator)


        # Set hover style for btns
        hoverStyle = """QPushButton:hover{
                        background-color:gray;
                        }
                        QPushButton{
                        background-color:#3C3C3C;
                        color:white;
                        }
                        """

        self.plus.setStyleSheet(hoverStyle)
        self.divide.setStyleSheet(hoverStyle)
        self.multiplication.setStyleSheet(hoverStyle)
        self.sub.setStyleSheet(hoverStyle)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculaor"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Number 1"))
        self.input2.setPlaceholderText(_translate("Form", "Number 2"))
        self.plus.setText(_translate("Form", "+"))
        self.divide.setText(_translate("Form", "/"))
        self.sub.setText(_translate("Form", "-"))
        self.multiplication.setText(_translate("Form", "*"))
        self.output.setPlaceholderText(_translate("Form", "OutPut"))

    def sum(self):
        num1 = float(self.lineEdit_3.text())
        num2 = float(self.input2.text())
        self.output.setText(str(num1 + num2))

    def calcDivide(self):
        num1 = float(self.lineEdit_3.text())
        num2 = float(self.input2.text())
        self.output.setText(str(num1 / num2))

    def calcMulti(self):
        num1 = float(self.lineEdit_3.text())
        num2 = float(self.input2.text())
        self.output.setText(str(num1 * num2))


    def calcSub(self):
        num1 = float(self.lineEdit_3.text())
        num2 = float(self.input2.text())
        self.output.setText(str(num1 - num2))


if __name__ == "__main__":
    try :
        import sys

        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec())

    # beacuse when we click the button without type anything in the fild app doesn't close
    except :
        print("Error")
