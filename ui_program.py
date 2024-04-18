# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_program.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1089, 827)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_text = QLabel(self.centralwidget)
        self.label_text.setObjectName(u"label_text")
        self.label_text.setGeometry(QRect(20, 10, 471, 61))
        font1 = QFont()
        font1.setFamilies([u"NiseSega Cyrillic"])
        font1.setPointSize(18)
        self.label_text.setFont(font1)
        self.label_text.setAlignment(Qt.AlignCenter)
        self.label_converted_text = QLabel(self.centralwidget)
        self.label_converted_text.setObjectName(u"label_converted_text")
        self.label_converted_text.setGeometry(QRect(20, 540, 471, 61))
        self.label_converted_text.setFont(font1)
        self.label_converted_text.setAlignment(Qt.AlignCenter)
        self.original_text = QTextEdit(self.centralwidget)
        self.original_text.setObjectName(u"original_text")
        self.original_text.setGeometry(QRect(20, 100, 471, 161))
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(12)
        self.original_text.setFont(font2)
        self.original_text.setStyleSheet(u"border-color: white;\n"
"padding: 5px;")
        self.original_text.setFrameShape(QFrame.Box)
        self.original_text.setFrameShadow(QFrame.Plain)
        self.label_key = QLabel(self.centralwidget)
        self.label_key.setObjectName(u"label_key")
        self.label_key.setGeometry(QRect(20, 340, 471, 51))
        self.label_key.setFont(font1)
        self.label_key.setAlignment(Qt.AlignCenter)
        self.btn_performing = QPushButton(self.centralwidget)
        self.btn_performing.setObjectName(u"btn_performing")
        self.btn_performing.setGeometry(QRect(700, 720, 211, 61))
        self.btn_performing.setFont(font1)
        self.btn_performing.setStyleSheet(u"QPushButton {\n"
"color: red;\n"
"border: 2px solid red;\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 90);\n"
"}")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(640, 500, 332, 131))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_performing = QLabel(self.layoutWidget)
        self.label_performing.setObjectName(u"label_performing")
        self.label_performing.setFont(font1)
        self.label_performing.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_performing)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radio_encode = QRadioButton(self.layoutWidget)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radio_encode)
        self.radio_encode.setObjectName(u"radio_encode")
        self.radio_encode.setEnabled(True)
        font3 = QFont()
        font3.setFamilies([u"Consolas"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.radio_encode.setFont(font3)

        self.horizontalLayout.addWidget(self.radio_encode)

        self.radio_decode = QRadioButton(self.layoutWidget)
        self.buttonGroup.addButton(self.radio_decode)
        self.radio_decode.setObjectName(u"radio_decode")
        self.radio_decode.setEnabled(True)
        self.radio_decode.setFont(font3)

        self.horizontalLayout.addWidget(self.radio_decode)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.table_alphabet = QTableWidget(self.centralwidget)
        self.table_alphabet.setObjectName(u"table_alphabet")
        self.table_alphabet.setGeometry(QRect(650, 140, 321, 351))
        font4 = QFont()
        font4.setPointSize(12)
        self.table_alphabet.setFont(font4)
        self.table_alphabet.setStyleSheet(u"")
        self.table_alphabet.setAlternatingRowColors(False)
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(650, 10, 321, 111))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_alphabet = QLabel(self.layoutWidget1)
        self.label_alphabet.setObjectName(u"label_alphabet")
        self.label_alphabet.setFont(font1)
        self.label_alphabet.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_alphabet)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radio_rus_alphabet = QRadioButton(self.layoutWidget1)
        self.radio_rus_alphabet.setObjectName(u"radio_rus_alphabet")
        self.radio_rus_alphabet.setEnabled(True)
        self.radio_rus_alphabet.setFont(font3)

        self.horizontalLayout_2.addWidget(self.radio_rus_alphabet)

        self.radio_eng_alphabet = QRadioButton(self.layoutWidget1)
        self.radio_eng_alphabet.setObjectName(u"radio_eng_alphabet")
        self.radio_eng_alphabet.setEnabled(True)
        self.radio_eng_alphabet.setFont(font3)

        self.horizontalLayout_2.addWidget(self.radio_eng_alphabet)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.key = QTextEdit(self.centralwidget)
        self.key.setObjectName(u"key")
        self.key.setGeometry(QRect(20, 420, 471, 61))
        self.key.setFont(font2)
        self.key.setStyleSheet(u"border-color: white;\n"
"padding: 5px;")
        self.key.setFrameShape(QFrame.Box)
        self.key.setFrameShadow(QFrame.Plain)
        self.cipher_modification = QCheckBox(self.centralwidget)
        self.cipher_modification.setObjectName(u"cipher_modification")
        self.cipher_modification.setGeometry(QRect(690, 650, 231, 41))
        font5 = QFont()
        font5.setFamilies([u"Consolas"])
        font5.setPointSize(16)
        self.cipher_modification.setFont(font5)
        self.converted_text = QTextEdit(self.centralwidget)
        self.converted_text.setObjectName(u"converted_text")
        self.converted_text.setGeometry(QRect(20, 630, 471, 151))
        self.converted_text.setFont(font2)
        self.converted_text.setStyleSheet(u"border-color: white;\n"
"padding: 5px;")
        self.converted_text.setFrameShape(QFrame.Box)
        self.converted_text.setFrameShadow(QFrame.Plain)
        self.converted_text.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Hill Cipher", None))
        self.label_text.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442:", None))
        self.label_converted_text.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442:", None))
        self.original_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442", None))
        self.label_key.setText(QCoreApplication.translate("MainWindow", u"\u043a\u043b\u044e\u0447:", None))
        self.btn_performing.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0410\u0421\u0421\u0427\u0418\u0422\u0410\u0422\u042c", None))
        self.label_performing.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435:", None))
        self.radio_encode.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.radio_decode.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_alphabet.setText(QCoreApplication.translate("MainWindow", u"\u0430\u043b\u0444\u0430\u0432\u0438\u0442:", None))
        self.radio_rus_alphabet.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0441\u0441\u043a\u0438\u0439", None))
        self.radio_eng_alphabet.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439", None))
        self.key.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u044e\u0447", None))
        self.cipher_modification.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u0448\u0438\u0444\u0440\u0430", None))
        self.converted_text.setPlaceholderText("")
    # retranslateUi

