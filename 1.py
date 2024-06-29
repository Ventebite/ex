'''
Напишите программу для проверки корректности пароля введенного
пользователем. Пароль должен иметь следующие свойства:
Не менее 1 буквы из диапазона a-z и 1 из диапазона A-Z
Не менее одной цифры в диапазоне 0-9
Не менее одного символа из $#@
Длина не менее 6 и не более 16 символов
'''
import string
string.ascii_lowercase
string.ascii_uppercase

def task_1 ():
    password = input()
    lower_upper = False
    numeric = False
    int_list = [1,2,3,4,5,6,7,8,9,0]
    secure_sym_list = ['$', '#', '@']
    secure_sym = False
    len_password = False
    for i in password:
        if i in string.ascii_lowercase and i in string.ascii_uppercase:
            lower_upper = True
        if int(i) in int_list:
            numeric = True
        if i in secure_sym_list:
            secure_sym = True
        if len(password) >= 6 and len(password) <= 16:
            len_password = True
        return lower_upper and numeric and secure_sym and len_password