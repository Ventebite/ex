'''
 Реализуйте функцию, которая принимает в качестве первого аргумента строку,
а затем любое количество именованных аргументов. Именованные аргументы
представляют собой множества. Принадлежность элемента к конкретному
множеству определяется по первому символу имени аргумента. Найти
объединение, пересечение или симметрическую разность полученных
множеств
'''


def task_31(operation_in_str, **kwargs):

    set_for_operation = {}

    for key, value in kwargs.items():
        if key[0] in operation_in_str:
            set_for_operation[key] = set(value)

 #Статик методы для множеств аля ООП из Java
    if 'or' in operation_in_str:  # Объединение
        result = set().union(*set_for_operation.values())
    elif 'and' in operation_in_str:  # Пересечение
        result = set().intersection(*set_for_operation.values())
    else:  # Симметрическая разность
        result = set().symmetric_difference(*set_for_operation.values())

    return result
