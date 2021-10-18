from helper import sanitizer, cutter, dict_creater, found_duplication, database_loads
from sql import cursor
from typing import List


def reply_output(text: str, data: List) -> List[str]:
    output_size = 3

    dict_output: dict = dict_creater(data)

    clear_problem_text: str = sanitizer(text)  # Удаление знаков припенания
    splited_problem_text: list = clear_problem_text.split()

    default_weight_list = [['wrong_future', 0],
                           ['due', 0],
                           ['mind_reading', 0],
                           ['black_and_white_thinking', 0],
                           ['catastrophization', 0],
                           ['generalization', 0],
                           ['filtering', 0],
                           ['disqualification_positive', 0],
                           ['jumping_conclusions', 0],
                           ['exaggeration_understatement', 0],
                           ['emotions_conclusions', 0],
                           ['possible', 0],
                           ['labels', 0],
                           ['responsibility', 0]
                           ]

    cutted_words_list: list = cutter(splited_problem_text)

    reply_list: list = found_duplication(dict_output, default_weight_list, cutted_words_list)
    reply_list.sort(key=lambda x: x[1], reverse=True)

    ans = []
    for i in range(output_size):
        if reply_list[i][0] != 0:
            ans.append(reply_list[i][0])
    return ans


MOCK_PROBLEM_TEXT: str = 'Я совершил ошибку и всегда буду их совершать!!!!!!!'.lower()
DATABASE_OUTPUT: list = database_loads(cursor)

print(reply_output(MOCK_PROBLEM_TEXT, DATABASE_OUTPUT))
