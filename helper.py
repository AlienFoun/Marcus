import string
import json
from sql import sql_fetch


def cutter(text: list) -> list:
    if text != [] and isinstance(text, list):
        total = []  # Создание списка для вывода
        simbol = 0  # Счетчик количества символов
        while ' '.join(text) not in total:  # Проверка, находится ли входной текст в списке вывода
            prom = []  # создание/очистка промежуточного списка
            i = 0  # Счетчик цикла
            while i < len(text):
                prom.append(text[i])  # Добавляем элементы в промежуточный список
                if len(prom) == simbol + 1:  # Нужно нарезать список сначала по одному слову,
                    # потом по 2, 3 и т.д., тут происходит проверка на количество символов
                    total.append(' '.join(prom))  # Если верно, то добавляем в список вывода
                    prom = []  # Очищаем промежуточный список
                    i -= simbol  # Сдвигаемся на n индексов назад
                i += 1
            simbol += 1
        return total  # Возвращаем список вывода
    else:
        return []


def appends(cursor, tag_name: str) -> list:
    tag_list_name = []
    rows = sql_fetch(cursor, tag_name)
    for row in rows:
        words = json.loads(row[1])
        tag_list_name += words
    return tag_list_name


def words_list_gen(lists: list, tag_list_name: list) -> list:
    not_join_words_list = []
    for element in lists:
        if element not in tag_list_name:
            not_join_words_list.append(element)
    return not_join_words_list


def sanitizer(clear_text: str) -> str:
    punc = string.punctuation
    for element in punc:
        clear_text = clear_text.replace(element, '')
    return clear_text
