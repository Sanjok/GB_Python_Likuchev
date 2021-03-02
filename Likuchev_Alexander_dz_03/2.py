"""
2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными,
 начинающимися с заглавной буквы. Например:
# >>> >>> num_translate_adv("One")
"Один"
# >>> num_translate_adv("two")
"два"
"""


def num_translate_adv(number):
    if number.istitle():
        print(numbers.get(number.lower()).title())
    else:
        print(numbers.get(number))


numbers = {
    'null': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

num_translate_adv("one")
num_translate_adv("One")
num_translate_adv("eight")
