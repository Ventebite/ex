'''
Дан текст: в первой строке записано число строк, далее идут сами строки.
Определите, сколько различных слов содержится в этом тексте.
Словом считается последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом пробелов или
символами конца строки.
'''

def task_20():
    text_list_num = int(input())
    unique_words = set()
    for i in range(text_list_num):
        str_for_add = input().split()
        for y in str_for_add:
            unique_words.add(y)
    return len(unique_words)
result = task_20()
print(result)
