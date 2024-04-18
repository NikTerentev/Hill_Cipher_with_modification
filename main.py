import csv
import re
import sys

from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, \
    QAbstractItemView, QTableWidgetItem

from hill_cipher import HillCipher
from ui_program import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(1089, 827)
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        self.alphabet = ""

        self.ui.radio_encode.setChecked(True)
        self.ui.radio_rus_alphabet.setChecked(True)

        self.show_rus_alphabet()

        self.ui.btn_performing.clicked.connect(self.performing_transformations)
        self.ui.radio_rus_alphabet.clicked.connect(self.show_rus_alphabet)
        self.ui.radio_eng_alphabet.clicked.connect(self.show_eng_alphabet)

    def show_rus_alphabet(self):
        if not self.alphabet == "rus":
            table_alphabet = self.ui.table_alphabet
            table_alphabet.setEditTriggers(QAbstractItemView.NoEditTriggers)

            table_alphabet.setRowCount(37)
            table_alphabet.setColumnCount(2)
            table_alphabet.setColumnWidth(0, 120)
            table_alphabet.setColumnWidth(1, 120)

            with open("alphabets/Russian_alphabet.csv",
                      encoding="utf-8-sig") as csv_alphabet:
                file_reader = csv.reader(csv_alphabet, delimiter=";")
                row_number = -1
                for row in file_reader:
                    row_number += 1
                    for column_number in range(0, 2):
                        table_alphabet.setItem(row_number, column_number,
                                               QTableWidgetItem(
                                                   row[column_number]))

            self.alphabet = "rus"

    def show_eng_alphabet(self):
        if not self.alphabet == "eng":
            table_alphabet = self.ui.table_alphabet
            table_alphabet.setEditTriggers(QAbstractItemView.NoEditTriggers)

            table_alphabet.setRowCount(31)
            table_alphabet.setColumnCount(2)
            table_alphabet.setColumnWidth(0, 120)
            table_alphabet.setColumnWidth(1, 120)

            with open("alphabets/English_alphabet.csv",
                      encoding="utf-8-sig") as csv_alphabet:
                file_reader = csv.reader(csv_alphabet, delimiter=";")
                row_number = -1
                for row in file_reader:
                    row_number += 1
                    for column_number in range(0, 2):
                        table_alphabet.setItem(row_number, column_number,
                                               QTableWidgetItem(
                                                   row[column_number]))

            self.alphabet = "eng"

    def match_strings(self):
        regular_string = "^[А-ЯЁ,. ?]+$" if self.alphabet == "rus" else \
            "^[A-Z,. ?!]+$"

        if re.fullmatch(regular_string,
                        self.ui.original_text.toPlainText().upper().strip()):
            if not re.fullmatch(
                    regular_string, self.ui.key.toPlainText().upper().strip()):
                QMessageBox.critical(None, "Ошибка!",
                                     "Неверный ключ. Ключ должен "
                                     "содержать только алфавитные "
                                     "символы!",
                                     QMessageBox.Ok)
            else:
                return True
        else:
            QMessageBox.critical(None, "Ошибка!",
                                 "Неверный текст. Текст должен "
                                 "содержать только алфавитные символы!",
                                 QMessageBox.Ok)

    def check_fields(self):
        if not self.ui.original_text.toPlainText().strip():
            QMessageBox.critical(None, "Ошибка!", "Поле для текста пусто!",
                                 QMessageBox.Ok)
        elif not self.ui.key.toPlainText().strip():
            QMessageBox.critical(None, "Ошибка!", "Ключ не указан!",
                                 QMessageBox.Ok)
        else:
            if self.match_strings():
                return True
            else:
                return False

    def performing_transformations(self):
        if self.check_fields():
            encoder = HillCipher(self.alphabet,
                                 self.ui.original_text.toPlainText().upper().
                                 strip(),
                                 self.ui.key.toPlainText().upper().strip())
            if encoder:
                if self.ui.radio_encode.isChecked():
                    if self.ui.cipher_modification.isChecked():
                        self.ui.converted_text.setText(
                            encoder.encode_modification())
                    else:
                        self.ui.converted_text.setText(
                            encoder.encode())
                elif self.ui.radio_decode.isChecked():
                    if self.ui.cipher_modification.isChecked():
                        self.ui.converted_text.setText(
                            encoder.decode_modification())
                    else:
                        self.ui.converted_text.setText(
                            encoder.decode())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
