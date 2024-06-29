'''Дан список. Выведите те его элементы, которые 
встречаются в списке только
один раз. Элементы нужно выводить в том порядке, в котором они
встречаются в списке.
'''
def task_17():
    list_for_valid = list(map(int, input().split()))
    list_for_return = []
    for i in list_for_valid:
        if list_for_valid.count(i) == 1:
            list_for_return.append(str(i))
    return " ".join(list_for_return)