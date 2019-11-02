'''Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе'''

wrd1 = b'attribute'
wrd2 = b'класс'
wrd3 =b'функция'
wrd4 =b'type'

# на строки записанные на кириллице вылетает исключение
'''
    wrd2 = b'класс'
          ^
SyntaxError: bytes can only contain ASCII literal characters.
'''