"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import default_timer, timeit


def time_it(func):
    def wrapper(*args):
        print(timeit(f"{func(*args)}", globals=globals(), number=1000))
        # start_time = default_timer()
        # func(numb)
        # print(default_timer() - start_time)
    return wrapper


@time_it
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@time_it
def func_2(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


NUMS = [el for el in range(1000)]
NUMS_2 = [el for el in range(1000000)]


# func_1(7)

# func_1(NUMS)
print("Замеры первой и второй функции со значением 1 000 ")
func_1(NUMS)
func_2(NUMS)
print("_"*100)
print("Замеры первой и второй функции со значением 1 000 000 ")
func_1(NUMS_2)
func_2(NUMS_2)

"""
Был сделан замер времени с помощью декоратора:
Были получены замеры по времени по функциям, в которых использовались:
1) добавление элементов после перебора эелементов в массиве с помощью append
2) list comprehension
Результаты измерений немного отличаются, list comprehension работает быстрее.
В случае с 1 000 элементов в массиве на 8,00 %
В случае с 1 000 000 элементов в массиве на 1,0 % 
"""