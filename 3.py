"""
3. Реализовать склонение слова «процент» для чисел до 20.
Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента».
Вывести все склонения для проверки.
"""

words = ['процентов', 'процент', 'процента']

# p = int(input('Введите количество процентов: '))
# if p < 0 or p > 20:
#     print('Введите число от 0 до 20!')
# elif p == 0 or p >= 5:
#     print(p, words[0])
# elif p == 1:
#     print(p, words[1])
# elif 2 <= p <= 4:
#     print(p, words[2])

i = 0
while i <= 20:
    if i < 0 or i > 20:
        print('Введите число от 0 до 20!')
    elif i == 0 or i >= 5:
        print(i, words[0])
    elif i == 1:
        print(i, words[1])
    elif 2 <= i <= 4:
        print(i, words[2])
    i += 1

