# 19. Write a Python program to create Fibonacci series upto n using Lambda. 
from functools import reduce
num = 8
# list2 = [x for x in range(1,number_to_get_fibonachi+1)] 
# fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
# lmn = lambda x, _ : x+ [x[-1]+x[-2]]
# redc = reduce(lmn, range(num-2))
# fib_series = lambda num : redc , [0,1]
# fib_series = lambda num: reduce(lambda x, _: x+[x[-1]+x[-2]], range(num-2),[0,1] )


fib_series = lambda num: reduce(function=lambda x, _: x+[x[-1]+ x[-2]], sequence=range(num-2), initial= [0,1])

print(fib_series(8))
# reduce(lambda x : (x+x-1), list2)

# def fib(num:int) ->int:
#     num1 = 0
#     num2 = 1
#     for i in range(1, num+1):
#         new_num = num1 + num2
#         num1 = num2
#         num2 = new_num
#     return new_num
# print(fib(7))
