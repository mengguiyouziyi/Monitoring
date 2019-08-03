import time
import pymysql

while True:
    time.sleep(1)
    time_now = time.strftime("%H:%M:%S", time.localtime())  # 刷新
    if time_now == "00:00:00":  # 此处设置每天定时的时间
        db = pymysql.connect(host='127.0.0.1', user='root', password='root', port=3306, db='django', charset="utf8", use_unicode=True)
        cursor = db.cursor()
        sql = """SELECT COUNT(id) FROM moniter_app_num"""
        cursor.execute(sql)
        db.commit()
        now_count = cursor.fetchone()[0]
        print(now_count)
        select_data = """SELECT monday,tuesday,wednesday,thursday FROM moniter_data_count"""
        cursor.execute(select_data)
        db.commit()
        data = cursor.fetchone()
        monday = data[0]
        tuesday = data[1]
        wednesday = data[2]
        thursday = data[3]
        print(monday, tuesday, wednesday, thursday)
        update_sql = """UPDATE `django`.`moniter_data_count` SET `monday`='%s', `tuesday`='%s', `wednesday`='%s', `thursday`='%s' WHERE (`id`='1');"""%(tuesday, wednesday, thursday, now_count)
        print(update_sql)
        cursor.execute(update_sql)
        db.commit()
        time.sleep(2)
    else:
        continue