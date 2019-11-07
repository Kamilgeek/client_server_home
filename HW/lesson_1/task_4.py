'''Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).'''
wrds = ['разработка', 'администривание', 'protocol', 'standart']

for i in wrds:
    a = i.encode('utf-8')
    print(a, type(a))
    b = a.decode('utf-8')
    print(b, type(b))