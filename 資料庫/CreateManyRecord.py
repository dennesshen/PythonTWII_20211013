import sqlite3
# 建立資料庫與資料表

conn = sqlite3.connect("tw_stock.db")

insert_sql = '''
    insert into portfolio(symbol, cost, amount, ts) 
    values(?, ?, ?, ?)
    '''
datas = [
    ('2303', 50, 7000, '2021-11-3'),
    ('2317', 110, 6000, '2021-11-3'),
    ('2449', 70.5, 4000, '2021-11-3')
]


cursor = conn.cursor()
cursor.executemany(insert_sql, datas)

conn.commit()
conn.close()
