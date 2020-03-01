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

    while True:
        r = requests.get(url, params={'from': 'liuting'})
        result_data = r.text

        sql = 'SELECT COUNT(id) FROM mywork WHERE item = ?'
        result = conn.execute(sql, (result_data,)).fetchall()
        result = result[0][0]

        if result > 0:  # 如果result大于0表示发现重复 跳过执行
            continue

        # 如果没有重复内容 则继续执行下面
        # 如果上面有重复内容，本身是没有做任何操作的，只是跳过，没有插入数据库，所以不用做计数以及调试查看

        sql = 'INSERT INTO mywork (type, item) VALUES (?, ?)'
        cursor.execute(sql, (typ, result_data))
        conn.commit()  # 提交到数据库

        # 插入了数据库 num 条内容后，跳出运行
        l.append(result_data)

        # 输出作为调试用
        print(len(l), result_data)
        if len(l) >= num:
            break




print_text('https://chp.shadiao.app/api.php', '彩虹屁', 20)
print_text('https://du.shadiao.app/api.php', '毒鸡汤', 20)
print_text('https://pyq.shadiao.app/api.php', '朋友圈', 20)
