# Генератор для четных чисел
def even_numbers(n):
    for a in range(n):
        if a % 2 == 0:
            yield a


for a in even_numbers(30 + 1):


# Печать четных чисел
        print("Четным числом в списке является: ", a)



