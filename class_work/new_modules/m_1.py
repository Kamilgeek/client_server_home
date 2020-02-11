from subprocess import Popen, PIPE, call
import chardet

ret = call('ls', shell=True)
print(ret)

PROC = Popen('ls', shell=True, stdout=PIPE)

DATA = PROC.stdout.read()
RESULT = chardet.detect(DATA)
OUT = DATA.decode(RESULT['encoding'])

print(OUT)

RETURNCODE = call('ls')
if RETURNCODE == 0:
    print('ALL GOOD!')
else:
    print('ERROR!')


