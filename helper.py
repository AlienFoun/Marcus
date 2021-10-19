import string
import json
from sql import sql_fetch
from typing import List


def cutter(text: List[str]) -> List:
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
    return []


def appends(cursor, tag_name: str) -> List[str]:
    tag_list_name = []
    new_tags = []
    rows = sql_fetch(cursor, tag_name)
    for row in rows:
        words = json.loads(row[1])
        tag_list_name += words

    if rows == []:
        new_tags.append(tag_name)
    return tag_list_name, new_tags


def words_list_gen(lists: List, tag_list_name: List) -> List[str]:
    for element in lists:
        if element not in tag_list_name:
            tag_list_name.append(element)
    return tag_list_name


def sanitizer(clear_text: str) -> str:
    punc = string.punctuation
    for element in punc:
        clear_text = clear_text.replace(element, '')
    return clear_text


def dict_creater(data_list: List) -> dict:
    new_dict = {}
    for element in data_list:
        dict_updater = {element[0]: tuple(element[1])}
        new_dict.update(dict_updater)
    return new_dict


def found_duplication(data_dict: dict, weight_list: list, words_list: list) -> list:
    for element in weight_list:
        tag_words = data_dict.get(element[0]) # Получаем слова для определенного тэга из базы
        for word in words_list:  # Цикл для проверки наличия входных данных в значениях из базы
            if word in tag_words:  # Проверяем наличие
                element[1] += 1  # Прибавляем 1 к счетчику, который в списке тэгов
    return weight_list
