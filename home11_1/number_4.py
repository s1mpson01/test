# Генератор чисел Фибоначчи
# Числа Фибоначчи — это последовательность чисел,
# начиная с 0 и 1, в которой каждое следующее число
# равно сумме двух предыдущих. Таким образом, последовательность
# выглядит следующим образом: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 и т. д.

def fibonacci():

    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fibonacci()
for i in range(10):
    print(next(f))