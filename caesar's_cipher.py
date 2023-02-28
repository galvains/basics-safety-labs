
# Функция-генератор для индивидуального задания, использовал для перебора ключей сдвига.

def caesar_ind():

    s = 'х ёедягцф ние шцг дыныг, де шзь э ёеёжечйаиы ёедхит'
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    # alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''

    for count in range(1, 34):
        for elem in s:
            if elem in alphabet:
                result += alphabet[(alphabet.index(elem) + count) % len(alphabet)]
            else:
                result += elem

        yield (count, result)
        result = ''

# Функция для шифровки/дешифровки текста

str = input('Please input text: ')
key = int(input('key: '))
f = int(input('cipher/decipher (0 or 1): '))

def caesar(str, key, f):

    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    # alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''

    for elem in str:
        if elem in alphabet:
            if f == 0:
                result += alphabet[(alphabet.index(elem) + key) % len(alphabet)]
            else:
                result += alphabet[(alphabet.index(elem) - key) % len(alphabet)]
        else:
            result += elem
    print(result)

# Сортировка по последнему элементу (кол-во букв) в заданном тексте.

def by_count(elem):
    return elem[-1]

# Частотный анализ заданного текста с выводом в отдельный файл.

def frequency_analysis(str):

    result = []
    for i in set(str.replace(' ', '')):
        result.append([i, str.count(i)])

    with open('analysis.txt', 'w') as file:
        for line in sorted(result, key=by_count, reverse=True):
            file.write(f'{line[0]}: {line[-1]}\n')

if __name__ == '__main__':
    caesar(str, key, f)
    frequency_analysis(str)

    # for cipher in caesar_ind():
    #     print(f'{cipher[0]} | {cipher[-1]}')