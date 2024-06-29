'''Определите сумму всех элементов последовательности, завершающейся
числом 0.
'''
def task_6():

    num_for_append = int(input())
    list_for_execute = []

    while num_for_append != 0:
        list_for_execute.append(num_for_append)
        num_for_append = int(input())

    return sum(list_for_execute)
result = task_6()
print(result)