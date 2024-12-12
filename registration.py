# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_registration(object):
    def setupUi(self, registration):
        registration.setObjectName("registration")
        registration.resize(655, 580)
        registration.setStyleSheet("background-color: rgb(51, 51, 51);")

        # Поле для ввода логина
        self.lineEdit_regist_login = QtWidgets.QLineEdit(registration)
        self.lineEdit_regist_login.setGeometry(QtCore.QRect(106, 88, 443, 55))
        self.lineEdit_regist_login.setStyleSheet(
            """
            QLineEdit {
                border-radius: 10px;
                font-size: 20px;
                background-color: white;
                padding-left: 10px;
            }
            """
        )
        self.lineEdit_regist_login.setPlaceholderText("Login")
        self.lineEdit_regist_login.setObjectName("lineEdit_regist_login")

        # Поле для ввода пароля
        self.lineEdit_registration_password = QtWidgets.QLineEdit(registration)
        self.lineEdit_registration_password.setGeometry(QtCore.QRect(106, 177, 443, 55))
        self.lineEdit_registration_password.setStyleSheet(
            """
            QLineEdit {
                border-radius: 10px;
                font-size: 20px;
                background-color: white;
                padding-left: 10px;
            }
            """
        )
        self.lineEdit_registration_password.setPlaceholderText("Password")
        self.lineEdit_registration_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_registration_password.setObjectName("lineEdit_registration_password")

        # Поле для подтверждения пароля
        self.lineEdit_confirmregistpassword = QtWidgets.QLineEdit(registration)
        self.lineEdit_confirmregistpassword.setGeometry(QtCore.QRect(106, 262, 443, 55))
        self.lineEdit_confirmregistpassword.setStyleSheet(
            """
            QLineEdit {
                border-radius: 10px;
                font-size: 20px;
                background-color: white;
                padding-left: 10px;
            }
            """
        )
        self.lineEdit_confirmregistpassword.setPlaceholderText("Confirm Password")
        self.lineEdit_confirmregistpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_confirmregistpassword.setObjectName("lineEdit_confirmregistpassword")

        # Чекбокс "I'm not a robot"
        self.checkBox = QtWidgets.QCheckBox(registration)
        self.checkBox.setGeometry(QtCore.QRect(110, 335, 361, 31))
        self.checkBox.setStyleSheet(
        """
        QCheckBox {
            color: white;
            font-size: 18px;
        }
        QCheckBox::indicator {
            width: 30px; 
            height: 30px;
        }
        """
        )

        # self.checkBox.raise_()

        self.checkBox.setText("I'm not a robot")
        self.checkBox.setChecked(False)  # Чекбокс по умолчанию не отмечен
        self.checkBox.setObjectName("checkBox")

        # Кнопка регистрации
        self.pushButton_register_login = QtWidgets.QPushButton(registration)
        self.pushButton_register_login.setGeometry(QtCore.QRect(187, 443, 282, 56))
        self.pushButton_register_login.setStyleSheet(
            """
            QPushButton {
                background-color: #FF0000;
                color: white;
                font-size: 18px;
                font-weight: bold;
                border-radius: 10px;
            }
            """
        )
        self.pushButton_register_login.setObjectName("pushButton_register_login")

        self.retranslateUi(registration)
        QtCore.QMetaObject.connectSlotsByName(registration)

    def retranslateUi(self, registration):
        _translate = QtCore.QCoreApplication.translate
        registration.setWindowTitle(_translate("registration", "Registration Form"))
        self.pushButton_register_login.setText(_translate("registration", "Register"))


