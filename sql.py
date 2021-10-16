import sqlite3 as sql


def sql_insert(cur, tag_name, words_list):
    cur.execute(f"INSERT INTO `Tags` VALUES ('{tag_name}', '{words_list}')")
    con.commit()


def sql_fetch(cur, tag_name):
    cur.execute(f"select * from Tags where Tag='{tag_name}'")
    rows = cur.fetchall()
    return rows


def sql_select_tags(tag, list_of_words):
    if list_of_words != '':
        sql_insert(cur, tag, list_of_words)
        print('Данные успешно добавлены в базу данных')
    else:
        print('Данные не были добавлены в базу данных')


def sql_close():
    con.commit()
    cur.close()


con = sql.connect('Database.db')  # подключение к бд
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS `Tags` (`Tag` STRING, `Words` STRING)")
