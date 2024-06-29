'''
 Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг
другу. Считается, что любые два элемента, равные друг другу образуют одну
пару, которую необходимо посчитать.
Входные данные
'''

def tusk_16():
    input_list = list(map(int, input().split() ) )
    num_par = 0
    for i in input_list:
        if input_list.count(i)%2 == 0:
            num_par += 1
    if num_par > 0:
        return int(num_par/2)
    else:
        return 0