import math

'''
股票交易成本計算
小明在股價 10 元時買了 Hero 公司股票 10 張，於 11 元全數賣出，
請問小明賺了多少？
提示：
1張 = 1000股
交易成本(台股)
手續費：股票價值 * 1.425(‰) 買賣股票時都要扣除(不足 20 元者以 20 元計算。)
證交稅：股票價值 * 3(‰) 賣出股票時才扣除
'''
feeRate = 0.001425
taxRate = 0.003
cell = 1000


def fee(tradeMoney):
    fee_return = 20 if tradeMoney * feeRate < 20 else math.floor(tradeMoney * feeRate)
    return fee_return


buyPrice = 10
buyAmount = 10
sellPrice = 11
sellAmount = 10

# 購買股票總花費
buyCost = buyPrice * buyAmount * cell
buy_fee = fee(buyCost)
totalCost = buyCost + buy_fee

# 賣股票總收入
sellMoney = sellPrice * sellAmount * cell
sell_fee = fee(sellMoney)
sellTax = sellMoney * taxRate

totalSell = sellMoney - sellTax - sell_fee

# 印出結果
print("購買", buyCost, buy_fee)
print("銷售", sellMoney, sellTax, sell_fee)
print(totalSell - totalCost)
