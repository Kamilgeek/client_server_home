'''Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать
 результаты из байтовового в строковый тип на кириллице.
'''
import subprocess


ping_wrds = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for ping_now in ping_wrds:

    ping_process = subprocess.Popen(ping_now, stdout=subprocess.PIPE)

    i = 0

    for line in ping_process.stdout:

        if i < 10:
            print(line)
            print(line.decode('utf-8'))
            i += 1
        else:
            print('#' * 30)
            break

# что-то не получилось