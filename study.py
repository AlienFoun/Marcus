from helper import *
from sql import *
import json

def update_Problems_dict(text: str, tags: list):
    # Удаление знаков припенания
    clear_Problem_Text = sanitizer(text)
    Splited_Problem_Text = clear_Problem_Text.split()

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
        'responsibility': [],
    }

    for i in range(len(tags)):
        dict_problem_tag = tags[i]
        new_value = appends(cur, tags[i])
        dict_updater = {dict_problem_tag: new_value}
        Problems_dict.update(dict_updater)

    cutted_words_list = cutter(Splited_Problem_Text)

    for i in range(len(tags)):
        dict_value = Problems_dict.get(tags[i])
        words_list = json.dumps(words_list_gen(cutted_words_list, dict_value) if dict_value != [] else cutted_words_list)
        sql_select_tags(tags[i], words_list)

    sql_close()

Mock_Problem_Text = 'Я совершил ошибку и всегда буду их совершать!!!!!!!'.lower()
Mock_Problem_Tags = ['due']

update_Problems_dict(Mock_Problem_Text, Mock_Problem_Tags)
