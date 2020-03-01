import requests
import sqlite3

conn = sqlite3.connect('homework.db')
cursor = conn.cursor()
try:
    cursor.execute(
        'create table  mywork (id INTEGER PRIMARY KEY AUTOINCREMENT, type varchar(255), item varchar(255))'
    )
except Exception as e:
    pass


def print_text(url, typ, num):
    l = []
    j = 1
    while True:
        r = requests.get(url, params={'from': 'liuting'})

        if r.text not in l:
            print(j, r.text)

        sql = 'SELECT COUNT(id) FROM mywork WHERE item = ?'
        value = conn.execute(sql, (r.text,)).fetchall()
        value = value[0][0]

        if value != 0:
            print('    发现重复的啦~')
            continue

        sql = 'INSERT INTO mywork (type, item) VALUES (?, ?)'
        cursor.execute(sql, (typ, r.text))
        conn.commit()
        j = j + 1
        l.append(r.text)
        if j >= num + 1:
            break


print_text('https://chp.shadiao.app/api.php', '彩虹屁', 20)
print_text('https://du.shadiao.app/api.php', '毒鸡汤', 20)
print_text('https://pyq.shadiao.app/api.php', '朋友圈', 20)
