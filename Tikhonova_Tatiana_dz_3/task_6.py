# 6.Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text.


def int_func(word):
    big_letters = []
    list_words = word.split()
    for word in list_words:
        """перебор, у каждого слова в списке меняю первую букву, далее конкатенация с оставшимся словом"""
        big_letter = chr(ord(word[0]) - ord('a') + ord('A'))
        word = big_letter + word[1:]
        big_letters.append(word)
    return ' '.join(big_letters)


print(int_func('hello'))
print(int_func('how are you doing'))
