import string
from sql import sql_fetch


def cutter(text: str):
    total = []  # Создание списка для вывода
    n = 0  # Счетчик количества символов
    while ' '.join(text) not in total:  # Проверка, находится ли входной текст в списке вывода
        prom = []  # создание/очистка промежуточного списка
        for i in range(len(text)):
            prom.append(text[i])  # Добавляем элементы в промежуточный список
            if len(prom) == n + 1:  # Нужно нарезать список сначала по одному слову,
                # потом по 2, 3 и т.д., тут происходит проверка на количество символов
                total.append(' '.join(prom))  # Если верно, то добавляем в список вывода
                prom = []  # Очищаем промежуточный список
                i -= n  # Сдвигаемся на n индексов назад
        n += 1
    return total  # Возвращаем список вывода


def appends(cur, tag_name: str):
    tag_list_name = []
    rows = sql_fetch(cur, tag_name)
    for row in rows:
        words = row[1].split(' | ')
        for i in range(len(words)):
            tag_list_name.append(words[i])
    return tag_list_name


def words_list_gen(lists: list, tag_list_name: list):
    not_join_words_list = []
    for i in range(len(lists)):
        if lists[i] not in tag_list_name:
            not_join_words_list.append(lists[i])
    return not_join_words_list


def sanitizer(clear_text: str):
    punc = string.punctuation
    for i in range(len(punc)):
        clear_text = clear_text.replace(punc[i], '')
    return clear_text
