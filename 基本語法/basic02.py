import math
if __name__ == '__main__':
    r = 123
    # 求出圓面積與球體積 (利用 math API)
    area = math.pi * math.pow(r, 2)
    volume = math.pi * math.pow(r, 2) * (4/3)
    print("圓面積 = %.2f" % area)
    print("球面積 = %.2f" % volume)
    print("圓面積 = ", format(float("%.2f" % area), ","))

