''' Напишите программу, которая принимает 3 числа - стороны треугольника и
проверяет, является ли треугольник равносторонним ( equilateral ),
равнобедренным ( isosceles ) или общего вида ( scalene ).'''
def task_4():
    list_of_num = list(map(int, input().split() ) )

    for i in list_of_num:

        if list_of_num.count(i) == 2:
            return 'isosceles'

        if list_of_num.count(i) == 3:
            return 'equilateral'

        else:
            return 'scalene'