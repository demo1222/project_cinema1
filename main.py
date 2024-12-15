from PyQt5 import QtWidgets
import sys
import requests
from login import *
from main_window import *
from regis import *
from admin import *
from seats import *
from info import *
from history import *
import json

movie = None
time1 = None
arr = []
me = []
admins = ['emil']

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.login_window = QtWidgets.QMainWindow()
        self.login_ui = Ui_loginpage()
        self.login_ui.setupUi(self.login_window)
        self.login_window.setMaximumSize(655, 580)
        self.login_window.show()

        self.login_ui.pushButtonlogin.clicked.connect(self.login)
        self.login_ui.register_2.linkActivated.connect(self.open_registerwindow)

        self.mouse_moved = False
        self.setMouseTracking(True)
        self.login_window.setMouseTracking(True)

        self.movie = None
        self.time1 = None


    def register(self):
        username = self.register_window_ui.lineEdit_regist_login.text()
        password = self.register_window_ui.lineEdit_registration_password.text()
        confirmation = self.register_window_ui.lineEdit_confirmregistpassword.text()
        if password != confirmation:
            return QtWidgets.QMessageBox.warning(self.login_window, "Error", "Passwords must be matched")
        if len(username) < 1 or len(password) < 1:
            QtWidgets.QMessageBox.warning(self.login_window, "Error", "Please type login/password.")
            return
        url = 'https://zarylbek.pythonanywhere.com/register'
        register_try = {'username': username, 'password':password}
        response = requests.get(url, params=register_try)
        if response.text == 'Success':
            me.append(username)
            self.register_window.close()
            self.open_mainwindow()
        else:
            QtWidgets.QMessageBox.warning(self.login_window, "Error", "Login is already exist, try another one")

    def login(self):
        username = self.login_ui.lineEdit_login.text()
        password = self.login_ui.lineEdit_password.text()
        url = 'https://zarylbek.pythonanywhere.com/login'
        login_try = {'username': username, 'password':password}
        response = requests.get(url, params=login_try)
        if len(username) < 1 or len(password) < 1:
            QtWidgets.QMessageBox.warning(self.login_window, "Error", "Please type login/password.")
            return
        if not self.login_ui.checkBox.isChecked():
            QtWidgets.QMessageBox.warning(self.login_window, "Error", "Please confirm you are not a robot.")
            return
        if response.status_code == 200:
            me.append(username)
            self.login_window.close()
            if username in admins:
                self.open_adminpanel()
            self.open_mainwindow()
        else:
            QtWidgets.QMessageBox.warning(self.login_window, "Error", "Invalid username or password.")

    def mouseMoveEvent(self, event):
        if not self.mouse_moved:
            self.mouse_moved = True
            self.login_ui.checkBox.setEnabled(True)

    def open_adminpanel(self):
        self.admin_window = QtWidgets.QMainWindow()
        self.admin_window_ui = Ui_Admin()
        self.admin_window_ui.setupUi(self.admin_window)
        self.admin_window.setMaximumSize(655, 580)
        self.admin_window.show()

        self.admin_window_ui.pushButton_sign_out.clicked.connect(self.log_out)
        self.admin_window_ui.pushButton_add_movie.clicked.connect(self.add_movie)
        self.admin_window_ui.pushButton_delete_movie.clicked.connect(self.remove_movie)

    def add_movie(self):
        title = self.admin_window_ui.lineEdit_film_title.text()
        time = self.admin_window_ui.lineEdit_film_time.text()
        url = 'https://zarylbek.pythonanywhere.com/add_movie'
        addmovie_try = {'title':title, 'time':time}
        response = requests.get(url, params = addmovie_try)
        if len(title) < 1 or len(time) < 1:
            return QtWidgets.QMessageBox.warning(self.login_window, "Error", "Please type login/password.")
        if response.text == f'{time} is successfully added to movie {title}':
            QtWidgets.QMessageBox.information(self.login_window, "Done", "Successfully added.")
            self.main_window_ui.listWidget_main_title.clear()
            for i in self.checkMovies():
                self.main_window_ui.listWidget_main_title.addItem(i)
        elif response.text ==  f'{time} already exists':
            QtWidgets.QMessageBox.warning(self.login_window, "Error", "Schedule is already exist.")

    def remove_movie(self):
        title = self.admin_window_ui.lineEdit_film_title.text()
        time = self.admin_window_ui.lineEdit_film_time.text()
        url = 'https://zarylbek.pythonanywhere.com/remove_movie'
        removemovie_try = {'title':title, 'time':time}
        response = requests.get(url, params= removemovie_try)
        if len(title) < 1 or len(time) < 1:
            return QtWidgets.QMessageBox.warning(self.login_window, "Error", "Please type login/password.")
        if response.text == 'Success':
            QtWidgets.QMessageBox.information(self.login_window, "Done", "Successfully removed.")
            self.main_window_ui.listWidget_main_title.clear()
            for i in self.checkMovies():
                self.main_window_ui.listWidget_main_title.addItem(i)
            if title == self.movie:
                self.movie = None
                self.time1 = None
        elif response.text ==  'Movie does not exist':
            QtWidgets.QMessageBox.warning(self.login_window, "Error", "Movie does not exist")
        elif response.text == 'Schedule does not exist':
            QtWidgets.QMessageBox.warning(self.login_window, "Error", "Schedule does not exist")
        else:
            QtWidgets.QMessageBox.warning(self.register_window, "Error", "Unknown Error")

    def open_registerwindow(self):
        self.login_window.close()
        self.register_window = QtWidgets.QMainWindow()
        self.register_window_ui = Ui_registration()
        self.register_window.setMaximumSize(655, 580)
        self.register_window_ui.setupUi(self.register_window)
        self.register_window_ui.pushButton_register_login.clicked.connect(self.register)
        # self.register_window_ui.register_2.linkActivated.connect(self.log_out)
        self.register_window.show()

    def open_mainwindow(self):
        self.main_window = QtWidgets.QMainWindow()
        self.main_window_ui = Ui_main()
        self.main_window_ui.setupUi(self.main_window)
        self.main_window.setMaximumSize(655, 580)
        self.main_window.show()

        self.main_window_ui.pushButton_sign_out_main.clicked.connect(self.log_out)
        for i in self.checkMovies():
            self.main_window_ui.listWidget_main_title.addItem(i)
        self.main_window_ui.listWidget_main_title.itemClicked.connect(self.on_item_clicked)
        self.main_window_ui.listWidget_main_schedule.itemClicked.connect(self.changetime)
        self.main_window_ui.pushButton_but_main.clicked.connect(self.open_buyseatswindow)
        self.main_window_ui.pushButton_movi_info.clicked.connect(self.open_MovieInfoWindow)
        self.main_window_ui.pushButton_user_history.clicked.connect(self.open_UserHistoryWindow)

    def checkMovies(self):
        url = 'https://zarylbek.pythonanywhere.com/get_onlymovies'
        response = requests.get(url)
        return json.loads(response.text)
    
    def on_item_clicked(self, item):
        arr.clear()
        self.main_window_ui.listWidget_main_schedule.clear()
        self.movie = item.text()
        self.time1 = None
        res = []
        url = 'https://zarylbek.pythonanywhere.com/get_movies'
        response = requests.get(url)
        print(response.text)
        jsonied = response.json()
        for i,k in jsonied.items():  #{moana:[11:30, 12:30, moana2:[11:30]]}
            if i == item.text():
                res += k
        print(item.text())
        for i in res:
            self.main_window_ui.listWidget_main_schedule.addItem(i)
        self.main_window_ui.listWidget_main_title.clear()
        for i in self.checkMovies():
            self.main_window_ui.listWidget_main_title.addItem(i)
            arr.append(i)

    def changetime(self, item):
        print(item.text())
        self.time1 = item.text()

    def open_MovieInfoWindow(self):
        if not self.movie:
            return QtWidgets.QMessageBox.warning(self.login_window, "Error", "Please choose movie.")
        self.MovieInfoWindow = QtWidgets.QMainWindow()
        self.MovieInfoWindow_ui = Ui_info()
        self.MovieInfoWindow_ui.setupUi(self.MovieInfoWindow)
        self.MovieInfoWindow.setMaximumSize(655, 580)
        self.MovieInfoWindow.show()
        title = str(self.movie)
        time = str(self.time1)
        if time != 'None':
            url = 'https://zarylbek.pythonanywhere.com/get_seatsInDict'
            getSeats_try = {'title':title, 'time':time}
            response = requests.get(url, getSeats_try)
            if response.status_code == 200:
                self.MovieInfoWindow_ui.label_empty_movie_name.setText(title + ', ' + time)
                response = response.json()
                self.MovieInfoWindow_ui.label_empty_free_seats.setText(str(len([i for i,k in response.items() if not k])))
                self.MovieInfoWindow_ui.label_empty_session.setText('1')
                for i,k in response.items():
                    if k:
                        label = i + ', ' + k + ', ' + title
                        self.MovieInfoWindow_ui.listWidget_to_show_people.addItem(label)
                self.MovieInfoWindow_ui.listWidget_to_show_people.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        else: 
            url = 'https://zarylbek.pythonanywhere.com/get_seatsAll'
            getSeats_try = {'title':title}
            response = requests.get(url, getSeats_try)
            if response.status_code == 200:
                self.MovieInfoWindow_ui.label_empty_movie_name.setText(title)
                response = response.json()
                self.MovieInfoWindow_ui.label_empty_free_seats.setText(str(sum(1 for i,k in response.items() for j,o in k.items() if not o)))
                self.MovieInfoWindow_ui.label_empty_session.setText(str(len(response)))
                for i,k in response.items():
                    for j,o in k.items():
                        if o:
                            label = j + ', ' + o + ', ' + title + ', ' + i
                            self.MovieInfoWindow_ui.listWidget_to_show_people.addItem(label)

        print(response)

    def open_UserHistoryWindow(self):
        self.UserHistory_window = QtWidgets.QMainWindow()
        self.UserHistory_ui = Ui_user_history()
        self.UserHistory_window.setMaximumSize(655, 580)
        self.UserHistory_ui.setupUi(self.UserHistory_window)
        self.UserHistory_window.show()
        url = 'https://zarylbek.pythonanywhere.com/get_infoClient'
        response = requests.get(url, params = {'client': me[0]})
        if response.status_code == 200:
            response = response.json()
            self.UserHistory_ui.label_user_history.setText(me[0] + "'s" + ' ' + 'history')
            for i,k in response.items():
                for i1, k1 in k.items():
                        for i2 in k1:
                            self.UserHistory_ui.listWidget_movie.addItem(i)
                            self.UserHistory_ui.listWidget_time.addItem(i1)
                            self.UserHistory_ui.listWidget_seat.addItem(i2)
            print(response)
        print(response)

    def open_buyseatswindow(self):
        if self.movie and self.time1:
            pass
        else:
            return QtWidgets.QMessageBox.warning(self.main_window, "Error", "Choose movie and schedule for it")
        self.buy_window = QtWidgets.QMainWindow()
        self.buy_window_ui = Ui_seats()
        self.buy_window_ui.setupUi(self.buy_window)
        self.buy_window.setMaximumSize(655, 580)
        self.buy_window.show()
        self.dict = {f"{letter}{number}":False for letter in "abcdf" for number in range(1, 8)}
        for i,k in self.checkSeats().items():
            if k and k != me[0]:
                button_name = f'pushButton_{i}'
                button = getattr(self.buy_window_ui, button_name, None)
                button.setStyleSheet("QPushButton { background-color: black; }")
                button.setEnabled(False)
                self.dict[i] = True
            elif k and k == me[0]:
                button_name = f'pushButton_{i}'
                button = getattr(self.buy_window_ui, button_name, None)
                button.setStyleSheet("QPushButton { background-color: red; }")
                self.dict[i] = True

        for i in 'abcdf':
            for k in range(1, 8):
                v = i + str(k)
                print(v)
                button = getattr(self.buy_window_ui, f'pushButton_{v}', None)
                button.clicked.connect(self.create_fun(v))
                
    def create_fun(self, v):
        def button():
            but = getattr(self.buy_window_ui, f'pushButton_{v}', None)
            if not self.dict[v]:
                url = 'https://zarylbek.pythonanywhere.com/bookSeat'
                book_try = {'client':me[0], 'seat':v, 'title': self.movie, 'time':self.time1}
                response = requests.get(url, params= book_try)
                if response.text == 'Done':
                    but.setStyleSheet("QPushButton { background-color: red; }")
                    print('good')
                    self.dict[v] = True
                else:
                    print('bad')
            else:
                url = 'https://zarylbek.pythonanywhere.com/removeseat'
                book_try = {'seat':v, 'title': self.movie, 'time':self.time1}
                response = requests.get(url, params= book_try)
                if response.text == 'Done':
                    but.setStyleSheet("QPushButton { background-color: white; }")
                    print('good')
                    self.dict[v] = False
                else:
                    print('bad')
        return button
    
    def checkSeats(self):
        title = str(self.movie)
        time = str(self.time1)
        url = 'https://zarylbek.pythonanywhere.com/get_seatsInDict'
        getSeats_try = {'title':title, 'time':time}
        response = requests.get(url, params = getSeats_try)
        if response.status_code == 200:
            response_data = response.json()  # Декодируем JSON из ответа
            print(response_data)
            return response_data
        else:
            print(f"Ошибка {response.status_code}: {response.text}")
        print(response)

    def log_out(self):
        try:
            self.admin_window.close()
        except:
            pass
        me.clear()
        self.main_window.close()
        if not hasattr(self, 'login_window') or not self.login_window.isVisible(): # на крайний случай это условие
            self.login_window = QtWidgets.QMainWindow()
            self.login_ui = Ui_loginpage()
            self.login_window.setMaximumSize(655, 580)
            self.login_ui.setupUi(self.login_window)
            self.login_ui.pushButtonlogin.clicked.connect(self.login)
            self.login_ui.register_2.linkActivated.connect(self.open_registerwindow)
        self.login_window.show()
        self.movie = None
        self.time1 = None

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    sys.exit(app.exec_())
    