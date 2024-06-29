'''Напишите программу, которая принимает на вход 2 числа a и b и выводит
все числа в диапазоне от [a; b], в которых каждая цифра является четной.
Полученные числа вывести через запятую.'''
def task_3():
    int_for_range = list(map (int, input().split() ) )
    list_for_num = list(range(int_for_range[0],int_for_range[1]+1 ) )

    list_for_print = []
    for i in list_for_num:
        if i % 2 == 0:
            list_for_print.append(str(i))

    str_for_print = ','.join(list_for_print)
    print(str_for_print)

task_3()