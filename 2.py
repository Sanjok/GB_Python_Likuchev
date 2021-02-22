"""
2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
сумма цифр которых делится нацело на 7. Внимание: новый список не создавать!!!
"""

global_sum = 0
my_list = [1]
i = 3
while i <= 1000:
    if i % 2 != 0:
        my_list.append(i ** 3)
    i += 1
print(my_list)

for t in my_list:
    s = 0
    while t != 0:
        s += t % 10
        t = t // 10
    # print(t, '=', s)
    if s % 7 == 0:
        global_sum += s
print('The special sum of 1st list is ', global_sum)

for k in range(len(my_list)):
    my_list[k] += 17

for t in my_list:
    s = 0
    while t != 0:
        s += t % 10
        t = t // 10
    # print(t, '=', s)
    if s % 7 == 0:
        global_sum += s
print(my_list)
print('The special sum of 2nd list is ', global_sum)


