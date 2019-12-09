import time
import threading

THREADS_NUM = 5

lock = threading.Lock()

def sample(name, num):
    for itm in range(1, num+1):
        time.sleep(1)
        lock.acquire()
        print(f'{name} was called {itm} times')
        lock.release()

# thread = threading.Thread(target=sample, args=('thread', 10))
# thread.start()
# sample('call-1', 5)

for itm in range(1, THREADS_NUM+1):
    num = 3 + itm
    name = f'thread {itm}'
    thread = threading.Thread(target=sample, args=(name, num))
    thread.start()