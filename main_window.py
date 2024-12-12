# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
# Created by: PyQt5 UI code generator 5.15.11

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(655, 580)
        main.setStyleSheet("background-color: rgb(51, 51, 51);")

        # Sign Out Button
        self.pushButton_sign_out_main = QtWidgets.QPushButton(main)
        self.pushButton_sign_out_main.setGeometry(QtCore.QRect(40, 30, 121, 31))
        self.pushButton_sign_out_main.setStyleSheet(
            "QPushButton {"
            "    background-color: white;"
            "    color: black;"
            "    font-size: 18px;"  # Увеличение размера текста
            "    border-radius: 10px;"  # Радиус скругления углов
            "}"
        )
        self.pushButton_sign_out_main.setObjectName("pushButton_sign_out_main")

        # Buy Button
        self.pushButton_but_main = QtWidgets.QPushButton(main)
        self.pushButton_but_main.setGeometry(QtCore.QRect(51, 381, 550, 50))
        self.pushButton_but_main.setStyleSheet(
            "QPushButton {"
            "    background-color: #FF0000;"
            "    color: white;"
            "    font-size: 18px;"
            "    font-weight: bold;"
            "    border-radius: 10px;"
            "}"
        )
        self.pushButton_but_main.setObjectName("pushButton_but_main")

        # User History Button
        self.pushButton_user_history = QtWidgets.QPushButton(main)
        self.pushButton_user_history.setGeometry(QtCore.QRect(342, 465, 261, 50))
        self.pushButton_user_history.setStyleSheet(
            "QPushButton {"
            "    background-color: white;"
            "    color: black;"
            "    font-size: 18px;"
            "    border-radius: 10px;"
            "}"
        )
        self.pushButton_user_history.setObjectName("pushButton_user_history")

        # Movie Info Button
        self.pushButton_movi_info = QtWidgets.QPushButton(main)
        self.pushButton_movi_info.setGeometry(QtCore.QRect(55, 465, 258, 50))
        self.pushButton_movi_info.setStyleSheet(
            "QPushButton {"
            "    background-color: white;"
            "    color: black;"
            "    font-size: 18px;"
            "    border-radius: 10px;"
            "}"
        )
        self.pushButton_movi_info.setObjectName("pushButton_movi_info")

        # Movie Title List
        self.listWidget_main_title = QtWidgets.QListWidget(main)
        self.listWidget_main_title.setGeometry(QtCore.QRect(50, 150, 251, 171))
        self.listWidget_main_title.setStyleSheet(
            "QListWidget {"
            "    background-color: white;"
            "    color: black;"
            "    font-size: 18px;"
            "    border-radius: 10px;"
            "}"
        )
        self.listWidget_main_title.setObjectName("listWidget_main_title")

        # Movie Schedule List
        self.listWidget_main_schedule = QtWidgets.QListWidget(main)
        self.listWidget_main_schedule.setGeometry(QtCore.QRect(350, 150, 256, 171))
        self.listWidget_main_schedule.setStyleSheet(
            "QListWidget {"
            "    background-color: white;"
            "    color: black;"
            "    font-size: 18px;"
            "    border-radius: 10px;"
            "}"
        )
        self.listWidget_main_schedule.setObjectName("listWidget_main_schedule")

        # Movie Title Label
        self.label_movie_title_main = QtWidgets.QLabel(main)
        self.label_movie_title_main.setGeometry(QtCore.QRect(125, 110, 131, 31))
        self.label_movie_title_main.setStyleSheet(
            "color: #FFFFFF;"
            "font-size: 22px;"
        )
        self.label_movie_title_main.setObjectName("label_movie_title_main")

        # Movie Schedule Label
        self.label_movi_schedule_main = QtWidgets.QLabel(main)
        self.label_movi_schedule_main.setGeometry(QtCore.QRect(400, 110, 151, 31))
        self.label_movi_schedule_main.setStyleSheet(
            "color: #FFFFFF;"
            "font-size: 22px;"
        )
        self.label_movi_schedule_main.setObjectName("label_movi_schedule_main")

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Form"))
        self.pushButton_sign_out_main.setText(_translate("main", "SIGN OUT"))
        self.pushButton_but_main.setText(_translate("main", "Buy"))
        self.pushButton_user_history.setText(_translate("main", "User history"))
        self.pushButton_movi_info.setText(_translate("main", "Movie info"))
        self.listWidget_main_title.setToolTip(
            _translate("main", "<html><head/><body><p>kjhkj</p></body></html>")
        )
        self.label_movie_title_main.setText(_translate("main", "Movie title"))
        self.label_movi_schedule_main.setText(_translate("main", "Movie schedule"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QWidget()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())
