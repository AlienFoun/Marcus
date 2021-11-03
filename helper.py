import json
import string
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
                    if len(' '.join(prom)) > 2:
                        total.append(' '.join(prom))  # Если верно, то добавляем в список вывода
                    prom = []  # Очищаем промежуточный список
                    i -= simbol  # Сдвигаемся на n индексов назад
                i += 1
            simbol += 1
        return total  # Возвращаем список вывода
    return []


def appends(rows: list) -> dict:
    tag_list_name = {}
    for row in rows:
        tag_list_name = json.loads(row[2])  # Преобразуем данные из формата json и берем только словарь из слов+их веса
    return tag_list_name


def words_dict_gen(lists: dict, tag_dict: dict) -> dict:
    input_dict_keys = lists.keys()  # Получаем все слова из словаря со входными данными
    database_dict_keys = tag_dict.keys()  # Получаем все слова из словаря из базы данных

    for element in input_dict_keys:
        new_value = {element: tag_dict[element] + lists[element]} if element in database_dict_keys \
            else {element: lists[element]}  # Создаем новое значение для словаря, которое равно:
        # 1 случай (если слово есть в словах из базы) - {Слово: Вес слова в словаре из базы + вес во входящем словаре}
        # 2 случай (если слова нет) - {Слово: Вес слова во входящем словаре}
        tag_dict.update(new_value)

    return tag_dict


def sanitizer(clear_text: str) -> str:
    return clear_text.translate({ord(i): None for i in string.punctuation})


def found_duplication(data_dict: dict, weight_dict: dict, words_list: list) -> list:
    dict_keys = list(weight_dict.keys())  # Получаем названия всех ошибок
    for element in dict_keys:
        tag_words = data_dict.get(element)  # Получаем словарь слов для определенной ошибки из базы

        words = list(tag_words.keys())  # Получаем слова

        for word in words_list:  # Цикл для проверки наличия входных данных в значениях из базы
            if word in words:  # Проверяем наличие
                new_weight = {element: weight_dict[element] + tag_words[word]}  # Создаем переменную для обновления веса
                weight_dict.update(new_weight)  # Обновляем

    return_list = list(weight_dict.items())  # метод .items возвращает все пары (ключ, значение) <- Кортеж
    # .items возвращает значения в виде динамической структуры,
    # переводим в список, чтобы удобнее было работать
    return return_list


def weight_input_calibrator(text: list) -> dict:
    if text == ['']:
        return {}  # Проверка входных данных
    text_dict = {}  # Создаем словарь, в котором будут храниться слова + их вес
    for value in text:
        new_values = {value: (len(value) // 5) + 1}  # Создаем переменную для обновления словаря в виде: {слово: вес}
        text_dict.update(new_values)  # Обновляем словарь
    return text_dict
