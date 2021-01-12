# 2.Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой
# строке.

with open('text_2.txt', 'r', encoding='utf-8') as f:
    file_content = f.read().splitlines()
    print(f'количество строк в файле: {len(file_content)}')
    for i, el in enumerate(file_content, 1):
        words = el.split()
        print(f'количество слов в {i} строке: {len(words)}')
