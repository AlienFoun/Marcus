from helper import sanitizer, cutter, dict_creater, found_duplication
from sql import cursor, database_loads
from typing import List


def reply_output(text: str, output_from_database: List) -> List[str]:
    output_size = 3

    dict_output: dict = dict_creater(output_from_database)

    clear_problem_text: str = sanitizer(text)  # Удаление знаков припенания
    splited_problem_text: list = clear_problem_text.split()

    default_weight_list = []
    for element in output_from_database:
        default_weight_list.append([element[0], 0])

    cutted_words_list: list = cutter(splited_problem_text)

    reply_list: list = found_duplication(dict_output, default_weight_list, cutted_words_list)
    reply_list.sort(key=lambda x: x[1], reverse=True)

    ans = []
    for i in range(output_size):
        try:
            if reply_list[i][1] != 0:
                ans.append(reply_list[i][0])
        except IndexError:
            return ans
    return ans


MOCK_PROBLEM_TEXT: str = 'Я совершил ошибку и всегда буду их совершать!!!!!!!'.lower()
DATABASE_OUTPUT: list = database_loads(cursor)

print(reply_output(MOCK_PROBLEM_TEXT, DATABASE_OUTPUT))
