from helper import sanitizer, cutter, found_duplication
from sql import cursor, database_loads
from typing import List, Dict


def reply_output(text: str, dict_output: Dict[str, Dict[str, int]]) -> List[str]:
    output_size = 3

    clear_problem_text: str = sanitizer(text)  # Удаление знаков припенания
    splited_problem_text: list = clear_problem_text.split()

    default_weight_list = {}.fromkeys(dict_output.keys(), 0)  # создаем словарь для определения веса тэга, по умолчанию 0

    cutted_words_list: list = cutter(splited_problem_text)

    reply_list: list = found_duplication(dict_output, default_weight_list, cutted_words_list)  # отправляем значения в функцию для определения веса тэга
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
DATABASE_OUTPUT: List[Dict[str, Dict[str, int]]] = database_loads(cursor)

print(reply_output(MOCK_PROBLEM_TEXT, DATABASE_OUTPUT))
