'''Дана строка, в которой буква  h  встречается как минимум два раза.
Разверните последовательность символов, заключенную между первым и
последним появлением буквы  h , в противоположном порядке.
'''
def task_11():
    str_for_valid = input()

    start_index = str_for_valid.find('h')
    end_index = - str_for_valid[::-1].find('h')

    reverse_str_start_end = str_for_valid[start_index + 1: end_index][::-1]

    print(f"Перевёрнутая строка между буквами: {reverse_str_start_end}")

    complete = str_for_valid[:start_index] + reverse_str_start_end + str_for_valid[end_index-1::+1]

    return complete

result = task_11()
print(result)
