'''Дана строка. Замените в этой строке все появления буквы  h  на букву  H ,
кроме первого и последнего вхождения.
'''
def task_13():
    str_for_valid = input()

    start_index = str_for_valid.find('h')
    end_index = - str_for_valid[::-1].find('h')

    sres_for_swith_h = str_for_valid[start_index+1 : end_index - 1]

    list_for_join = []

    for i in sres_for_swith_h:
        if i == 'h':
            list_for_join.append('H')
        else:
            list_for_join.append(i)

    str_for_concat = ''.join(list_for_join)
    return str_for_valid[0:start_index+1] + str_for_concat + str_for_valid[end_index-1::+1]

result = task_13()
print(result)