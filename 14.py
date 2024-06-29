'''
Петя перешёл в другую школу. На уроке физкультуры ему понадобилось
определить своё место в строю. Помогите ему это сделать.
Программа получает на вход невозрастающую последовательность
натуральных чисел, означающих рост каждого человека в строю. После этого
вводится число X – рост Пети. Все числа во входных данных натуральные и
не превышают 200.
Выведите номер, под которым Петя должен встать в строй. Если в строю есть
люди с одинаковым ростом, таким же, как у Пети, то он должен встать после
них.
'''
# Прикол со ссылками в Питоне уже начинает чуточку бесить
def task_14():
    num_list = list(map(int, input().split() ) )
    Petya = int(input())
    index_petya = 0

    reverse_num_list = num_list[::-1].copy()

    for index, value in enumerate(reverse_num_list): #Поиск значения после которого должен встать Петя
        if value >= Petya:
            reverse_num_list.insert(index, Petya)
            break

    for index, value in enumerate(reverse_num_list[::-1]): # Нахождение индекса Пети
        if value == Petya:
            index_petya = index

    return index_petya + 1

result = task_14()
print(result)
