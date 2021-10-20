if __name__ == '__main__':
    symbol = '2330.TW'
    amount = 3000
    price = 614
    print(symbol, amount, price, sep="&", end=",")  # end 的預設是斷行
    print(symbol, amount, price, sep='&')
