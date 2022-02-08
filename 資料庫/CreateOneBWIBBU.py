import time
import datetime

from 遠端資料擷取 import BWIBBU as bwi
import sqlite3

def create_table():
    sql = '''
        create table if not exists BWIBBU(
        id integer not null primary key autoincrement,
        symbol varchar(20) not null,
        name varchar(20) not null,
        yield float not null,
        pe float not null,
        pb float not null,
        ts date 
        )
        '''
    conn = sqlite3.connect("tw_stock.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

def create_record(list):
    sql = '''
        insert into BWIBBU(symbol, name, yield, pe, pb, ts) 
        values(?, ?, ?, ?, ?, ?)
        '''
    conn = sqlite3.connect("tw_stock.db")
    cursor = conn.cursor()
    cursor.executemany(sql, list)
    conn.commit()
    conn.close()
    print("ok")

def dateList(start_date, end_date):
    start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    date_list = []
    while start <= end:
        date_list.append(start.timetuple())
        start += datetime.timedelta(1)
    return date_list

if __name__ == '__main__':
    create_table()
    for i in dateList("2021-03-01", "2021-03-31"):
        list = bwi.getData(i[0], i[1] , i[2])
        print(list)
        create_record(list)
        time.sleep(20)