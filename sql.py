import sqlite3 as sql
from typing import List, Tuple


def sql_insert(cur: sql.Cursor, tag_name: str, words_list: str) -> None:
    cur.execute(f"INSERT INTO `Tags` VALUES ('{tag_name}', '{words_list}')")
    con.commit()


def sql_fetch(cur: sql.Cursor, tag_name: str) -> List[Tuple[str]]:
    cur.execute(f"select * from Tags where Tag='{tag_name}'")
    rows = cursor.fetchall()
    return rows


def sql_select_tags(tag: str, list_of_words: str) -> None:
    if list_of_words != '[]':
        sql_insert(cursor, tag, list_of_words)
        print('Данные успешно добавлены в базу данных')
    else:
        print('Данные не были добавлены в базу данных')


def sql_close() -> None:
    con.commit()
    cursor.close()


con = sql.connect('Database.db')  # подключение к бд
with con:
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Tags` (`Tag` STRING, `Words` STRING)")
