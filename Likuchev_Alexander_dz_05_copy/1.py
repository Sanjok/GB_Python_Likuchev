"""
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
1
# >>> next(odd_to_15)
3
...
# >>> next(odd_to_15)
15
# >>> next(odd_to_15)
...StopIteration...
"""


def odd_nums(number):
    for num in range(1, number + 1, 2):
        yield num


odd_to_15 = odd_nums(15)
for i in range(15):
    print(next(odd_to_15))


