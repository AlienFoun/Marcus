import sqlite3 as sql
import json
from typing import List, Tuple


def sql_insert(cur: sql.Cursor, tag_name: str, words_list: str) -> None:
    cur.execute(f"UPDATE Tags SET Words = '{words_list}' WHERE Tag = '{tag_name}'")
    con.commit()


def sql_fetch(cur: sql.Cursor, tag_name: str) -> List[Tuple[str]]:
    cur.execute(f"select * from Tags where Tag='{tag_name}'")
    rows = cursor.fetchall()
    return rows


def sql_select_tags(tag: str, string_of_words: str) -> None:
    if string_of_words != '[]':
        sql_insert(cursor, tag, string_of_words)
        print('База данных была успешно обновлена')
    else:
        print('При обновлении базы данных произошла ошибка')


def sql_close() -> None:
    con.commit()
    cursor.close()


def sql_set_default() -> None:
    default_value = json.dumps('')
    cursor.execute(f"UPDATE Tags SET Words = '{default_value}'")
    print('База данных приведена к значениям по умолчанию')


con = sql.connect('Database.db')  # подключение к бд
with con:
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Tags` (`Tag` STRING, `Words` STRING)")
