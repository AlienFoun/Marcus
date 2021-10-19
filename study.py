import json
from helper import appends, words_list_gen, sanitizer, cutter, weight_input_calibrator
from sql import cursor, sql_select_tags, sql_close, sql_insert
from typing import Dict, List


def update_problems_dict(text: str, tags: List[str]) -> None:
    clear_problem_text: str = sanitizer(text)  # Удаление знаков припенания
    splited_problem_text: list = clear_problem_text.split()

    problems_dict: dict = {}
    new_tags = []

    for tag in tags:
        dict_gen: Dict[str, list] = {tag: []}
        problems_dict.update(dict_gen)

    for tag in tags:
        new_value: List[str] = appends(cursor, tag)
        dict_updater: Dict[str, List[str]] = {tag: new_value[0]}
        problems_dict.update(dict_updater)
        new_tags += new_value[1]

    cutted_words_list: List[str] = cutter(splited_problem_text)
    calebrated_words_list = weight_input_calibrator(cutted_words_list)

    for tag in tags:
        dict_value = problems_dict.get(tag)
        words_list = json.dumps(calebrated_words_list if dict_value == ['']
                                else words_list_gen(calebrated_words_list, dict_value))
        sql_select_tags(tag, words_list)
        if new_tags:
            for new_tag in new_tags:
                sql_insert(cursor, new_tag, words_list)

    sql_close()


MOCK_PROBLEM_TEXT: str = 'Я совершил ошибку и всегда буду их совершать!!!!!!!'.lower()
MOCK_PROBLEM_TAGS: list = ['max']

update_problems_dict(MOCK_PROBLEM_TEXT, MOCK_PROBLEM_TAGS)
