import random
words_used = []
block = ['ъ', 'ь', 'ы', '.']
file_path = r'C:\Users\Вадим\Desktop\Projects_Python\game_in_words\russian.txt'
word = 'а'
count = 1
count_2 = 2

def find_word_in_file(file_path):
    with open(file_path, 'r') as file:
        a = random.randint(1, 1531464)
        for line_number, line in enumerate(file, start=1):
            if line_number == a:
                words_used.append(line)
                return line
            # if word in line:
            #     print(f'Слово находится на строке {line_number}')

def find_word_in_file_2(file_path, word):
    with open(file_path, 'r') as file:
        for line in enumerate(file, start=1):
            if word in line[1] and line[1][0] == word and len(line[1])>3 and line[1] not in words_used:
                words_used.append(line[1])
                return line[1]
            else:
                continue


def inp_my_world(word_her):
    global count_2
    if word_her[-count_2] in block:
        while word_her[-count_2] in block:
            count_2 +=1
    my_word = input(f'Теперь твоя очередь, буква {word_her[-count_2]}: ')
    if my_word[0] == word_her[-count_2] and my_word not in words_used:
        with open(file_path, 'r') as file:
            for line in enumerate(file, start=1):
                if my_word in line[1]:
                    words_used.append(my_word)
                    count_2 = 2
                    return my_word
            print('Такого слова в списке нет')
    else:
        if my_word in words_used:
            print('Слово уже было использовано')
        else:
            print('Слово начинается на другую букву')
    count_2 = 2
        
word_her = find_word_in_file(file_path)
if len(word_her) == 1:
        while len(word_her) == 1:
            word_her = find_word_in_file(file_path)
while True:
    print(f'Моё слово: {word_her}')
    my_wordd = inp_my_world(word_her)
    if my_wordd == None:
        while my_wordd == None:
            my_wordd = inp_my_world(word_her)
    if my_wordd[-count] in block:
        while my_wordd[-count] in block:
            count += 1
    word_her = find_word_in_file_2 (file_path, my_wordd[-count])
    count = 1

