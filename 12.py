'''Дана строка. Замените в этой строке все цифры  1  на слово  one .'''
def task_12():
    str_for_valid = input().split()

    final_list = []

    for i in str_for_valid:
        if i == '1':
            final_list.append("one")

        else:
            final_list.append(i)

    return ''.join(final_list)
result = task_12()
print(result)