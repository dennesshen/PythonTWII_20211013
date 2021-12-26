import sqlite3
# 建立資料庫與資料表

conn = sqlite3.connect("tw_stock.db")

insert_sql = '''
    insert into portfolio(symbol, cost, amount, ts) 
    values('%s', '%f', '%d', '%s')
    ''' \
    % ('2330', 5000, 499, '2021-11-3')

cursor = conn.cursor()
cursor.execute(insert_sql)

conn.commit()
conn.close()
