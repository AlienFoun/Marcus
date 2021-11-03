import json
from helper import words_dict_gen, cutter, weight_input_calibrator
from sql import sql_update, sql_close, sql_insert, sql_fetch
from typing import Dict, List


def update_problems_dict(text: str, tags: list) -> None:
    lower_problem_text = text.lower()
    splited_problem_text: list = lower_problem_text.split()

    problems_dict = {}
    new_tags = []
    tuple_tags = tuple(tags)

    rows = sql_fetch(tuple_tags)  # Получаем значения из базы для ошибок в формате json в виде списка

    for i in range(len(tags)):

        if not rows[i]:  # Если для конкретной ошибки пустой вывод, то этой ошибки нет в базе
            new_tags.append(tags[i])  # Добавляем ее название в список для новых ошибок

        new_value: dict = json.loads(rows[i][0]) if rows else {}

        dict_updater: Dict[str, dict] = {tags[i]: new_value}  # Создаем переменную для обновления словаря, в виде
        # {Тэг: словарь из базы}
        problems_dict.update(dict_updater)

    cutted_words_list: List[str] = cutter(splited_problem_text)
    calebrated_words_list = weight_input_calibrator(cutted_words_list)  # выставление веса для входной строки

    for tag in tags:
        dict_value = problems_dict.get(tag)  # Получаем словарь из слов с их весом из базы для определенной ошибки
        words_list = json.dumps(calebrated_words_list if dict_value == []
                                else words_dict_gen(calebrated_words_list, dict_value), ensure_ascii=False)
        sql_update(tag, words_list)

    if new_tags:  # Если существуют новые ошибки, которых нет в базе
        words_list = json.dumps(calebrated_words_list,
                                ensure_ascii=False)  # Создаем переменную в формате json для внесения в базу
        for new_tag in new_tags:
            sql_insert(new_tag, words_list)

    sql_close()

# MOCK_PROBLEM_TEXT: str = 'Я совершил ошибку и всегда буду не их совершать!!!!!!!'.lower()
# MOCK_PROBLEM_TAGS: list = ['max']
