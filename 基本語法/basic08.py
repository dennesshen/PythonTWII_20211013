# 1. lamda parameter_list: expression
from functools import reduce

max = lambda a, b: a if a > b else b
print(max(10, 20))

# 2. (lamda parameter_list: expression)(arg)
print( (lambda a : a*a)(5) )

# 3. filter ( lambda parameter : expression, iterable)
# iterable : 數組
nums = [50, 2, 10, 40]
print( type(nums), nums )
result = filter(lambda x : x > 20, nums)
print(result, list(result))

# 4. map ( lambda parameter : expression, iterable)
# map 轉換
nums = [70, 2, 10, 0, 87]
result = map(lambda x: x > 60, nums)
print(list(result))
result = map(lambda x: "Pass" if x > 60 else "Fail", nums)
print(list(result))

# 5. reduce ( lambda parameter : expression, iterable)
# reduce 歸納
result = reduce(lambda x, y: x + y , nums)
print(result)

# 6. Sorted(iterable, key = lambda parameter : expression)
print(sorted(nums))
print(sorted(nums, reverse= True))

stocks = [('2330.TW', 599), ('2317.TW', 708), ('3008.TW', 2080)]
print(sorted(stocks))
print(sorted(stocks, key= lambda x: x[1]))