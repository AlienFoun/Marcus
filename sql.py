import sqlite3 as sql
import json
from typing import List, Tuple, Dict


def sql_update(tag_name: str, words_list: str) -> None:
    cur = con.cursor()
    cur.execute(f"UPDATE Tags SET Words = '{words_list}' WHERE Tag = '{tag_name}'")
    print('The database has been successfully updated')
    con.commit()
    cur.close()

def sql_insert(tag_name: str, words_list: str) -> None:
    cur = con.cursor()
    cur.execute(f"INSERT INTO `Tags` VALUES ('{tag_name}', '{words_list}')")
    con.commit()
    cur.close()


def sql_fetch(tag_name: str) -> List[Tuple[str]]:
    cur = con.cursor()
    cur.execute(f"select * from Tags where Tag='{tag_name}'")
    rows = cur.fetchall()
    cur.close()
    return rows


def sql_close() -> None:
    con.commit()


def sql_set_default() -> None:
    cur = con.cursor()
    default_value = json.dumps({})
    cur.execute(f"UPDATE Tags SET Words = '{default_value}'")
    cur.close()
    print('Database brought to default values')


def database_loads() -> Dict[str, Dict[str, int]]:
    cur = con.cursor()
    execution = cur.execute('select * from Tags')
    data_output = execution.fetchall()
    dict_data = {}
    for diction in data_output:
        updater = {diction[0]: json.loads(diction[1])}
        dict_data.update(updater)
    cur.close()
    return dict_data


con = sql.connect('Database.db', check_same_thread=False)  # подключение к бд

