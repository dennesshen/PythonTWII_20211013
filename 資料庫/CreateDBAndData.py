import sqlite3
# 建立資料庫與資料表

conn = sqlite3.connect("tw_stock.db")

creat_table_sql = '''

    create table if not exists portfolio(
        id integer not null primary key autoincrement,
        symbol text not null,
        cost float,
        amount integer,
        ts date 
        )
'''
cursor = conn.cursor()
cursor.execute(creat_table_sql)

conn.commit()
conn.close()
