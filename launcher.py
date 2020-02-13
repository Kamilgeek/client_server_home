import subprocess

process = []

while True:
    action = input('Выберите действик: q - выход , s - выпустить сервер и клиенты , x - закрыть все окна :')

    if action == 'q':
        break
    elif action == 's':
        process.append(subprocess.Popen('python server', shell=True))
        process.append(subprocess.Popen('python client -n test1', shell=True))
        process.append(subprocess.Popen('python client -n test2', shell=True))
        process.append(subprocess.Popen('python client -n test3', shell=True))
    elif action == 'x':
        while process:
            victim = process.pop()
            victim.kill()



