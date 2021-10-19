import sqlite3 as sql
import json
from typing import List, Tuple


def sql_update(cur: sql.Cursor, tag_name: str, words_list: str) -> None:
    cur.execute(f"UPDATE Tags SET Words = '{words_list}' WHERE Tag = '{tag_name}'")
    con.commit()

def sql_insert(cur: sql.Cursor, tag_name: str, words_list: str) -> None:
    cur.execute(f"INSERT INTO `Tags` VALUES ('{tag_name}', '{words_list}')")
    con.commit()

def sql_fetch(cur: sql.Cursor, tag_name: str) -> List[Tuple[str]]:
    cur.execute(f"select * from Tags where Tag='{tag_name}'")
    rows = cursor.fetchall()
    return rows


def sql_select_tags(tag: str, string_of_words: str) -> None:
    if string_of_words != '[]':
        sql_update(cursor, tag, string_of_words)
        print('The database has been successfully updated')
    else:
        print('An error occurred while updating the database')


def sql_close() -> None:
    con.commit()
    cursor.close()


def sql_set_default() -> None:
    default_value = json.dumps('')
    cursor.execute(f"UPDATE Tags SET Words = '{default_value}'")
    print('Database brought to default values')


def database_loads(cur) -> List[List[str]]:
    execution = cur.execute('select * from Tags')
    data = execution.fetchall()
    for i in range(len(data)):
        data[i] = list(data[i])
        data[i][1] = json.loads(data[i][1])
    return data


con = sql.connect('Database.db')  # подключение к бд
with con:
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Tags` (`Tag` STRING, `Words` STRING)")
