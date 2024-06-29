'''
Переставьте соседние элементы списка ( A[0] c A[1] , A[2] c A[3] и т. д.).
Если элементов нечетное число, то последний элемент остается на своем
месте
'''
def task_15():
    input_int_list = list(map(int, input().split()))
    for i in range(0, len(input_int_list) - 1, 2):
        input_int_list[i], input_int_list[i + 1] = input_int_list[i + 1], input_int_list[i]
    return input_int_list

result = task_15()
print(task_15())
