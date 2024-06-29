'''Определите среднее значение всех элементов последовательности,
завершающейся числом 0.
'''
def task_7():

    num_for_append = int(input())
    list_for_execute = []

    while num_for_append != 0:
        list_for_execute.append(num_for_append)
        num_for_append = int(input())

    return int(sum(list_for_execute) / len(list_for_execute))
result = task_7()
print(result)