import sqlite3 as sql
import string


def cutter(text):
    total = []  # Создание списка для вывода
    n = 0  # Счетчик количества символов
    while ' '.join(text) not in total:  # Проверка, находится ли входной текст в списке вывода
        prom = []  # создание/очистка промежуточного списка
        i = 0  # Счетчик цикла
        while i < len(text):
            prom.append(text[i])  # Добавляем элементы в промежуточный список
            if len(prom) == n + 1:  # Нужно нарезать список сначала по одному слову,
                # потом по 2, 3 и т.д., тут происходит проверка на количество символов
                total.append(' '.join(prom))  # Если верно, то добавляем в список вывода
                prom = []  # Очищаем промежуточный список
                i -= n  # Сдвигаемся на n индексов назад
            i += 1
        n += 1
    return total  # Возвращаем список вывода


def sql_insert(cur, tag_name, words_list):
    cur.execute(f"INSERT INTO `Tags` VALUES ('{tag_name}', '{words_list}')")
    con.commit()


def sql_fetch(cur, tag_name):
    if tag_name == 'неверное понимание будущего':
        cur.execute("select * from Tags where Tag='неверное понимание будущего'")
    elif tag_name == 'долженствование':
        cur.execute("select * from Tags where Tag='долженствование'")
    elif tag_name == 'чтение мыслей':
        cur.execute("select * from Tags where Tag='чтение мыслей'")
    elif tag_name == 'черно-белое мышление':
        cur.execute("select * from Tags where Tag='черно-белое мышление'")
    elif tag_name == 'катастрофизация':
        cur.execute("select * from Tags where Tag='катастрофизация'")
    elif tag_name == 'обобщение':
        cur.execute("select * from Tags where Tag='обобщение'")
    elif tag_name == 'фильтрация':
        cur.execute("select * from Tags where Tag='фильтрация'")
    elif tag_name == 'дисквалификация положительного':
        cur.execute("select * from Tags where Tag='дисквалификация положительного'")
    elif tag_name == 'скачущие умозаключения':
        cur.execute("select * from Tags where Tag='скачущие умозаключения'")
    elif tag_name == 'преувеличение и преуменьшение':
        cur.execute("select * from Tags where Tag='преувеличение и преуменьшение'")
    elif tag_name == 'выводы на эмоциях':
        cur.execute("select * from Tags where Tag='выводы на эмоциях'")
    elif tag_name == 'можно было бы':
        cur.execute("select * from Tags where Tag='можно было бы'")
    elif tag_name == 'ярлыки':
        cur.execute("select * from Tags where Tag='ярлыки'")
    elif tag_name == 'ответственность за независящие от тебя события':
        cur.execute("select * from Tags where Tag='ответственность за независящие от тебя события'")

    rows = cur.fetchall()
    return rows


def appends(cur, tag_name):
    tag_list_name = []
    rows = sql_fetch(cur, tag_name)
    for row in rows:
        words = row[1].split(' | ')
        for i in range(len(words)):
            tag_list_name.append(words[i])
    return tag_list_name


def words_list_gen(lists, tag_list_name):
    not_join_words_list = []
    for i in range(len(lists)):
        if lists[i] not in tag_list_name:
            not_join_words_list.append(cutted_words_list[i])
    return not_join_words_list


def sql_select_tags(tag, list_of_words):
    if list_of_words != '':
        if tag == wrong_future:
            sql_insert(cur, wrong_future, list_of_words)
        elif tag == due:
            sql_insert(cur, due, list_of_words)
        elif tag == mind_reading:
            sql_insert(cur, mind_reading, list_of_words)
        elif tag == black_and_white_thinking:
            sql_insert(cur, black_and_white_thinking, list_of_words)
        elif tag == catastrophization:
            sql_insert(cur, catastrophization, list_of_words)
        elif tag == generalization:
            sql_insert(cur, generalization, list_of_words)
        elif tag == filtering:
            sql_insert(cur, filtering, list_of_words)
        elif tag == disqualification_positive:
            sql_insert(cur, disqualification_positive, list_of_words)
        elif tag == jumping_conclusions:
            sql_insert(cur, jumping_conclusions, list_of_words)
        elif tag == exaggeration_understatement:
            sql_insert(cur, exaggeration_understatement, list_of_words)
        elif tag == emotions_conclusions:
            sql_insert(cur, emotions_conclusions, list_of_words)
        elif tag == possible:
            sql_insert(cur, possible, list_of_words)
        elif tag == labels:
            sql_insert(cur, labels, list_of_words)
        elif tag == responsibility:
            sql_insert(cur, responsibility, list_of_words)

        print('Данные успешно добавлены в базу данных')
    else:
        print('Данные не были добавлены в базу данных')


con = sql.connect('Database.db') # подключение к бд
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS `Tags` (`Tag` STRING, `Words` STRING)")

    # Problem_Text = input('Введите текст проблемы: ').lower()
    # Problem_Tags = input('Введите теги, относящиеся к проблеме через запятую: ').split(', ')

    Problem_Text = 'Я совершил ошибку и всегда буду их совершать!!!!!!!'.lower()
    Problem_Tags = 'Неверное понимание будущего, Долженствование'.lower().split(', ')

    # Удаление знаков припенания
    punc = string.punctuation
    for i in range(len(punc)):
        Problem_Text = Problem_Text.replace(punc[i], '')
    Problem_Text = Problem_Text.split()

    wrong_future = 'неверное понимание будущего'
    due = 'долженствование'
    mind_reading = 'чтение мыслей'
    black_and_white_thinking = 'черно-белое мышление'
    catastrophization = 'катастрофизация'
    generalization = 'обощение'
    filtering = 'фильтрация'
    disqualification_positive = 'дисквалификация положительного'
    jumping_conclusions = 'скачущие умозаключения'
    exaggeration_understatement = 'преувеличение и преуменьшение'
    emotions_conclusions = 'выводы на эмоциях'
    possible = 'можно было бы'
    labels = 'ярлыки'
    responsibility = 'ответственность за независящие от тебя события'

    wrong_future_list = []
    due_list = []
    mind_reading_list = []
    black_and_white_thinking_list = []
    catastrophization_list = []
    generalization_list = []
    filtering_list = []
    disqualification_positive_list = []
    jumping_conclusions_list = []
    exaggeration_understatement_list = []
    emotions_conclusions_list = []
    possible_list = []
    labels_list = []
    responsibility_list = []

    # if Problem_Tags == ['']:

    if wrong_future in Problem_Tags:
        wrong_future_list = appends(cur, wrong_future)
    if due in Problem_Tags:
        due_list = appends(cur, due)
    if mind_reading in Problem_Tags:
        mind_reading_list = appends(cur, mind_reading)
    if black_and_white_thinking in Problem_Tags:
        black_and_white_thinking_list = appends(cur, black_and_white_thinking)
    if catastrophization in Problem_Tags:
        catastrophization_list = appends(cur, catastrophization)
    if generalization in Problem_Tags:
        generalization_list = appends(cur, generalization)
    if filtering in Problem_Tags:
        filtering_list = appends(cur, filtering)
    if disqualification_positive in Problem_Tags:
        disqualification_positive_list = appends(cur, disqualification_positive)
    if jumping_conclusions in Problem_Tags:
        jumping_conclusions_list = appends(cur, jumping_conclusions)
    if exaggeration_understatement in Problem_Tags:
        exaggeration_understatement_list = appends(cur, exaggeration_understatement)
    if emotions_conclusions in Problem_Tags:
        emotions_conclusions_list = appends(cur, emotions_conclusions)
    if possible in Problem_Tags:
        possible_list = appends(cur, possible)
    if labels in Problem_Tags:
        labels_list = appends(cur, labels)
    if responsibility in Problem_Tags:
        responsibility_list = appends(cur, responsibility)

    cutted_words_list = cutter(Problem_Text)

    if wrong_future_list != []:
        words_list = ' | '.join(words_list_gen(cutted_words_list, wrong_future_list))
        sql_select_tags(wrong_future, words_list)
    elif wrong_future_list == [] and wrong_future in Problem_Tags:
        words_list = ' | '.join(cutted_words_list)
        sql_select_tags(wrong_future, words_list)

    if due_list != []:
        words_list = ' | '.join(words_list_gen(cutted_words_list, due_list))
        sql_select_tags(due, words_list)
    elif due_list == [] and due in Problem_Tags:
        words_list = ' | '.join(cutted_words_list)
        sql_select_tags(due, words_list)

    if mind_reading_list != []:
        words_list = ' | '.join(words_list_gen(cutted_words_list, mind_reading_list))
        sql_select_tags(mind_reading, words_list)
    elif mind_reading_list == [] and mind_reading in Problem_Tags:
        words_list = ' | '.join(cutted_words_list)
        sql_select_tags(mind_reading, words_list)

    if black_and_white_thinking_list != []:
        words_list = ' | '.join(words_list_gen(cutted_words_list, black_and_white_thinking))
        sql_select_tags(black_and_white_thinking, words_list)
    elif black_and_white_thinking_list == [] and black_and_white_thinking in Problem_Tags:
        words_list = ' | '.join(cutted_words_list)
        sql_select_tags(black_and_white_thinking, words_list)

    if catastrophization_list != []:
        words_list = ' | '.join(words_list_gen(cutted_words_list, catastrophization))
        sql_select_tags(catastrophization, words_list)
    elif catastrophization_list == [] and catastrophization in Problem_Tags:
        words_list = ' | '.join(cutted_words_list)
        sql_select_tags(catastrophization, words_list)

    if generalization_list != []:
        words_list = ' | '.join(words_list_gen(cutted_words_list, generalization))
        sql_select_tags(generalization, words_list)
    elif generalization_list == [] and generalization in Problem_Tags:
        words_list = ' | '.join(cutted_words_list)
        sql_select_tags(generalization, words_list)

    if filtering_list != []:
        words_list = ' | '.join(words_list_gen(cutted_words_list, filtering))
        sql_select_tags(filtering, words_list)
    elif filtering_list == [] and filtering in Problem_Tags:
        words_list = ' | '.join(cutted_words_list)
        sql_select_tags(filtering, words_list)

    if disqualification_positive_list != []:
        words_list = ' | '.join(words_list_gen(cutted_words_list, disqualification_positive))
        sql_select_tags(disqualification_positive, words_list)
    elif disqualification_positive_list == [] and disqualification_positive in Problem_Tags:
        words_list = ' | '.join(cutted_words_list)
        sql_select_tags(disqualification_positive, words_list)

    if jumping_conclusions_list != []:
        words_list = ' | '.join(words_list_gen(cutted_words_list, jumping_conclusions))
        sql_select_tags(jumping_conclusions, words_list)
    elif jumping_conclusions_list == [] and jumping_conclusions in Problem_Tags:
        words_list = ' | '.join(cutted_words_list)
        sql_select_tags(jumping_conclusions, words_list)

    if exaggeration_understatement_list != []:
        words_list = ' | '.join(words_list_gen(cutted_words_list, exaggeration_understatement))
        sql_select_tags(exaggeration_understatement, words_list)
    elif exaggeration_understatement_list == [] and exaggeration_understatement in Problem_Tags:
        words_list = ' | '.join(cutted_words_list)
        sql_select_tags(exaggeration_understatement, words_list)

    if emotions_conclusions_list != []:
        words_list = ' | '.join(words_list_gen(cutted_words_list, emotions_conclusions))
        sql_select_tags(emotions_conclusions, words_list)
    elif emotions_conclusions_list == [] and emotions_conclusions in Problem_Tags:
        words_list = ' | '.join(cutted_words_list)
        sql_select_tags(emotions_conclusions, words_list)

    if possible_list != []:
        words_list = ' | '.join(words_list_gen(cutted_words_list, possible))
        sql_select_tags(possible, words_list)
    elif possible_list == [] and possible in Problem_Tags:
        words_list = ' | '.join(cutted_words_list)
        sql_select_tags(possible, words_list)

    if labels_list != []:
        words_list = ' | '.join(words_list_gen(cutted_words_list, labels))
        sql_select_tags(labels, words_list)
    elif labels_list == [] and labels in Problem_Tags:
        words_list = ' | '.join(cutted_words_list)
        sql_select_tags(labels, words_list)

    if responsibility_list != []:
        words_list = ' | '.join(words_list_gen(cutted_words_list, responsibility))
        sql_select_tags(responsibility, words_list)
    elif responsibility_list == [] and responsibility in Problem_Tags:
        words_list = ' | '.join(cutted_words_list)
        sql_select_tags(responsibility, words_list)

    con.commit()
    cur.close()
