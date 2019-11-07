wrds = ['разработка', 'сокет', 'декоратор']

for i in wrds:
    print(type(i), i)

enc_wrds = []
for t in wrds:
    enc = t.encode('utf-8')
    enc_wrds.append(enc)
print(enc_wrds)

for i in enc_wrds:
    print(type(i), i)

