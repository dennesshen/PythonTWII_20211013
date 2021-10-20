"""
雞兔同籠
雞加兔子共有 83 隻，雞的腳加上兔子的腳共有 240 隻腳，求雞與兔子各有幾隻?
"""

totalHead = 83
totalFeet = 240

rabbit = (totalFeet - totalHead*2)/2
chicken = totalHead - rabbit
print("rabbit = ", rabbit)
print("chicken = ", chicken)
