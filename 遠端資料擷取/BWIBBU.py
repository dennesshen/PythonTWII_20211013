import requests
def getData(yyyy, mm, dd):

    month = "%02d" % mm
    day = "%02d" % dd
    yyyymmdd = str(yyyy)+ month + day
    url = "https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=%s&selectType=ALL" %yyyymmdd
    print(url)
    data = requests.get(url).text
    data = data.split("\r\n")
    # print(type(data), data)

    list = [] # 用來存放整理好的資料
    for d in data:
        d = d.replace('"' , '')
        array = d.split(",")
        if len(array) == 8 and array[0] != '證券代號':
            row = (
                array[0],
                array[1],
                float(array[2]) if array[2] != '-' else -1,
                float(array[4]) if array[4] != '-' else -1,
                float(array[5]) if array[5] != '-' else -1,
                str(yyyy)+"-"+str(mm)+"-"+str(dd)
            )
            list.append(row)
    return list


