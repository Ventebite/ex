'''
Реализуйте функцию, которая принимает в качестве первого аргумента строку,
а затем любое количество аргументов и возвращает строку, являющуюся
объединением всех аргументов разделенных строкой из первого аргумента.
Метод строк join не применять.
'''
def task_30(rasdel, *args):
    result = str(args[0])
    for arg in args[1:]:
        result += rasdel + str(arg)
    return result

