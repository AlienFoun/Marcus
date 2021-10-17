from sql import *
from helper import *

Mock_Problem_Text = 'Я совершил ошибку и всегда буду их совершать!!!!!!!'.lower()
Mock_Problem_Tags = ['due', 'mind_reading']

# Удаление знаков припенания
clear_Problem_Text = sanitizer(Mock_Problem_Text)
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

# if Mock_Problem_Tags == ['']:

for i in range(len(Mock_Problem_Tags)):
    dict_problem_tag = Mock_Problem_Tags[i]
    new_value = appends(cur, Mock_Problem_Tags[i])
    dict_updater = {dict_problem_tag: new_value}
    Problems_dict.update(dict_updater)

cutted_words_list = cutter(Splited_Problem_Text)

for i in range(len(Mock_Problem_Tags)):
    dict_value = Problems_dict.get(Mock_Problem_Tags[i])
    if dict_value != []:
        words_list = ' | '.join(words_list_gen(cutted_words_list, dict_value))
    else:
        words_list = ' | '.join(cutted_words_list)
    sql_select_tags(Mock_Problem_Tags[i], words_list)

sql_close()
