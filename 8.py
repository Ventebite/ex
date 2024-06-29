'''Последовательность состоит из натуральных чисел и завершается числом 0.
Определите значение наибольшего элемента последовательности'''
def task_8():

    num_for_append = int(input())
    list_for_execute = []

    while num_for_append != 0:
        list_for_execute.append(num_for_append)
        num_for_append = int(input())

    return max(list_for_execute)
result = task_8()
print(result)