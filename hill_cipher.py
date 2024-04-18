import math
import csv
import numpy as np
import numpy.linalg.linalg

from PySide6.QtWidgets import QMessageBox


class HillCipher:
    def __init__(self, alphabet, text, key):
        self.alphabet = alphabet
        self.text = text
        self.key = key
        self.key_length = 0
        self.key_sqrt = 0
        self.key_matrix = []
        self.invert_key_matrix = []
        self.load_alphabet()

    def load_alphabet(self):
        path_to_file = ""

        if self.alphabet == "rus":
            path_to_file = "alphabets/Russian_alphabet.csv"
        elif self.alphabet == "eng":
            path_to_file = "alphabets/English_alphabet.csv"

        self.alphabet = {}

        with open(path_to_file,
                  encoding="utf-8-sig", newline="") as csv_alphabet:
            file_reader = csv.reader(csv_alphabet, delimiter=";")
            for row in file_reader:
                self.alphabet[row[0]] = int(row[1])

    def convert_text(self):
        text_blocks = []
        for index in range(int(len(self.text) / self.key_sqrt)):
            tmp = np.array(self.text[self.key_sqrt * index:(self.key_sqrt *
                                                            index) +
                                                           self.key_sqrt])
            tmp = np.reshape(tmp, (self.key_sqrt, 1))
            text_blocks.append(tmp)
        self.text = np.array(text_blocks)

    def prepare_data(self):
        if self.check_key_sqrt():
            for letter in self.key:
                self.key_matrix.append(self.alphabet[letter])

            self.key_matrix = np.reshape(np.array(self.key_matrix),
                                         (-1, self.key_sqrt))

            determinant = numpy.linalg.det(self.key_matrix)

            if determinant != 0:
                if np.gcd(int(determinant), len(self.alphabet)) == 1:
                    text_padded = self.pad_text()

                    self.text = []
                    for letter in text_padded:
                        self.text.append(self.alphabet[letter])

                    self.convert_text()

                    return True

                else:
                    QMessageBox.critical(None, "Ошибка!",
                                         "Неверный ключ. Детерминат "
                                         "матрицы ключа"
                                         " и длина алфавита не являются взаимно"
                                         " простыми",
                                         QMessageBox.Ok)
                    return False

            else:
                QMessageBox.critical(None, "Ошибка!",
                                     "Неверный ключ. Определитель матрицы ключа"
                                     " равен нулю",
                                     QMessageBox.Ok)
                return False

        else:
            QMessageBox.critical(None, "Ошибка!",
                                 "Неверный ключ. Длина ключа должна быть"
                                 " квадратом целого числа",
                                 QMessageBox.Ok)
            return False

    def check_key_sqrt(self):
        self.key_length = len(self.key)
        self.key_sqrt = math.sqrt(self.key_length)

        if (self.key_sqrt - int(self.key_sqrt)) != 0:
            return False
        else:
            self.key_sqrt = int(self.key_sqrt)
            return True

    def pad_text(self):
        text_len = len(self.text)
        if (text_len % self.key_sqrt) != 0:
            pad_len = self.key_sqrt - (text_len % self.key_sqrt)

            text_padded = self.text + pad_len * ' '
            return text_padded
        return self.text

    def get_letter(self, target):
        for letter, number in self.alphabet.items():
            if number == target:
                return letter

    def multiplicative_inverse(self, det):
        mul_inv = -1
        for i in range(len(self.alphabet)):
            inverse = det * i
            if inverse % len(self.alphabet) == 1:
                mul_inv = i
                break
        return mul_inv

    def invert_key(self):
        determinant = int(np.round(np.linalg.det(self.key_matrix)))
        determinant_inverse = self.multiplicative_inverse(
            determinant % len(self.alphabet))
        self.invert_key_matrix = determinant_inverse * np.round(
            determinant * np.linalg.inv(self.key_matrix)).astype(int) % len(
            self.alphabet)

    def encrypt(self):
        message = []
        for block in self.text:
            tmp = np.dot(self.key_matrix, block) % len(self.alphabet)
            message.append(tmp)
        message = np.array(message).flatten()
        encrypted_text = [self.get_letter(number) for number in message]
        return "".join(encrypted_text)

    def encode(self):
        if self.prepare_data():
            encrypted_text = self.encrypt()
            return encrypted_text
        else:
            return ""

    def encrypt_modification(self):
        message = []
        for block in self.text:
            # Перемешиваем элементы блока в соответствии с функцией перестановки, зависящей от ключа
            shuffled_block = self.shuffle(block)
            # Умножаем перемешанный блок на матрицу ключа по модулю размера алфавита
            tmp = np.dot(self.key_matrix, shuffled_block) % len(self.alphabet)
            message.append(tmp)
        message = np.array(message).flatten()
        encrypted_text = [self.get_letter(number) for number in message]
        return "".join(encrypted_text)

    def shuffle(self, block):
        # Определяем функцию перестановки, например, такую:
        # f(x_1, x_2, ..., x_k) = (x_k + a_{11}, x_1 + a_{22}, ..., x_{k-1} + a_{kk}) mod m
        # где a_{ii} - элементы на главной диагонали матрицы ключа
        # k - размерность ключа
        k = self.key_sqrt
        m = len(self.alphabet)
        # Создаем пустой список для хранения перемешанных элементов блока
        shuffled_block = []
        # Для каждого элемента блока применяем функцию перестановки и добавляем его в список
        for i in range(k):
            x_i = block[i][0]
            a_ii = self.key_matrix[i][i]
            y_i = (x_i + a_ii) % m
            shuffled_block.append(y_i)
        # Сдвигаем список на один элемент влево, чтобы получить циклическую перестановку
        shuffled_block = shuffled_block[-1:] + shuffled_block[:-1]
        # Возвращаем перемешанный блок в виде вектора-столбца
        return np.array(shuffled_block).reshape(k, 1)

    def encode_modification(self):
        if self.prepare_data():
            encrypted_text = self.encrypt_modification()
            return encrypted_text
        else:
            return ""

    def decrypt_modification(self):
        # Находим обратную матрицу ключа
        self.invert_key()

        message = []
        for block in self.text:
            # Умножаем зашифрованный блок на обратную матрицу ключа по модулю размера алфавита
            tmp = np.dot(self.invert_key_matrix, block) % len(self.alphabet)
            # Восстанавливаем элементы блока в соответствии с обратной функцией перестановки, зависящей от ключа
            restored_block = self.restore(tmp)
            message.append(restored_block)
        message = np.array(message).flatten()
        decrypted_text = [self.get_letter(int(number)) for number in message]
        return "".join(decrypted_text)

    def restore(self, block):
        # Определяем обратную функцию перестановки, например, такую:
        # f^{-1}(y_1, y_2, ..., y_k) = (y_2 - a_{22}, y_3 - a_{33}, ..., y_1 - a_{11}) mod m
        # где a_{ii} - элементы на главной диагонали матрицы ключа
        # k - размерность ключа
        k = self.key_sqrt
        m = len(self.alphabet)
        # Создаем пустой список для хранения исходных элементов блока
        original_block = []
        # Сдвигаем список на один элемент вправо, чтобы получить обратную циклическую перестановку
        block = np.roll(block[:, 0], -1).reshape((-1, 1))
        # Для каждого элемента блока применяем обратную функцию перестановки и добавляем его в список
        for i in range(k):
            y_i = block[i][0]
            a_ii = self.key_matrix[i][i]
            x_i = (y_i - a_ii) % m
            original_block.append(x_i)
        # Возвращаем исходный блок в виде вектора-столбца
        return np.array(original_block).reshape(k, 1)

    def decode_modification(self):
        if self.prepare_data():
            decrypted_text = self.decrypt_modification()
            return decrypted_text
        else:
            return ""

    def decrypt(self):
        self.invert_key()

        message = []
        for block in self.text:
            tmp = np.dot(self.invert_key_matrix, block) % len(self.alphabet)
            message.append(tmp)
        message = np.array(message).flatten()
        encrypted_text = [self.get_letter(int(number)) for number in message]
        return "".join(encrypted_text)

    def decode(self):
        if self.prepare_data():
            decrypted_text = self.decrypt()
            return decrypted_text
        else:
            return ""
