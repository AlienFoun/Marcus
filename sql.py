import json
import pymysql as sql
from typing import List, Tuple, Dict
from config import host, user, password, db_name


def sql_update(tag_name: str, words_list: str) -> None:
    cur = con.cursor()
    cur.execute(f"UPDATE `Tags` SET words = '{words_list}' WHERE tag = '{tag_name}'")
    print('The database has been successfully updated')
    con.commit()
    cur.close()


def sql_insert(tag_name: str, words_list: str) -> None:
    cur = con.cursor()
    cur.execute(f"INSERT INTO `Tags` (tag, words) VALUES ('{tag_name}', '{words_list}')")
    con.commit()
    cur.close()


def sql_fetch(tag_name: str) -> List[Tuple[str]]:
    cur = con.cursor()
    cur.execute(f"select tag, words from `Tags` where tag='{tag_name}'")
    rows = cur.fetchall()
    cur.close()
    return rows


def sql_close() -> None:
    con.commit()


def sql_set_default() -> None:
    cur = con.cursor()
    default_value = {}
    cur.execute(f"UPDATE `Tags` SET words = '{default_value}'")
    cur.close()
    print('Database brought to default values')


def database_loads() -> Dict[str, Dict[str, int]]:
    cur = con.cursor()
    cur.execute('SELECT tag, words FROM `Tags`')
    data_output = cur.fetchall()
    dict_data = {}
    for diction in data_output:
        updater = {diction[0]: json.loads(diction[1])}
        dict_data.update(updater)
    cur.close()
    return dict_data


con = sql.connect(host=host,
                  port=3306,
                  user=user,
                  password=password,
                  database=db_name)

cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS `Tags` (id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, tag text NOT NULL, words longtext NOT NULL)")
