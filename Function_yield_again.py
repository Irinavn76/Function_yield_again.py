# Генератор  для четных чисел
def even_numbers(n):
    for a in range(n):
        if a % 2 == 0:
            yield a


# Печать четных чисел
print("Четными числами в списке являются: ")
for a in even_numbers(30+1):
    print(a)
