# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
"""
Функция сжатия данных - данные берутся из файла и записываются в финальный файл
"""

import sys


def compress(text):
    if text == "":
        return ""

    i = 0
    count = 1
    result = ''

    for i in range(len(text) - 1):
        if text[i+1] == text[i]:
            count += 1
        else:
            result += text[i] + str(count)
            count = 1
        text[i] == text[i - 1]

    result += text[i] + str(count)

    return result

"""
Функция разжатия данных - сжатые данные берутся из файла
"""


def decompress(text):
    i = 0
    result = ""
    while i < len(text):
        ch, count = text[i], ""
        i += 1
        while i < len(text) and '0' <= text[i] <= '9':
            count += text[i]
            i += 1

        result += ch * int(count)

    return result


def read_file(title):
    src = input(title)
    f = open(src, "r")
    data = f.read()
    f.close()

    return data


def write_file(title, data):
    dst = input(title)
    f = open(dst, "w")
    f.write(data)
    f.close()


command = input("Введите команду (compress|decompress): ")

if command == "compress":
    data = read_file("Файл с входными данными для сжатия: ")
    print(f"Сейчас мы будем сжимать данные: {data}")
    compressed = compress(data)
    print(f"Сжатые данные: {compressed}")
    write_file("Файл для сжатых данных: ", compressed)

elif command == "decompress":
    data = read_file("Файл с сжатыми данными: ")
    print(f"Сейчас мы будем разжимать данные: {data}")
    decompressed = decompress(data)
    print(f"Разжатые данные: {decompressed}")
    write_file("Файл для разжатых данных: ", decompressed)

else:
    print("Команда не найдена")
