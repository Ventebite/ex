'''Последовательность состоит из натуральных чисел и завершается числом 0.
Определите индекс наибольшего элемента последовательности. Если
наибольших элементов несколько, выведите индекс первого из них.
Нумерация элементов начинается с нуля.'''
def task_9():

    num_for_append = int(input())
    list_for_execute = []

    while num_for_append != 0:
        list_for_execute.append(num_for_append)
        num_for_append = int(input())

    max_num = max(list_for_execute)
    index_max_num = None

    for num,value in enumerate(list_for_execute):
        if value == max_num:
            index_max_num = num

    return  index_max_num
result = task_9()
print(result)