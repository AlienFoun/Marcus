import json
from helper import appends, words_list_gen, sanitizer, cutter
from sql import cursor, sql_select_tags, sql_close
from typing import Dict, List


def update_problems_dict(text: str, tags: List[str]) -> None:
    clear_problem_text: str = sanitizer(text)  # Удаление знаков припенания
    splited_problem_text: list = clear_problem_text.split()

    problems_dict: dict = {}
    for tag in tags:
        dict_gen: Dict[str, list] = {tag: []}
        problems_dict.update(dict_gen)
    '''    
    Problems_dict = {
        'wrong_future': [],
        'due': [],
        'mind_reading': [],
        'black_and_white_thinking': [],
        'catastrophization': [],
        'generalization': [],
        'filtering': [],
        'disqualification_positive': [],
        'jumping_conclusions': [],
        'exaggeration_understatement': [],
        'emotions_conclusions': [],
        'possible': [],
        'labels': [],
        'responsibility': []
    }
    '''

    for tag in tags:
        new_value: List[str] = appends(cursor, tag)
        dict_updater: Dict[str, List[str]] = {tag: new_value}
        problems_dict.update(dict_updater)

    cutted_words_list: List[str] = cutter(splited_problem_text)

    for tag in tags:
        dict_value = problems_dict.get(tag)
        words_list = json.dumps(cutted_words_list if dict_value == []
                                else words_list_gen(cutted_words_list, dict_value))
        sql_select_tags(tag, words_list)

    sql_close()


MOCK_PROBLEM_TEXT: str = 'Я совершил ошибку и всегда буду их совершать!!!!!!!'.lower()
MOCK_PROBLEM_TAGS: list = ['due']

update_problems_dict(MOCK_PROBLEM_TEXT, MOCK_PROBLEM_TAGS)
