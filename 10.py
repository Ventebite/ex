''' Дана строка, в которой буква  h  встречается минимум
 два раза. Удалите из
этой строки первое и последнее вхождение буквы  h , а также все символы,
находящиеся между ними'''
def task_10(): #Задание на переворачивание строки и нахождение символа
    str_for_valid = input()

    stat_index = str_for_valid.find('h')
    print(f"Первый индекс: {stat_index}")

    end_index = - str_for_valid[::-1].find('h')
    print(f"Последний индекс: {end_index}")

    print(f"Срез до первого индекса: {str_for_valid[:stat_index]}")

    print(f"Срез до последнего индекса: {str_for_valid[end_index::+1]}") #Не забываем про минус

    result_for_return = str_for_valid[:stat_index] + str_for_valid[-end_index::+1]
    print(f"Результат выполнения слияния: {result_for_return}")
    return result_for_return
task_10()