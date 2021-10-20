"""
雞兔同籠
雞加兔子共有 83 隻，雞的腳加上兔子的腳共有 240 隻腳，求雞與兔子各有幾隻?
"""


def get_rabbit_and_chicken(total_head, total_feet):

    if total_head * 2 <= total_feet <= total_head * 4:
        rabbit = (total_feet - total_head * 2) / 2
        chicken = total_head - rabbit
        return rabbit, chicken
    else:
        return False


if __name__ == '__main__':
    result = get_rabbit_and_chicken(83, 240)
    if result is False:
        print("參數錯誤")
    else:
        rabbitResult, chickenResult = result[0], result[1]
        print("rabbit = ", rabbitResult, "chicken = ", chickenResult)
