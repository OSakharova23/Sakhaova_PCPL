import os
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit, QPlainTextEdit, QComboBox, QSpinBox
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QDialogButtonBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import QUrl
from random import choice
import sys


def except_hook(cls, exception, traceback): #функция для нормального отображения ошибки кода
    sys.__excepthook__(cls, exception, traceback)


class Ex(QWidget): #основное окно
    def __init__(self):
        super().__init__()
        self.programs()

    def programs(self):
        #создание окна игры
        self.setWindowTitle('Monopoly for you')                #название окна
        self.setGeometry(200, 200, 1408, 790)                  #размер и расположение окна
        self.setMaximumSize(1408, 790)                         #не позволяет расширять окно
        self.setMinimumSize(1408, 790)                         #не позволяет уменьшать окно


        with open('данные.csv', 'r', encoding='windows-1251') as file:
            self.data = [line.strip().split(';') for line in file.readlines()]

        #фон заставки
        self.pix_background = QPixmap('картинки/monopoly_1.jfif')                  #открытие картинки с заставкой
        self.image_background = QLabel(self)                                       #создание виджета
        self.image_background.move(0, 0)                                           #расположение виджета
        self.image_background.setPixmap(self.pix_background)                       #запись картинки на виджет

        #картинка игрового поля
        self.pix_game = QPixmap('картинки/поле.png')                               #открытие картинки с полем
        self.image_game = QLabel(self)                                             #создание виджета
        self.image_game.move(300, 20)                                              #расположение виджета
        self.image_game.setPixmap(self.pix_game)                                   #запись картинки на виджет
        self.image_game.hide()                                                     #скрытие картинки

        #надпись "Monopoly for you"
        self.title = QLabel('<h1 style="color: rgb(255, 255, 255);">Monopoly for you</h1>', self)#создание, текст, стиль
        self.title.move(170, 150)                                                                #расположение виджета
        self.title.setFont(QFont('Arial', 25))                                                   #размер и шрифт текста

        #кнопка "Новая игра"
        self.game = QPushButton('Новая игра', self)                                 #создание, название виджета
        self.game.setFont(QFont('Times New Roman', 30))                             #шрифт и размер текста
        self.game.resize(500, 100)                                                  #размер виджета
        self.game.move(450, 400)                                                    #расположение виджета
        self.game.clicked.connect(self.next)                                        #подключение виджета функции next

        #кнопка "Продолжить"
        self.old_game = QPushButton('Продолжить', self)                          #создание, название виджета
        self.old_game.setFont(QFont('Times New Roman', 30))                      #шрифт и размер текста
        self.old_game.resize(500, 100)                                           #размер виджета
        self.old_game.move(450, 525)                                             #расположение виджета
        self.old_game.setEnabled(False)                                          #отключение возможности нажимать кнопку
        self.old_game.clicked.connect(self.oldgame)                              #подключение виджета функции oldgame

        #кнопка "Сохранить и выйти"
        self.ext = QPushButton('Сохранить и выйти', self)                           #создание, название виджета
        self.ext.setFont(QFont('Times New Roman', 10))                              #шрифт и размер текста
        self.ext.resize(200, 25)                                                    #размер виджета
        self.ext.move(10, 10)                                                       #расположение виджета
        self.ext.hide()                                                             #скрытие виджета
        self.ext.clicked.connect(self.exit)                                         #подключение виджета функции exit

        #кнопка "Готово"
        self.start = QPushButton('Готово', self)                                    #создание, название виджета
        self.start.setFont(QFont('Times New Roman', 10))                            #шрифт и размер текста
        self.start.resize(250, 75)                                                  #размер виджета
        self.start.move(575, 690)                                                   #расположение виджета
        self.start.hide()                                                           #скрытие виджета
        self.start.clicked.connect(self.ready)                                      #подключение виджета функции ready

        #надпись "Игрок 1, введите имя:"
        self.player1 = QLabel('<h1 style="color: rgb(255, 255, 255);">Игрок 1, введите имя:  </h1>', self)
        self.player1.setFont(QFont('Times New Roman', 10))                                        #шрифт и размер текста
        self.player1.move(150, 50)                                                                #расположение виджета
        self.player1.hide()                                                                       #скрытие виджета

        #надпись "Игрок 2, введите имя:"
        self.player2 = QLabel('<h1 style="color: rgb(255, 255, 255);">Игрок 2, введите имя:  </h1>', self)
        self.player2.setFont(QFont('Times New Roman', 10))                                        #шрифт и размер текста
        self.player2.move(850, 50)                                                                #расположение виджета
        self.player2.hide()                                                                       #скрытие виджета

        #кнопка ">"
        self.next1 = QPushButton('>', self)                                        #создание, название виджета
        self.next1.setFont(QFont('Times New Roman', 10))                           #шрифт и размер текста
        self.next1.resize(50, 50)                                                  #размер виджета
        self.next1.move(550, 450)                                                  #расположение виджета
        self.next1.clicked.connect(self.picture_selection_player1)                 #подключение виджета функции
        self.next1.hide()                                                          #скрытие виджета

        #кнопка ">"
        self.next2 = QPushButton('>', self)                                        #создание, название виджета
        self.next2.setFont(QFont('Times New Roman', 10))                           #шрифт и размер текста
        self.next2.resize(50, 50)                                                  #размер виджета
        self.next2.move(1250, 450)                                                 #расположение виджета
        self.next2.clicked.connect(self.picture_selection_player2)                 #подключение виджета функции
        self.next2.hide()                                                          #скрытие виджета

        #кнопка "<"
        self.previous1 = QPushButton('<', self)                                    #создание, название виджета
        self.previous1.setFont(QFont('Times New Roman', 10))                       #шрифт и размер текста
        self.previous1.resize(50, 50)                                              #размер виджета
        self.previous1.move(50, 450)                                               #расположение виджета
        self.previous1.clicked.connect(self.picture_selection_player1)             #подключение виджета функции
        self.previous1.hide()                                                      #скрытие виджета

        #кнопка "<"
        self.previous2 = QPushButton('<', self)                                    #создание, название виджета
        self.previous2.setFont(QFont('Times New Roman', 10))                       #шрифт и размер текста
        self.previous2.resize(50, 50)                                              #размер виджета
        self.previous2.move(750, 450)                                              #расположение виджета
        self.previous2.clicked.connect(self.picture_selection_player2)             #подключение виджета функции
        self.previous2.hide()                                                      #скрытие виджета

        #надпись "Выберите фишку:"
        self.choice1 = QLabel('<h1 style="color: rgb(255, 255, 255);">Выберите фишку:  </h1>', self)
        self.choice1.setFont(QFont('Times New Roman', 10))                                        #шрифт и размер текста
        self.choice1.move(150, 250)                                                               #расположение виджета
        self.choice1.hide()                                                                       #скрытие виджета

        #надпись "Выберите фишку:"
        self.choice2 = QLabel('<h1 style="color: rgb(255, 255, 255);">Выберите фишку:  </h1>', self)
        self.choice2.setFont(QFont('Times New Roman', 10))                                        #шрифт и размер текста
        self.choice2.move(850, 250)                                                               #расположение виджета
        self.choice2.hide()                                                                       #скрытие виджета

        #строка для ввода имени 1 игрока
        self.name_1 = QLineEdit(self)                                              #создание виджета
        self.name_1.resize(400, 50)                                                #размер виджета
        self.name_1.move(150, 125)                                                 #расположение виджета
        self.name_1.setFont(QFont('Times New Roman', 10))                          #шрифт и размер текста
        self.name_1.hide()                                                         #скрытие виджета

        #строка для ввода имени 2 игрока
        self.name_2 = QLineEdit(self)                                              #создание виджета
        self.name_2.resize(400, 50)                                                #размер виджета
        self.name_2.move(850, 125)                                                 #расположение виджета
        self.name_2.setFont(QFont('Times New Roman', 10))                          #шрифт и размер текста
        self.name_2.hide()                                                         #скрытие виджета

        #картинка с фишкой 1 игрока
        self.pix1 = QPixmap('картинки/red.png')                                   #открытие картинки
        self.image1 = QLabel(self)                                                #создание виджета
        self.image1.move(200, 350)                                                #расположение виджета
        self.image1.setPixmap(self.pix1)                                          #подключение картинки на виджет
        self.image1.hide()                                                        #скрытие виджета

        self.skin1 = 0

        # строка для ввода имени 1 игрока
        self.pix2 = QPixmap('картинки/red.png')                                   #открытие картинки
        self.image2 = QLabel(self)                                                #создание виджета
        self.image2.move(950, 350)                                                #расположение виджета
        self.image2.setPixmap(self.pix2)                                          #подключение картинки на виджет
        self.image2.hide()                                                        #скрытие виджета

        self.skin2 = 0

        self.music = QMediaPlayer()
        self.playAudioFile()

        #надпись "Введите разные имена"
        self.identical = QLabel('<h1 style="color: rgb(255, 255, 255);">Введите разные имена</h1>', self)
        self.identical.setFont(QFont('Times New Roman', 10))                                      #шрифт и размер текста
        self.identical.move(515, 625)                                                             #расположение виджета
        self.identical.hide()  # скрытие виджета

        #надпись "Имя не должно быть длинее 10"
        self.very_long1 = QLabel('<h1 style="color: rgb(255, 255, 255);">Имя не должно быть длинее 10</h1>', self)
        self.very_long1.setFont(QFont('Times New Roman', 10))                                     #шрифт и размер текста
        self.very_long1.move(150, 200)                                                            #расположение виджета
        self.very_long1.hide()                                                                    #скрытие виджета

        #надпись "Выберите разные фишки"
        self.same_color = QLabel('<h1 style="color: rgb(255, 255, 255);">Выберите разные фишки</h1>', self)
        self.same_color.setFont(QFont('Times New Roman', 10))                                     #шрифт и размер текста
        self.same_color.move(500, 575)                                                            #расположение виджета
        self.same_color.hide()                                                                    #скрытие виджета

        #надпись "Имя не должно быть длинее 10"
        self.very_long2 = QLabel('<h1 style="color: rgb(255, 255, 255);">Имя не должно быть длинее 10</h1>', self)
        self.very_long2.setFont(QFont('Times New Roman', 10))                                     #шрифт и размер текста
        self.very_long2.move(850, 200)                                                            #расположение виджета
        self.very_long2.hide()                                                                    #скрытие виджета

        #надпись "Введите имя!"
        self.empty_line2 = QLabel('<h1 style="color: rgb(255, 255, 255);">Введите имя!</h1>', self)
        self.empty_line2.setFont(QFont('Times New Roman', 10))                                    #шрифт и размер текста
        self.empty_line2.move(900, 200)                                                           #расположение виджета
        self.empty_line2.hide()                                                                   #скрытие виджета

        #надпись "Введите имя!"
        self.empty_line1 = QLabel('<h1 style="color: rgb(255, 255, 255);">Введите имя!</h1>', self)
        self.empty_line1.setFont(QFont('Times New Roman', 10))                                    #шрифт и размер текста
        self.empty_line1.move(200, 200)                                                           #расположение виджета
        self.empty_line1.hide()                                                                   #скрытие виджета

        #показывает что выпало на кубике
        self.kubik_hod = QLabel('<h1 style="color: rgb(255, 255, 255);">  </h1>', self)          #создание, стиль текста
        self.kubik_hod.setFont(QFont('Times New Roman', 40))                                     #шрифт и размер текста
        self.kubik_hod.move(600, 300)                                                            #расположение виджета
        self.kubik_hod.hide()                                                                    #скрытие виджета

        #надпись "Ход игрока {имя}"
        self.hod_1 = QLabel('<h1 style="color: rgb(0, 0, 0);"> </h1>', self)                     #создание, стиль текста
        self.hod_1.setFont(QFont('Times New Roman', 10))                                         #шрифт и размер текста
        self.hod_1.move(530, 225)                                                                #расположение виджета
        self.hod_1.hide()                                                                        #скрытие виджета

        #надпись "Ход игрока {имя}"
        self.hod_2 = QLabel('<h1 style="color: rgb(0, 0, 0);"> </h1>', self)                     #создание, стиль текста
        self.hod_2.setFont(QFont('Times New Roman', 10))                                         #шрифт и размер текста
        self.hod_2.move(530, 225)                                                                #расположение виджета
        self.hod_2.hide()                                                                        #скрытие виджета

        #кнопка "Кинуть кубик"
        self.kubik = QPushButton('Кинуть кубик', self)                        #создание, название виджета
        self.kubik.setFont(QFont('Times New Roman', 10))                      #шрифт и размер текста
        self.kubik.resize(300, 50)                                            #размер виджета
        self.kubik.move(530, 270)                                             #расположение виджета
        self.kubik.hide()                                                     #скрытие виджета
        self.kubik.clicked.connect(self.roll_the_dice)                        #подключение виджета функции roll_the_dice

        #кнопка "Завершить игру"
        self.end = QPushButton('Завершить игру', self)                          #создание, название виджета
        self.end.setFont(QFont('Times New Roman', 10))                          #шрифт и размер текста
        self.end.resize(200, 25)                                                #размер виджета
        self.end.move(1205, 760)                                                #расположение виджета
        self.end.hide()                                                         #скрытие виджета
        self.end.clicked.connect(self.the_end)                                  #подключение виджета функции the_end

        #надпись "Игрок {имя}"
        self.name_player1 = QLabel('<h1 style="color: rgb(0, 0, 0);">Игрок  </h1>', self)        #создание, текст, стиль
        self.name_player1.resize(300, 50)                                                        #размер виджета
        self.name_player1.move(50, 50)                                                           #расположение виджета
        self.name_player1.hide()                                                                 #скрытие виджета

        #надпись, показывающая количество тугриков
        self.bank1 = QLabel('<h1 style="color: rgb(0, 0, 0);">  </h1>', self)                    #создание, текст, стиль
        self.bank1.move(50, 150)                                                                 #расположение виджета
        self.bank1.hide()                                                                        #скрытие виджета

        #надпись, показывающая количество тугриков
        self.bank2 = QLabel('<h1 style="color: rgb(0, 0, 0);">  </h1>', self)
        self.bank2.move(1100, 150)                                                                 #расположение виджета
        self.bank2.hide()                                                                          #скрытие виджета

        #надпись "Игрок {имя}"
        self.name_player2 = QLabel('<h1 style="color: rgb(0, 0, 0);">Игрок  </h1>', self)        #создание, текст, стиль
        self.name_player2.resize(300, 50)                                                        #размер виджета
        self.name_player2.move(1100, 50)                                                         #расположение виджета
        self.name_player2.hide()                                                                 #скрытие виджета

        #надпись "В наличии:"
        self.in_stock1 = QLabel('<h1 style="color: rgb(0, 0, 0);">  </h1>', self)                #создание, стиль текста
        self.in_stock1.setText('В наличии: ')                                                    #текст виджета
        self.in_stock1.setFont(QFont('Times New Roman', 10))                                     #шрифт и размер текста
        self.in_stock1.move(50, 250)                                                             #расположение виджета
        self.in_stock1.hide()                                                                    #скрытие виджета

        #строки для ввода текста, где отображается количество купленных улиц 1 игрока
        self.text_1 = QPlainTextEdit(self)                                      #создание виджета
        self.text_1.setReadOnly(True)                                           #отключение возможности менять текст
        self.text_1.resize(200, 450)                                            #размер виджета
        self.text_1.move(50, 300)                                               #расположение виджета
        self.text_1.hide()                                                      #скрытие виджета

        #строки для ввода текста, где отображается количество купленных улиц 2 игрока
        self.text_2 = QPlainTextEdit(self)                                     #создание виджета
        self.text_2.setReadOnly(True)                                          #отключение возможности менять текст
        self.text_2.resize(200, 450)                                           #размер виджета
        self.text_2.move(1110, 300)                                            #расположение виджета
        self.text_2.setFont(QFont('Times New Roman', 10))                      #шрифт и размер текста
        self.text_2.hide()                                                     #скрытие виджета

        #надпись "В наличии:"
        self.in_stock2 = QLabel('<h1 style="color: rgb(0, 0, 0);">  </h1>', self)                #создание, стиль текста
        self.in_stock2.setText('В наличии: ')                                                    #текст виджета
        self.in_stock2.setFont(QFont('Times New Roman', 10))                                     #шрифт и размер текста
        self.in_stock2.move(1100, 250)                                                           #расположение виджета
        self.in_stock2.hide()                                                                    #скрытие виджета

        #кнопка "⋮" с правилами
        self.regulations_button = QPushButton('⋮', self)                        #создание, название виджета
        self.regulations_button.setFont(QFont('Times New Roman', 20))           #шрифт и размер текста
        self.regulations_button.resize(50, 50)                                  #размер виджета
        self.regulations_button.move(1350, 10)                                  #расположение виджета
        self.regulations_button.clicked.connect(self.open_form)                 #подключение виджета функции open_form

        #кнопка "🏷️" с таблицей цен
        self.price_button = QPushButton('🏷️', self)                            #создание, название виджета
        self.price_button.setFont(QFont('Times New Roman', 15))                #шрифт и размер текста
        self.price_button.resize(50, 50)                                       #размер виджета
        self.price_button.move(1250, 10)                                       #расположение виджета
        self.price_button.clicked.connect(self.open_form)                      #подключение виджета функции open_form

        #кнопка "⚙" с настройкой звука
        self.settings_button = QPushButton('⚙', self)                         #создание, название виджета
        self.settings_button.setFont(QFont('Times New Roman', 10))             #шрифт и размер текста
        self.settings_button.resize(50, 50)                                    #размер виджета
        self.settings_button.move(1300, 10)                                    #расположение виджета
        self.settings_button.clicked.connect(self.open_form)                   #подключение виджета функции open_form

        #кнопка "Оплатить {цена}"
        self.fine_button = QPushButton(self)                                    #создание виджета
        self.fine_button.setFont(QFont('Times New Roman', 10))                  #шрифт и размер текста
        self.fine_button.resize(300, 50)                                        #размер виджета
        self.fine_button.move(530, 450)                                         #расположение виджета
        self.fine_button.hide()                                                 #скрытие виджета
        self.fine_button.clicked.connect(self.payment)                          #подключение виджета функции payment

        #кнопка "Купить"
        self.buy = QPushButton('Купить', self)                                  #создание, название виджета
        self.buy.setFont(QFont('Times New Roman', 10))                          #шрифт и размер текста
        self.buy.resize(145, 50)                                                #размер виджета
        self.buy.move(530, 450)                                                 #расположение виджета
        self.buy.clicked.connect(self.payment)                                  #подключение виджета функции payment
        self.buy.hide()                                                         #скрытие виджета

        #кнопка "Оставить"
        self.dont_buy = QPushButton('Оставить', self)                           #создание, название виджета
        self.dont_buy.setFont(QFont('Times New Roman', 10))                     #шрифт и размер текста
        self.dont_buy.resize(145, 50)                                           #размер виджета
        self.dont_buy.move(685, 450)                                            #расположение виджета
        self.dont_buy.clicked.connect(self.next_hod)                            #подключение виджета функции next_hod
        self.dont_buy.hide()                                                    #скрытие виджета

        #строки для ввода текста, где отображается куда вы попали
        self.street = QPlainTextEdit('Вы попали на улицу вторая коричневая. она стоит 1000', self)#создание, название
        self.street.setFont(QFont('Times New Roman', 10))                                         #шрифт и размер текста
        self.street.resize(365, 80)                                                               #размер виджета
        self.street.move(500, 540)                                                                #расположение виджета
        self.street.setReadOnly(True)                                                             #нельзя менять текст
        self.street.hide()                                                                        #скрытие виджета

        #кнопка "Обменять"
        self.change_street = QPushButton('Обменять улицы', self)                 #создание, название виджета
        self.change_street.setFont(QFont('Times New Roman', 8))                 #шрифт и размер текста
        self.change_street.resize(300, 50)                                       #размер виджета
        self.change_street.move(530, 170)                                        #расположение виджета
        self.change_street.clicked.connect(self.open_form)                       #подключение виджета функции open_form
        self.change_street.hide()                                                #скрытие виджета

        self.regulations_form = Regulation(self, "Правила")                      #создание окна с правилами
        self.regulations_form.hide()                                             #скрытие виджета

        self.settings_form = Sound_settings(self, "Настройки")                   #создание окна с настройкой звука
        self.settings_form.hide()                                                #скрытие виджета

        self.price_form = Price_list(self, "Цены")                               #создание окна с таблицей цен
        self.price_form.hide()                                                   #скрытие виджета

    def open_form(self): #функция для открывания окон
        # открывает окно с настройкой звука
        if self.sender().text() == '⚙':
            if self.settings_form.isHidden():
                self.settings_form.show()
            else:
                self.settings_form.hide()
        # открывает окно с правилами
        if self.sender().text() == '⋮':
            if self.regulations_form.isHidden():
                self.regulations_form.show()
            else:
                self.regulations_form.hide()
        # открывает окно с таблицей цен
        if self.sender().text() == '🏷️':
            if self.price_form.isHidden():
                self.price_form.show()
            else:
                self.price_form.hide()
        # создаёт диалоговое окно и передаёт переменные
        if self.sender().text() == 'Обменять улицы':
            global estate1, estate2                                                    #создание глобальных переменных
            estate1 = list(map(lambda x: x[:-9] if 'вокзал' not in x else x, self.estate_1)) #переменная список улиц 1
            estate2 = list(map(lambda x: x[:-9] if 'вокзал' not in x else x, self.estate_2)) #переменная список улиц 2

            global n1, n2, mon1, mon2                                                  #создание глобальных переменных
            n1 = self.name_1.text()                                                    #переменная с именем 1 игрока
            n2 = self.name_2.text()                                                    #переменная с именем 2 игрока
            mon1 = self.money_1                                                        #переменная с кол-вом денег 1
            mon2 = self.money_2                                                        #переменная с кол-вом денег 2

            self.exchange_form = Exchange_street()                                     #создание окна для обмена улицами
            self.exchange_form.show()                                                  #видимость окна

    def next(self): #функция появления виджетов для авторизации при новой игре
        #основные свойства у играков
        self.money_1 = 1000         #кол-во денег 1
        self.money_2 = 1000         #кол-во денег 2
        self.estate_1 = []          #список улиц 1
        self.estate_2 = []          #список улиц 2
        self.place_1 = 0            #номер клетки поля фишки 1
        self.place_2 = 0            #номер клетки поля фишки 2
        self.count = 1              #чей ход

        with open('данные.csv', 'r', encoding='windows-1251') as file:
            self.data = [line.strip().split(';') for line in file.readlines()] #список, содержащий данные улиц

        # стирание данных если игра уже была
        self.name_1.clear()
        self.name_2.clear()

        #виджеты, показывающие кол-во денег у играков, картинку фишки, кол-во улиц
        self.bank1.setText('Банк: ' + str(self.money_1))                        #надпись о кол-ве денег 1
        self.bank1.setFont(QFont('Times New Roman', 20))                        #шрифт, размер текста
        self.bank2.setText('Банк: ' + str(self.money_2))                        #надпись о кол-ве денег 2
        self.bank2.setFont(QFont('Times New Roman', 20))                        #шрифт, размер текста

        self.pix1 = QPixmap('картинки/red.png')                                 #нахождение картинки
        self.image1.setPixmap(self.pix1)                                        #начальная картинка с фишкой
        self.image2.setPixmap(self.pix1)                                        #начальная картинка с фишкой

        spisok1 = sorted(list(filter(lambda x: len(x) >= 9, self.estate_1)), key=lambda x: (x[7], x[3])) \
                 + sorted(list(filter(lambda x: len(x) < 9, self.estate_1)))   #сортировка списка улиц 1
        self.text_1.setPlainText('\n'.join(spisok1))                           #текст с улицами
        self.text_1.setFont(QFont('Times New Roman', 12))                      #шрифт, размер текста
        spisok2 = sorted(list(filter(lambda x: len(x) >= 9, self.estate_2)), key=lambda x: (x[7], x[3])) \
                  + sorted(list(filter(lambda x: len(x) < 9, self.estate_2)))  #сортировка списка улиц 2
        self.text_2.setPlainText('\n'.join(spisok2))                           #текст с улицами
        self.text_2.setFont(QFont('Times New Roman', 12))                      #шрифт, размер текста

        a = [self.player1, self.player2, self.name_1, self.name_2, self.start, self.choice1, self.choice2, self.next1,
             self.next2, self.previous1, self.previous2, self.image1, self.image2]  #список виджетов для появления
        self.title.hide()                                                           #скрытие виджета
        self.game.hide()                                                            #скрытие виджета
        self.old_game.hide()                                                        #скрытие виджета
        for i in a:                                                                 #появление виджетов по списку
            i.show()

    def picture_selection_player1(self): #функция, выбора цвета фишки 1 игрока
        self.name_pichure = ['red.png', 'yellow.png', 'green.png', 'blue.png']          #список с названиями картинок
        # при нажатии на > имя картинки 1 игрока сменяется на следующее
        if self.sender().text() == '>':
            if self.skin1 == 3:
                self.skin1 = 0
            else:
                self.skin1 += 1
        # при нажатии на < имя картинки 1 игрока сменяется на предыдущее
        else:
            if self.skin1 == 0:
                self.skin1 = 3
            else:
                self.skin1 -= 1
        # меняет картинку с фишкой 1 игрока на другую
        self.pix1 = QPixmap('картинки/' + self.name_pichure[self.skin1])      #открытие картинки
        self.image1.setPixmap(self.pix1)                                               #запись картинки на виджет

    def picture_selection_player2(self): #функция, выбора цвета фишки 2 игрока
        self.name_pichure = ['red.png', 'yellow.png', 'green.png', 'blue.png']         #список с названиями картинок
        # при нажатии на > имя картинки 2 игрока сменяется на следующее
        if self.sender().text() == '>':
            if self.skin2 == 3:
                self.skin2 = 0
            else:
                self.skin2 += 1
        # при нажатии на < имя картинки 2 игрока сменяется на предыдущее
        else:
            if self.skin2 == 0:
                self.skin2 = 3
            else:
                self.skin2 -= 1
        #меняет картинку с фишкой 2 игрока на другую
        self.pix2 = QPixmap('картинки/' + self.name_pichure[self.skin2])      #открытие картинки
        self.image2.setPixmap(self.pix2)                                               #запись картинки на виджет

    def ready(self): #функция, показывающая "страницу" с основым содержанием игры
        # если вместо имени 1 игрока ничего не введено, то появляется надпись "Введите имя"
        if self.name_1.text() == '':
            self.empty_line1.show()
        else:#если имя 1 игрока введено, а надпись видна, то надпись "Введите имя" исчезает
            if self.empty_line1.isHidden() is False:
                self.empty_line1.hide()

        # если вместо имени 2 игрока ничего не введено, то появляется надпись "Введите имя"
        if self.name_2.text() == '':
            self.empty_line2.show()
        else:#если имя 2 игрока введено, а надпись видна, то надпись "Введите имя" исчезает
            if self.empty_line2.isHidden() is False:
                self.empty_line2.hide()

        # если длина имени 1 игрока > 10, появляется надпись "Имя не должно быть длинее 10"
        if len(self.name_1.text()) > 10:
            self.very_long1.show()
        else:#если длина имени 1 игрока <= 10, а надпись виджета very_long1 видна, то надпись исчезает
            if self.very_long1.isHidden() is False:
                self.very_long1.hide()

        # если длина имени 2 игрока > 10, появляется надпись "Имя не должно быть длинее 10"
        if len(self.name_2.text()) > 10:
            self.very_long2.show()
        else:#если длина имени 2 игрока <= 10, а надпись виджета very_long2 видна, то надпись исчезает
            if self.very_long2.isHidden() is False:
                self.very_long2.hide()

        #если введенные имена игроков совпадают появляется надпись "Введите разные имена"
        if self.name_1.text() == self.name_2.text() and self.name_1.text() != '' and self.name_2.text() != '':
            self.identical.show()
        else: #если имена игроков разные, а надпись "Введите разные имена" видна, то надпись исчезает
            if self.identical.isHidden() is False:
                self.identical.hide()

        # если цвет фишек игроков совпадает появляется надпись "Выберите разные фишки"
        if self.skin1 == self.skin2:
            self.same_color.show()
        else: #если цвет фишек разный, а надпись "Выберите разные фишки" видна, то надпись исчезает
            if self.same_color.isHidden() is False:
                self.same_color.hide()

        #если все условия выполнены и авторизация успешна появляется основные виджеты и игра начинается
        if self.identical.isHidden() and self.same_color.isHidden() and self.empty_line1.isHidden() \
                and self.empty_line2.isHidden() and self.very_long1.isHidden() and self.very_long2.isHidden():
            a = [self.player1, self.player2, self.name_1, self.name_2, self.start,
                 self.choice1, self.choice2,self.next1, self.next2, self.previous1, self.previous2,
                 self.image1, self.image2, self.image_background]             #список виджетов, которые должны исчезнуть
            for i in a:                                                       #виджеты перебираются и исчезают
                i.hide()
            b = [self.image_game, self.kubik, self.end, self.bank1, self.bank2, self.in_stock1, self.in_stock2,
                 self.text_1, self.text_2, self.change_street, self.ext]                #список виджетов, которые должны появится
            for i in b:                                                       #виджеты перебираются и появляются
                i.show()
            #надпись с именем игрока
            self.name_player1.setText('Игрок "' + str(self.name_1.text()) + '"')
            self.name_player1.setFont(QFont('Times New Roman', 20))
            self.name_player2.setText('Игрок "' + str(self.name_2.text()) + '"')
            self.name_player2.setFont(QFont('Times New Roman', 20))
            self.name_player1.show()
            self.name_player2.show()

            self.hod_1.setText('Ход игрока "' + str(self.name_1.text()) + '"')
            self.hod_2.setText('Ход игрока "' + str(self.name_2.text()) + '"')
            self.hod_1.show()


            self.pix_player1 = QPixmap('картинки/' + self.name_pichure[self.skin1])
            self.pix_player1 = self.pix_player1.scaledToWidth(60)
            self.image_player1 = QLabel(self)
            self.image_player1.move(300, 675)
            self.image_player1.setPixmap(self.pix_player1)
            self.image_player1.show()

            self.pix_player2 = QPixmap('картинки/' + self.name_pichure[self.skin2])
            self.pix_player2 = self.pix_player2.scaledToWidth(60)
            self.image_player2 = QLabel(self)
            self.image_player2.move(350, 675)
            self.image_player2.setPixmap(self.pix_player2)
            self.image_player2.show()

    def exit(self):  #функция выхода на начальный экран
        b = [self.image_game, self.kubik, self.end, self.bank1, self.bank2, self.in_stock1, self.in_stock2,
             self.text_1, self.text_2, self.change_street, self.name_player1, self.name_player2, self.image_player1,
             self.image_player2, self.ext, self.kubik_hod, self.street]  #список виджетов, которые должны исчезнуть
        for i in b:  #виджеты перебираются и исчезают
            i.hide()
        global how_walks #создание глобальной переменной с виджетом чей ход
        if self.hod_1.isHidden():
            how_walks = self.hod_2
        else:
            how_walks = self.hod_1
        how_walks.hide()                                                             #срытие виджета
        self.title.show()                                                            #появление виджета
        self.game.show()                                                             #появление виджета
        self.old_game.show()                                                         #появление виджета
        self.image_background.show()                                                 #появление виджета
        self.old_game.setEnabled(True)                                               #можно нажимать кнопку "Продолжить"

    def oldgame(self): #функция появления виджетов для продолжения игры
        b = [self.image_game, self.kubik, self.end, self.bank1, self.bank2, self.in_stock1, self.in_stock2,
             self.text_1, self.text_2, self.change_street, self.name_player1, self.name_player2, self.image_player1,
             self.image_player2, self.ext, how_walks]  #список виджетов, которые должны появится
        for i in b:  #виджеты перебираются и появляются
            i.show()
        self.title.hide()                                                             #срытие виджета
        self.game.hide()                                                              #срытие виджета
        self.old_game.hide()                                                          #срытие виджета
        self.image_background.hide()                                                  #срытие виджета

    def exchange(self):  #функция для передачи улиц от одного игррока другому
        #передача улицы 1-ого игрока
        if street1 == 'ничего': #если игрок не выбрал улицу ничего не происходит
            pass
        else:
            if 'вокзал' in street1: #передча вокзалов
                self.estate_1.remove(list(filter(lambda x: street1 in x, self.estate_1))[0])  #удаление из списка 1-ого
                self.estate_2.append(street1)                                                 #добовление в список 2-ого
                t = 'вокзал'
                c = list(filter(lambda x: x[12] == 'вокзал' and x[6] == '1', self.data))  # список своих вокзалов
                if len(c) > 1:
                    for i in range(len(c)):
                        # изменение данных о количестве воказалов игрока 1
                        self.data[self.data.index(list(filter(lambda x: x[12] == t and x[6] == '1', self.data))[i])][7]\
                            = str(len(c) - 1)
                # изменение статуса {кому принадлежит} у вокзала:
                self.data[self.data.index(list(filter(lambda x: x[1] == street1, self.data))[0])][6] = '2'
                b = list(filter(lambda x: x[12] == 'вокзал' and x[6] == '2', self.data))   # список чужих вокзалов
                for i in range(len(b)):
                    # изменение данных о количестве воказалов игрока 2
                    self.data[self.data.index(list(filter(lambda x: x[12] == t and x[6] == '2', self.data))[i])][7] \
                        = str(len(b))
            else: #передча улиц
                t = self.data[self.data.index(list(filter(lambda x: x[1] == street1, self.data))[0])][12] #тип улицы
                c = list(filter(lambda x: x[12] == t and x[6] == '1', self.data))   #список его улиц того же типа
                if len(c) == len(list(filter(lambda x: x[12] == t, self.data))): #если собранны все улицы одного типа
                    for i in range(len(c)):
                        # изменение данных о количестве домов улиц того типа
                        self.data[self.data.index(list(filter(lambda x: x[12] == t, self.data))[i])][7] = '1'
                    # изменение статуса {кому принадлежит} у улицы:
                    self.data[self.data.index(list(filter(lambda x: x[1] == street1, self.data))[0])][6] = '2'
                    self.estate_1.remove(list(filter(lambda x: street1 in x, self.estate_1))[0]) #удаление из списка 1
                    self.estate_2.append(street1 + ': домов 0')                                  #добовление в список 2
                else: #если не собранны все улицы одного типа
                    # изменение статуса {кому принадлежит} у улицы:
                    self.data[self.data.index(list(filter(lambda x: x[1] == street1, self.data))[0])][6] = '2'
                    self.estate_1.remove(list(filter(lambda x: street1 in x, self.estate_1))[0]) #удаление из списка 1
                    self.estate_2.append(street1 + ': домов 0')                                  #добовление в список 2

        #передача улицы 2-ого игрока
        if street2 == 'ничего': #если игрок не выбрал улицу ничего не происходит
            pass
        else:
            if 'вокзал' in street2: #передча вокзалов
                self.estate_2.remove(list(filter(lambda x: street2 in x, self.estate_2))[0])  #удаление из списка 2-ого
                self.estate_1.append(street2)                                                 #добовление в список 1-ого
                t = 'вокзал'
                c = list(filter(lambda x: x[12] == 'вокзал' and x[6] == '2', self.data))      #список своих вокзалов
                if len(c) > 1: #если своих вокзалов > 1
                    for i in range(len(c)):
                        # изменение данных о количестве воказалов игрока 2
                        self.data[self.data.index(list(filter(lambda x: x[12] == t and x[6] == '2', self.data))[i])][7]\
                            = str(len(c) - 1)
                # изменение статуса {кому принадлежит} у вокзала:
                self.data[self.data.index(list(filter(lambda x: x[1] == street2, self.data))[0])][6] = '1'
                b = list(filter(lambda x: x[12] == 'вокзал' and x[6] == '1', self.data))      #список чужих вокзалов
                for i in range(len(b)):
                    # изменение данных о количестве воказалов игрока 1
                    self.data[self.data.index(list(filter(lambda x: x[12] == t and x[6] == '1', self.data))[i])][7]\
                        = str(len(b))
            else: #передча улиц
                t = self.data[self.data.index(list(filter(lambda x: x[1] == street2, self.data))[0])][12] #тип улицы
                c = list(filter(lambda x: x[12] == t and x[6] == '2', self.data))  #список его улиц того же типа
                if len(c) == len(list(filter(lambda x: x[12] == t, self.data))): #если собранны все улицы одного типа
                    for i in range(len(c)):
                        # изменение данных о количестве домов улиц того типа
                        self.data[self.data.index(list(filter(lambda x: x[12] == t, self.data))[i])][7] = '1'
                    # изменение статуса {кому принадлежит} у улицы:
                    self.data[self.data.index(list(filter(lambda x: x[1] == street2, self.data))[0])][6] = '1'
                    self.estate_2.remove(list(filter(lambda x: street2 in x, self.estate_2))[0]) #удаление из списка 2
                    self.estate_1.append(street2 + ': домов 0')                                  #добовление в список 1
                else: #если не собранны все улицы одного типа
                    # изменение статуса {кому принадлежит} у улицы:
                    self.data[self.data.index(list(filter(lambda x: x[1] == street2, self.data))[0])][6] = '1'
                    self.estate_2.remove(list(filter(lambda x: street2 in x, self.estate_2))[0]) #удаление из списка 2
                    self.estate_1.append(street2 + ': домов 0')                                  #добовление в список 1
        if street1 != 'ничего' or street2 != 'ничего': #если выбрана хотя бы 1 улица - обмен деньгами
            self.money_1 -= m1                                                         #списание денег у 1
            self.money_1 += m2                                                         #пополнение денег у 1
            self.money_2 -= m2                                                         #списание денег у 2
            self.money_2 += m1                                                         #пополнение денег у 2

            #изменение текста у виджетов с показателями (улиц, денег)
            self.bank1.setText('Банк: ' + str(self.money_1))                           #надпись с кол-вом денег 1
            self.bank2.setText('Банк: ' + str(self.money_2))                           #надпись с кол-вом денег 2
            spisok1 = sorted(list(filter(lambda x: len(x) >= 9, self.estate_1)), key=lambda x: (x[7], x[3])) \
                      + sorted(list(filter(lambda x: len(x) < 9, self.estate_1)))     #сортировка списка улиц 1
            self.text_1.setPlainText('\n'.join(spisok1))                              #добавление текста
            self.text_1.setFont(QFont('Times New Roman', 12))                         #шрифт, размер текста
            spisok2 = sorted(list(filter(lambda x: len(x) >= 9, self.estate_2)), key=lambda x: (x[7], x[3])) \
                     + sorted(list(filter(lambda x: len(x) < 9, self.estate_2)))      #сортировка списка улиц 2
            self.text_2.setPlainText('\n'.join(spisok2))                              #добавление текста
            self.text_2.setFont(QFont('Times New Roman', 12))                         #шрифт, размер текста

    def roll_the_dice(self): #функция хода и кидания кубиков
        self.ext.setEnabled(False)                                              #нельзя нажать кнопку "Выйти"
        if self.street.isHidden() is False:                                     #показ виджета с данными где вы
            self.street.hide()
        dashes = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']   #цифры кубиков
        s = str(choice(dashes)) + str(choice(dashes))                           #случайное выпадение кубиков
        number = int(dashes.index(s[0])) + int(dashes.index(s[1])) + 2          #цифра, выпавшая с кубиков
        self.kubik_hod.setText(s)                                               #добавление кубиков на виджет
        self.kubik_hod.show()                                                   #появление кубиков
        #ход игрока 1
        if self.count == 1:
            self.count = 2                                                      #счётчик хода
            self.place_1 += number                                              #номер клетки, где находится 1 игрок
            if self.place_1 > 31: #начисление зарплаты за проход круга
                self.money_1 += 200                                             #начисление зарплаты
                self.place_1 -= 32                                              #сброс номера клетки на круг
                self.bank1.setText('Банк: ' + str(self.money_1))                #надпись с кол-вом денег 1 игрока
            d = list(filter(lambda x: int(x[2]) == self.place_1 % 32, self.data[1:]))[0] #список данных клетки поля
            a, b = d[3][1:-1].split(', ')                                       #координаты клетки поля
            self.image_player1.move(int(a), int(b))                             #передвижение фишки на клетку поля
            if d[0] == 'стоянка' or d[0] == 'старт': #если находишься на стоянке или старте
                if d[0] == 'стоянка':
                    self.street.setPlainText('Вы попали на стоянку. Играем дальше')   #виджет с данными где вы
                else:
                    self.street.setPlainText('Вы попали на старт. Вы получаете +200') #виджет с данными где вы
                self.street.show()                                              #показ надписи где вы
                self.hod_2.show()                                               #показ чей ход
                self.hod_1.hide()                                               #скрытие виджета чей был ход
                self.ext.setEnabled(True)                                       #можно нажать кнопку "Выйти"
            elif d[0] == 'штраф': #если попал на штраф
                self.fine_button.setText('Заплатить штраф ' + d[5])              #текст кнопки
                self.fine_button.show()                                          #появление кнопки "Запалтить штраф"
                self.kubik.setEnabled(False)                                     #нельзя нажать на кнопку "Кинуть кубик"
                self.summa_1 = int(d[5])                                         #сумма штрафа
            elif d[0] == 'вокзал': #если попал на вокзал
                self.kubik.setEnabled(False)                                     #нельзя нажать на кнопку "Кинуть кубик"
                if d[6] == '0': #ничейный вокзал
                    self.buy.show()                                              #появление кнопки "Купить"
                    self.dont_buy.show()                                         #появление кнопки "Оставить"
                    self.street.setPlainText('Вы попали на вокзал. Он стоит ' + d[5]) #надпись где вы
                    self.street.show()                                           #показ надписи где вы
                    if self.money_1 < int(d[5]): #если не хватает денег нельзя купить
                        self.buy.setEnabled(False)                               #нельзя нажать на кнопку "Купить"
                elif d[6] == '1': #свой вокзал
                    self.street.setPlainText('Вы попали на свой вокзал. Следующий ход') #надпись где вы
                    self.street.show()                                           #показ надписи где вы
                    self.kubik.setEnabled(True)                                  #можно нажать на кнопку "Кинуть кубик"
                    self.ext.setEnabled(True)                                    #можно нажать на кнопку "Выйти"
                    self.hod_2.show()                                            #показ чей ход
                    self.hod_1.hide()                                            #скрытие чей был ход
                else: #чужой вокзал
                    self.street.setPlainText('Вы попали на чужой вокзал. Оплатите аренду ' + d[7 + int(d[7])]) #где вы
                    self.street.show()                                           #показ надписи где вы
                    self.fine_button.setText('Оплатить ' + d[7 + int(d[7])])     #текст кнопки
                    self.fine_button.show()                                      #появление кнопки "Оплатить"
            else: #если попал на улицу
                self.kubik.setEnabled(False)                                     #нельзя нажать на кнопку "Кинуть кубик"
                if d[6] == '0': #ничейная улица
                    self.buy.show()                                              #появление кнопки "Купить"
                    self.dont_buy.show()                                         #появление кнопки "Оставить"
                    self.street.setPlainText('Вы попали на улицу «' + d[1].capitalize() + '». Она стоит ' + d[5])#где вы
                    self.street.show()                                           #показ надписи где вы
                    if self.money_1 < int(d[5]): #если не хватает денег нельзя купить
                        self.buy.setEnabled(False)                               #нельзя нажать на кнопку "Купить"
                elif d[6] == '1': #своя улица
                    #a - кол-во своих улиц одного типа, b - кол-во улиц одного типа
                    a = list(filter(lambda x: x[12] == self.data[self.place_1 + 1][12] and x[6] == '1', self.data))
                    b = list(filter(lambda x: x[12] == self.data[self.place_1 + 1][12], self.data))
                    if len(a) == len(b): #если у вас все улицы одного цвета
                        if self.data[self.place_1 + 1][7] != '4':  #если у вас на улицы макс. кол-во домов
                            self.street.setPlainText('Вы попали на свою улицу. Желаете купить дом за ' + d[13] + '?')
                            self.street.show()                                         #показ надписи где вы
                            self.buy.show()                                            #появление кнопки "Купить"
                            self.dont_buy.show()                                       #появление кнопки "Оставить"
                            if self.money_1 < int(d[13]):#если не хватает денег нельзя купить
                                self.buy.setEnabled(False)                             #нельзя нажать на кнопку "Купить"
                        else: #если у вас на улицы не макс. кол-во домов
                            self.street.setPlainText('Вы попали на свою улицу. На ней уже есть 3 дома. Следующий ход')
                            self.street.show()                                    #показ надписи где вы
                            self.kubik.setEnabled(True)                           #можно нажать на кнопку "Кинуть кубик"
                            self.ext.setEnabled(True)                             #можно нажать на кнопку "Выйти"
                            self.hod_2.show()                                     #показ чей ход
                            self.hod_1.hide()                                     #скрытие чей был ход
                    else: #если у вас не все улицы одного цвета
                        self.street.setPlainText('Вы попали на свою улицу. Вы не можете поставить на неё дом' +
                                                 ', т.к. не куплены все улицы этого цвета. Следующий ход') #где вы
                        self.street.show()                                        #показ надписи где вы
                        self.kubik.setEnabled(True)                               #можно нажать на кнопку "Кинуть кубик"
                        self.ext.setEnabled(True)                                 #можно нажать на кнопку "Выйти"
                        self.hod_2.show()                                         #показ чей ход
                        self.hod_1.hide()                                         #скрытие чей был ход
                else:  #чужая улица
                    self.street.setPlainText('Вы попали на чужую улицу. Оплатите аренду ' + d[7 + int(d[7])]) #где вы
                    self.fine_button.setText('Оплатить ' + d[7 + int(d[7])])     #текст кнопки
                    self.fine_button.show()                                      #появление кнопки "Оплатить"
                    self.street.show()                                           #показ надписи где вы
        # ход игрока 2
        else:
            self.count = 1                                                       #счётчик хода
            self.place_2 += number                                               #номер клетки, где находится 1 игрок
            if self.place_2 > 31: #начисление зарплаты за проход круга
                self.money_2 += 200                                              #начисление зарплаты
                self.place_2 -= 32                                               #сброс номера клетки на круг
                self.bank2.setText('Банк: ' + str(self.money_2))                 #надпись с кол-вом денег 2 игрока
            d = list(filter(lambda x: int(x[2]) == self.place_2 % 32, self.data[1:]))[0] #список данных клетки поля
            a, b = d[4][1:-1].split(', ')                                       #координаты клетки поля
            self.image_player2.move(int(a), int(b))                             #передвижение фишки на клетку поля
            if d[0] == 'стоянка' or d[0] == 'старт': #если находишься на стоянке или старте
                if d[0] == 'стоянка':
                    self.street.setPlainText('Вы попали на стоянку. Играем дальше')   #виджет с данными где вы
                else:
                    self.street.setPlainText('Вы попали на старт. Вы получаете +200') #виджет с данными где вы
                self.street.show()                                               #показ надписи где вы
                self.hod_2.hide()                                                #скрытие надписи чей был ход
                self.hod_1.show()                                                #показ надписи чей ход
                self.ext.setEnabled(True)                                        #можно нажать на кнопку "Выйти"
            elif d[0] == 'штраф': #если попал на штраф
                self.fine_button.setText('Заплатить штраф ' + d[5])              #текст кнопки
                self.fine_button.show()                                          #появление кнопки "Заплатить штраф"
                self.kubik.setEnabled(False)                                     #нельзя нажать на кнопку "Кинуть кубик"
                self.summa_2 = int(d[5])                                         #сумма штрафа
            elif d[0] == 'вокзал': #если попал на вокзал
                self.kubik.setEnabled(False)                                     #нельзя нажать на кнопку "Кинуть кубик"
                if d[6] == '0': #ничейный вокзал
                    self.buy.show()                                              #появление кнопки "Купить"
                    self.dont_buy.show()                                         #появление кнопки "Оставить"
                    self.street.setPlainText('Вы попали на вокзал. Он стоит ' + d[5]) #надпись где вы
                    self.street.show()                                           #показ надписи где вы
                    if self.money_2 < int(d[5]): #если не хватает денег нельзя купить
                        self.buy.setEnabled(False)
                elif d[6] == '2': #свой вокзал
                    self.street.setPlainText('Вы попали на свой вокзал. Идём дальше') #надпись где вы
                    self.street.show()                                           #показ надписи где вы
                    self.kubik.setEnabled(True)                                  #можно нажать на кнопку "Кинуть кубик"
                    self.ext.setEnabled(True)                                    #можно нажать на кнопку "Выйти"
                    self.hod_2.hide()                                            #скрытие чей был ход
                    self.hod_1.show()                                            #показ чей ход
                else: #чужой вокзал
                    self.street.setPlainText('Вы попали на чужой вокзал. Оплатите аренду ' + d[7 + int(d[7])]) #где вы
                    self.street.show()                                           #показ надписи где вы
                    self.fine_button.setText('Оплатить ' + d[7 + int(d[7])])     #текст кнопки
                    self.fine_button.show()                                      #появление кнопки "Оплатить"
            else: #если попал на улицу
                self.kubik.setEnabled(False)                                     #нельзя нажать на кнопку "Кинуть кубик"
                if d[6] == '0': #ничейная улица
                    self.street.setPlainText('Вы попали на улицу «' + d[1].capitalize() + '». Она стоит ' + d[5])#где вы
                    self.street.show()                                           #показ надписи где вы
                    self.buy.show()                                              #появление кнопки "Купить"
                    self.dont_buy.show()                                         #появление кнопки "Оставить"
                    if self.money_2 < int(d[5]): #если не хватает денег нельзя купить
                        self.buy.setEnabled(False)                               #нельзя нажать на кнопку "Купить"
                elif d[6] == '2':  #своя улица
                    # a - кол-во своих улиц одного типа, b - кол-во улиц одного типа
                    a = list(filter(lambda x: x[12] == self.data[self.place_2 + 1][12] and x[6] == '2', self.data))
                    b = list(filter(lambda x: x[12] == self.data[self.place_2 + 1][12], self.data))
                    if len(a) == len(b): #если у вас все улицы одного цвета
                        if self.data[self.place_2 + 1][7] != '4': #если у вас на улицы макс. кол-во домов
                            self.street.setPlainText('Вы попали на свою улицу. Желаете купить дом за ' + d[13] + '?')
                            self.street.show()                                           #показ надписи где вы
                            self.buy.show()                                              #появление кнопки "Купить"
                            self.dont_buy.show()                                         #появление кнопки "Оставить"
                            if self.money_2 < int(d[13]): #если не хватает денег нельзя купить
                                self.buy.setEnabled(False)                        #нельзя нажать на кнопку "Купить"
                        else: #если у вас на улицы не макс. кол-во домов
                            self.street.setPlainText('Вы попали на свою улицу. На ней уже есть 3 дома. Следующий ход')
                            self.street.show()                                    #показ надписи где вы
                            self.kubik.setEnabled(True)                           #можно нажать на кнопку "Кинуть кубик"
                            self.ext.setEnabled(True)                             #можно нажать на кнопку "Выйти"
                            self.hod_2.hide()                                     #скрытие чей был ход
                            self.hod_1.show()                                     #показ чей ход
                    else: #если у вас не все улицы одного цвета
                        self.street.setPlainText('Вы попали на свою улицу. Вы не можете поставить на неё дом' +
                                                 ', т.к. не куплены все улицы этого цвета') #надпись где вы
                        self.street.show()                                        #показ надписи где вы
                        self.kubik.setEnabled(True)                               #можно нажать на кнопку "Кинуть кубик"
                        self.ext.setEnabled(True)                                 #можно нажать на кнопку "Выйти"
                        self.hod_2.hide()                                         #скрытие чей был ход
                        self.hod_1.show()                                         #показ чей ход
                else: #чужая улица
                    self.street.setPlainText('Вы попали на чужую улицу. Оплатите аренду ' + d[7 + int(d[7])]) #где вы
                    self.street.show()                                           #показ надписи где вы
                    self.fine_button.setText('Оплатить ' + d[7 + int(d[7])])     #текст кнопки
                    self.fine_button.show()                                      #появление кнопки "Оплатить"

    def next_hod(self): #Переход к следующему ходу
        self.kubik_hod.hide()                                             #скрыть кубики
        self.ext.setEnabled(True)                                         #можно нажать кнопку "Выйти"
        self.kubik.setEnabled(True)                                       #можно нажать кнопку "Кинуть кубик"
        self.buy.hide()                                                   #скрыть кнопку "Купить"
        self.dont_buy.hide()                                              #скрыть кнопку "Оставить"
        self.street.hide()                                                #скрыть надпись где вы
        if self.buy.isEnabled() is False:
            self.buy.setEnabled(True)                                     #можно нажать кнопку "Купить"
        if self.count == 2:
            self.hod_2.show()                                             #показать надпись чей ход
            self.hod_1.hide()                                             #скрыть надпись чей был ход
        else:
            self.hod_2.hide()                                             #скрыть надпись чей был ход
            self.hod_1.show()                                             #показать надпись чей ход

    def payment(self): #функция для оплаты и покупок
        #ход игрока 1
        if self.count == 2:
            if self.data[self.place_1 + 1][6] == '0':  #если ты попал на ничейное поле. Покупка поля
                #кол-во своих улиц одного типа
                a1 = list(filter(lambda x: x[12] == self.data[self.place_1 + 1][12] and x[6] == '1', self.data))
                if len(a1) > 0 and self.data[self.place_1 + 1][0] == 'вокзал': #если у тебя уже не один вокзал
                    # у всех своих воказалов в списке данных изменить {уровень}
                    for i in range(len(a1)):
                        self.data[self.data.index(a1[i])][7] = str(int(self.data[self.data.index(a1[i])][7]) + 1)
                    self.data[self.place_1 + 1][7] = str(int(self.data[self.place_1 + 1][7]) + len(a1))
                self.money_1 -= int(self.data[self.place_1 + 1][5])               #оплата покупки
                self.data[self.place_1 + 1][6] = '1'                              #кому принадлежит в списке данных
                if self.data[self.place_1 + 1][0] == 'вокзал': #если покупаешь вокзал
                    self.estate_1.append(self.data[self.place_1 + 1][1])           #добавление вокзала в список улиц 1
                else: #если покупаешь улицу
                    self.estate_1.append(self.data[self.place_1 + 1][1] + ': домов 0') #добавление улицы в список улиц 1
                self.buy.hide()                                                    #скрытие кнопки "Купить"
                self.dont_buy.hide()                                               #скрытие кнопки "Оставить"
                self.street.hide()                                                 #скрытие надписи где ты
            elif self.data[self.place_1 + 1][6] == '1': #если ты попал на свою улицу. Покупка дома
                home = str(int(self.data[self.place_1 + 1][7]) + 1)                #кол-во домов с покупкой
                self.data[self.place_1 + 1][7] = home                              #кол-во домов улицы в списке данных
                self.estate_1[self.estate_1.index(self.data[self.place_1 + 1][1] + ': домов ' + str(int(home) - 2))] =\
                    self.data[self.place_1 + 1][1] + ': домов ' + str(int(home) - 1) #кол-во домов улицы в списке улиц 1
                self.money_1 -= int(self.data[self.place_1 + 1][13])               #оплата покупки дома
                self.buy.hide()                                                    #скрытие кнопки "Купить"
                self.dont_buy.hide()                                               #скрытие кнопки "Оставить"
                self.street.hide()                                                 #скрытие надписи где ты
            elif self.data[self.place_1 + 1][6] == '2': #если ты попал на чужую улицу. Оплата аренды
                self.money_1 -= int(self.data[self.place_1 + 1][7 + int(self.data[self.place_1 + 1][7])])#оплата аренды
                self.money_2 += int(self.data[self.place_1 + 1][7 + int(self.data[self.place_1 + 1][7])])#доход с аренды
                self.fine_button.hide()                                            #скрытие кнопки "Оплатить аренду"
                self.street.hide()                                                 #скрытие надписи где ты
            if 'штраф' in self.sender().text(): #оплата штрафа
                self.money_1 -= self.summa_1                            #вычитание суммы штрафа
                self.summa_1 = 0                                        #очищение переменной
                self.fine_button.hide()                                 #скрытие кнопки "Заплатить штраф"
            if self.money_1 < 0: #обонкрачивание 1 игрока. Конец игры
                ex.the_end()     #запуск функции конец игры

            spisok1 = sorted(list(filter(lambda x: len(x) >= 9, self.estate_1)), key=lambda x: (x[7], x[3]))\
                     + sorted(list(filter(lambda x: len(x) < 9, self.estate_1)))  #сортировка списка улиц 1
            self.text_1.setPlainText('\n'.join(spisok1))                          #текст с улицами
            self.text_1.setFont(QFont('Times New Roman', 12))                     #шрифт, размер текста
            self.kubik.setEnabled(True)                                           #можно нажать кнопку "Кинуть кубик"
            self.ext.setEnabled(True)                                             #можно нажать кнопку "Выйти"
            self.hod_2.show()                                                     #появление виджета чей ход
            self.hod_1.hide()                                                     #скрытие виджета чей был ход
            self.kubik_hod.hide()                                                 #скрытие кубиков
        # ход игрока 2
        else:
            if self.data[self.place_2 + 1][6] == '0': #если ты попал на ничейное поле. Покупка поля
                #кол-во своих улиц одного типа
                a1 = list(filter(lambda x: x[12] == self.data[self.place_2 + 1][12] and x[6] == '2', self.data))
                if len(a1) > 0 and self.data[self.place_2 + 1][0] == 'вокзал': #если у тебя уже не один вокзал
                    # у всех своих воказалов в списке данных изменить {уровень}
                    for i in range(len(a1)):
                        self.data[self.data.index(a1[i])][7] = str(int(self.data[self.data.index(a1[i])][7]) + 1)
                    self.data[self.place_2 + 1][7] = str(int(self.data[self.place_2 + 1][7]) + len(a1))
                self.money_2 -= int(self.data[self.place_2 + 1][5])               #оплата покупки
                self.data[self.place_2 + 1][6] = '2'                              #кому принадлежит в списке данных
                if self.data[self.place_2 + 1][0] == 'вокзал': #если покупаешь вокзал
                    self.estate_2.append(self.data[self.place_2 + 1][1])          #добавление вокзала в список улиц 2
                else: #если покупаешь улицу
                    self.estate_2.append(self.data[self.place_2 + 1][1] + ': домов 0') #добавление улицы в список улиц 2
                self.buy.hide()                                                    #скрытие кнопки "Купить"
                self.dont_buy.hide()                                               #скрытие кнопки "Оставить"
                self.street.hide()                                                 #скрытие надписи где ты
            elif self.data[self.place_2 + 1][6] == '2': #если ты попал на свою улицу. Покупка дома
                home = str(int(self.data[self.place_2 + 1][7]) + 1)                #кол-во домов с покупкой
                self.data[self.place_2 + 1][7] = home                              #кол-во домов улицы в списке данных
                self.estate_2[self.estate_2.index(self.data[self.place_2 + 1][1] + ': домов ' + str(int(home) - 2))] =\
                    self.data[self.place_2 + 1][1] + ': домов ' + str(int(home) - 1) #кол-во домов улицы в списке улиц 2
                self.money_2 -= int(self.data[self.place_2 + 1][13])               #оплата покупки дома
                self.buy.hide()                                                    #скрытие кнопки "Купить"
                self.dont_buy.hide()                                               #скрытие кнопки "Оставить"
                self.street.hide()                                                 #скрытие надписи где ты
            elif self.data[self.place_2 + 1][6] == '1': #если ты попал на чужую улицу. Оплата аренды
                self.money_2 -= int(self.data[self.place_2 + 1][7 + int(self.data[self.place_2 + 1][7])])#оплата аренды
                self.money_1 += int(self.data[self.place_2 + 1][7 + int(self.data[self.place_2 + 1][7])])#доход с аренды
                self.fine_button.hide()                                            #скрытие кнопки "Оплатить аренду"
                self.street.hide()                                                 #скрытие надписи где ты
            if 'штраф' in self.sender().text(): #оплата штрафа
                self.money_2 -= self.summa_2                            #вычитание суммы штрафа
                self.summa_2 = 0                                        #очищение переменной
                self.fine_button.hide()                                 #скрытие кнопки "Заплатить штраф"
            if self.money_2 < 0: #обонкрачивание 2 игрока. Конец игры
                ex.the_end()     #запуск функции конец игры

            spisok = sorted(list(filter(lambda x: len(x) >= 9, self.estate_2)), key=lambda x: (x[7], x[3]))\
                     + sorted(list(filter(lambda x: len(x) < 9, self.estate_2))) #сортировка списка улиц 2
            self.text_2.setPlainText('\n'.join(spisok))                          #текст с улицами
            self.text_2.setFont(QFont('Times New Roman', 12))                    #шрифт, размер текста
            self.kubik.setEnabled(True)                                          #можно нажать кнопку "Кинуть кубик"
            self.ext.setEnabled(True)                                            #можно нажать кнопку "Выйти"
            self.hod_2.hide()                                                    #скрытие виджета чей был ход
            self.hod_1.show()                                                    #появление виджета чей ход
            self.kubik_hod.hide()                                                #скрытие кубиков
        self.bank1.setText('Банк: ' + str(self.money_1))                         #надпись о кол-ве денег 1
        self.bank2.setText('Банк: ' + str(self.money_2))                         #надпись о кол-ве денег 2

    def playAudioFile(self): #функция, запускающая музыку
        a = os.path.join(os.getcwd(), 'm3.mp3')                                     #находит файл с музыкой
        self.music.setMedia(QMediaContent(QUrl.fromLocalFile(a)))                   #что-то на скопированном
        self.music.setVolume(10)                                                    #назначает громкость музыки
        self.music.play()                                                           #включает музыку

    def stopAudio(self): #функция, выключающая музыку
        self.music.stop()

    def playAudio(self): #функция, включающая музыку
        self.music.play()

    def quieterAudio(self): #функция, уменьшающая громкость на 5, но полностью не отключает, оставляет 1
        if self.music.volume() > 5:
            self.music.setVolume(self.music.volume() - 5)
        else:
            self.music.setVolume(1)

    def louderAudio(self): #функция, увеличивающая громкость на 5
        self.music.setVolume(self.music.volume() + 5)

    def the_end(self): #функция, запускающая конец игры
        # создание для класса The_end необходимых переменных
        global winner, money, how_winner                              #создание глобальных переменных
        money = [int(self.money_1), int(self.money_2)]                #переменная со списком зароботанных денег играками
        winner = [self.name_1.text(), self.name_2.text()]             #переменная со списком имён играков

        # переменная со индексом победителя при одинаковом кол-ве денег
        if self.hod_1.isHidden():
            how_winner = 0
        else:
            how_winner = 1

        self.stopAudio()                                               #запуск функции stopAudio для отключения музыыки

        #подключение последней музыки
        self.music_end = QMediaPlayer()                                #класс для воспроизведения музыки
        a = os.path.join(os.getcwd(), 'm4.mp3')                        #нахождит музыкальный файл
        self.music_end.setMedia(QMediaContent(QUrl.fromLocalFile(a)))  #что-то на скопированном
        self.music_end.setVolume(10)                                   #назначение громкости
        self.music_end.play()                                          #запуск музыки

        self.game_over = The_end(self, "Конец игры")                   #создания окна с результатом
        self.hide()                                                    #закрытие основного окна
        self.game_over.show()                                          #показ окна с результатом


class Regulation(QWidget): #окно для прасмотра правил
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        # создание окна
        self.setGeometry(600, 300, 800, 600)                                #размер и расположение окна
        self.setWindowTitle('Правила')                                      #название окна

        with open('regulations.txt', 'r', encoding='utf-8') as text:        #открытие текстового файла на чтение
            my_list = [i.rstrip() for i in text.readlines()]                #запись файла в список

        #виджет текст
        self.text_field = QPlainTextEdit(self)                              #создание виджета
        self.text_field.setReadOnly(True)                                   #запрет менять текст пользователем
        self.text_field.move(10, 10)                                        #расположение виджета
        self.text_field.setPlainText('\n'.join(my_list))                    #запись в виджет текста из файла
        self.text_field.setFont(QFont('Times New Roman', 14))               #изменение размера и шрифта текста


    def resizeEvent(self, event): #функция, подстраивающая размер виджета относительно размера окна
        x, y = self.size().width(), self.size().height()                    #переменные x и у c размерами окна
        self.text_field.resize(x - 20, y - 20)                             #размер виджета относительно окна


class Exchange_street(QDialog): #диалоговое окно для торговли
    def __init__(self):
        super(Exchange_street, self).__init__()
        self.setFixedSize(550, 250)                                                 #фиксация размера окна
        self.layout = QVBoxLayout(self)                                             #создание виджета-макета
        self.buttonBox = QDialogButtonBox(self)                                     #создание виджета-макета для кнопок

        #надпись, указывающая имя 1 игрока
        self.label1 = QLabel(self)                                                  #создание виджета
        self.label1.resize(300, 50)                                                 #размер виджета
        self.label1.setText(f'Игрок "{n1}" выберите улицу')                         #название у виджета
        self.label1.setFont(QFont('Times New Roman', 8))                           #шрифт и размер текста
        self.label1.move(10, 10)                                                    #расположение виджета

        # надпись, указывающая имя 2 игрока
        self.label2 = QLabel(self)                                                  #создание виджета
        self.label2.resize(300, 50)                                                 #размер виджета
        self.label2.setText(f'Игрок "{n2}" выберите улицу')                         #название у виджета
        self.label2.setFont(QFont('Times New Roman', 8))                           #шрифт и размер текста
        self.label2.move(300, 10)                                                   #расположение виджета

        # надпись, указывающая имя 1 игрока для выбора отдаваемой суммы
        self.label3 = QLabel(self)                                                  #создание виджета
        self.label3.resize(300, 50)                                                 #размер виджета
        self.label3.setText('Введите сумму, которую отдаёте')                       #название у виджета
        self.label3.setFont(QFont('Times New Roman', 8))                           #шрифт и размер текста
        self.label3.move(10, 75)                                                    #расположение виджета

        # надпись, указывающая имя 1 игрока для выбора отдаваемой суммы
        self.label4 = QLabel(self)                                                  #создание виджета
        self.label4.resize(300, 50)                                                 #размер виджета
        self.label4.setText('Введите сумму, которую отдаёте')                       #название у виджета
        self.label4.setFont(QFont('Times New Roman', 8))                           #шрифт и размер текста
        self.label4.move(300, 75)                                                   #расположение виджета

        # виджет со списком для выбора улиц 1 игрока
        self.name_street1 = QComboBox(self)                                         #создание виджета
        self.name_street1.resize(200, 25)                                           #размер виджета
        self.name_street1.move(10, 58)                                              #расположение виджета

        # виджет со списком для выбора улиц 2 игрока
        self.name_street2 = QComboBox(self)                                         #создание виджета
        self.name_street2.resize(200, 25)                                           #размер виджета
        self.name_street2.move(300, 58)                                             #расположение виджета

        # виджет со выбором числа, меняющегося при помощи стрелок, 1 игрока
        self.money1 = QSpinBox(self)                                                #создание виджета
        self.money1.setSingleStep(25)                                               #выбор шага изменения числа
        self.money1.setRange(0, mon1)                                               #выбор границ числа
        self.money1.move(10, 125)                                                   #расположение виджета

        # виджет со выбором числа, меняющегося при помощи стрелок, 2 игрока
        self.money2 = QSpinBox(self)                                                #создание виджета
        self.money2.setSingleStep(25)                                               #выбор шага изменения числа
        self.money2.setRange(0, mon2)                                               #выбор границ числа
        self.money2.move(300, 125)                                                  #расположение виджета

        # подключение в виджеты списки с улицами
        self.name_street1.addItems(['ничего'] + estate1)
        self.name_street2.addItems(['ничего'] + estate2)

        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)       #подключение кнопок
        self.buttonBox.resize(200, 50)                                                         #размер виджета
        self.buttonBox.move(150, 200)                                                          #расположение виджета

        self.buttonBox.accepted.connect(self.accept)                                 #подключение кнопке функции
        self.buttonBox.rejected.connect(self.reject)                                 #подключение кнопке функции
        self.buttonBox.button(QDialogButtonBox.Ok).setText("Обменять")               #название кнопки
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("Отмена")             #название кнопки

    def accept(self): #функция для кнопки OK/Обменять
        self.hide()                                                                  #закрыть окно

        #создание для функции exchange необходимых переменных
        global street1, street2, m1, m2                              #создание глобальных переменных
        street1 = self.name_street1.currentText()                    #переменная с названием выбранной улицы от 1 игрока
        street2 = self.name_street2.currentText()                    #переменная с названием выбранной улицы от 2 игрока
        m1 = int(self.money1.text())                                 #переменная с суммой, которую заплатит 1 игрок
        m2 = int(self.money2.text())                                 #переменная с суммой, которую заплатит 1 игрок
        ex.exchange()                                                #запуск функции exchange


class Sound_settings(QWidget): #окно для настройки звука
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        #создание окна
        self.setGeometry(700, 250, 265, 200)                  #размер и расположение окна
        self.setWindowTitle('Настройки')                      #название окна
        self.setMaximumSize(265, 175)                         #не позволяет расширять окно
        self.setMinimumSize(265, 175)                         #не позволяет уменьшать окно

        #виджет надпись
        self.txt = QLabel('Настроить звук:', self)            #название и создание виджета
        self.txt.setFont(QFont('Times New Roman', 10))        #изменение размера и шрифта текста
        self.txt.resize(200, 50)                              #размер виджета
        self.txt.move(25, 25)                                 #расположение виджета

        #кнопка для уменьшения громкости
        self.quieter = QPushButton('-', self)                 #название и создание виджета
        self.quieter.setFont(QFont('Times New Roman', 25))    #изменение размера и шрифта текста
        self.quieter.resize(50, 50)                           #размер виджета
        self.quieter.move(25, 100)                            #расположение виджета
        self.quieter.clicked.connect(self.music)              #запуск функции music

        #кнопка для увеличения громкости
        self.louder = QPushButton('+', self)                  #название и создание виджета
        self.louder.setFont(QFont('Times New Roman', 30))     #изменение размера и шрифта текста
        self.louder.resize(50, 50)                            #размер виджета
        self.louder.move(190, 100)                            #расположение виджета
        self.louder.clicked.connect(self.music)               #запуск функции music

        #кнопка выключить звук
        self.pause = QPushButton('🔈', self)                  # название и создание виджета
        self.pause.setFont(QFont('Times New Roman', 20))      #изменение размера и шрифта текста
        self.pause.resize(50, 50)                             #размер виджета
        self.pause.move(80, 100)                              #расположение виджета
        self.pause.clicked.connect(self.music)                #запуск функции music

        #кнопка включить звук
        self.pusk = QPushButton('🔊', self)                  # название и создание виджета
        self.pusk.setFont(QFont('Times New Roman', 20))      #изменение размера и шрифта текста
        self.pusk.resize(50, 50)                             #размер виджета
        self.pusk.move(135, 100)                             #расположение виджета
        self.pusk.clicked.connect(self.music)                #запуск функции music

        #окно с подтверждением
        self.pause_form = Switch_off(self)                  #создаёт окно pause_form
        self.pause_form.hide()                              #скрывает окно pause_form

    def music(self): #функция, которая взависимости от кнопки запускает нужную функцию
        if self.sender().text() == '🔊':
            ex.playAudio()                         #запуск функции playAudio, которая включает звук
        if self.sender().text() == '+':
            ex.louderAudio()                       #запуск функции louderAudio, которая уменьшает громкость
        if self.sender().text() == '-':
            ex.quieterAudio()                      #запуск функции quieterAudio, которая увеличивает громкость
        if self.sender().text() == '🔈':
            if self.pause_form.isHidden():
                self.pause_form.show()             #показывает скрытое окно pause_form
            else:
                self.pause_form.hide()             #скрывает окно pause_form


class Switch_off(QWidget):  #окно для подтверждения ответа выключения музыки
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        #создание окна
        self.setGeometry(700, 250, 550, 250)                                     #размер и расположение окна
        self.setWindowTitle('Выбирайте с умом')                                  #название окна
        self.setMaximumSize(550, 250)                                            #не позволяет расширять окно
        self.setMinimumSize(550, 250)                                            #не позволяет уменьшать окно

        #надпись задаваемого вопроса
        self.question = QLabel('Вы уверены, что хотите выключить звук?', self)   #название и создание виджета
        self.question.setFont(QFont('Times New Roman', 20))                      #изменение размера и шрифта текста
        self.question.resize(600, 50)                                            #размер виджета
        self.question.move(25, 25)                                               #расположение виджета

        # кнопка, выключающая музыку
        self.heartless = QPushButton('Да, у меня нет сердца', self)              #название и создание виджета
        self.heartless.setFont(QFont('Times New Roman', 20))                     #изменение размера и шрифта текста
        self.heartless.resize(500, 50)                                           #размер виджета
        self.heartless.move(25, 100)                                             #расположение виджета
        self.heartless.clicked.connect(self.stop)                                #запуск функции stop

        #кнопка, возвращающая назад
        self.right_choice = QPushButton('Нет, музыка классная', self)            #название и создание виджета
        self.right_choice.setFont(QFont('Times New Roman', 20))                  #изменение размера и шрифта текста
        self.right_choice.resize(500, 50)                                        #размер виджета
        self.right_choice.move(25, 175)                                          #расположение виджета
        self.right_choice.clicked.connect(self.stop)                             #запуск функции stop

    # функция для выключения звука/возвращения назад
    def stop(self):
        if self.sender().text() == 'Да, у меня нет сердца':
            ex.stopAudio()                                                       #запуск функции, которая выключает звук
        self.hide()                                                              #сокрытие окна


class The_end(QWidget): #окно c результатом
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        # n - индекс по которму определяется победитель
        if money[0] == money[1]:
            n = how_winner #при одинаковом кол-ве денег проигрывает тот, кто ходил
        else:
            n = money.index(max(money)) #индекс того у кого больше денег
        self.setGeometry(500, 250, 1000, 700)                                   #размер и расположение окна
        self.setWindowTitle('Конец игры')                                       #название окна
        self.setMaximumSize(1000, 700)                                          #не позволяет расширять окно
        self.setMinimumSize(1000, 700)                                          #не позволяет уменьшать окно

        self.pix = QPixmap('картинки/город.jpg')                                # открытие картинки с заставкой
        self.image = QLabel(self)                                               # создание виджета
        self.image.move(0, 0)                                                   # расположение виджета
        self.image.setPixmap(self.pix)                                          # запись картинки на виджет

        self.title = QLabel(f'Победитель {winner[n]} !!!', self)                # надпись с именем победителя
        self.title.move(170, 200)                                               # расположение виджета
        self.title.setFont(QFont('Arial', 20))                                  # размер и шрифт текста

        self.result = QLabel(f'Всего заработал: {money[n]}', self)              #надпись сколько заработал победитель
        self.result.move(240, 365)                                              # расположение виджета
        self.result.setFont(QFont('Arial', 20))                                 #размер и шрифт текста


class Price_list(QWidget): #окно для прасмотра цен
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        # создание окна
        self.setGeometry(600, 300, 800, 600) #размер и расположение окна
        self.setWindowTitle('Цены') #название окна
        self.setFixedSize(665, 690)

        # картинка с ценами
        self.pix = QPixmap('картинки/цены.PNG')                 # открытие картинки с таблицей
        self.image = QLabel(self)                               # создание виджета
        self.image.move(10, 10)                                 # расположение виджета
        self.image.setPixmap(self.pix)                          # запись картинки на виджет
        self.image.show()                                       # скрытие картинки


app = QApplication(sys.argv)
ex = Ex()
ex.show()
sys.excepthook = except_hook
sys.exit(app.exec())
