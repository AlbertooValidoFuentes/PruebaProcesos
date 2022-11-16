import platform
import os
from multiprocessing import Process
from time import *
import datetime

def padreWindows():
    n = 1

    while n <= 10:
        p = Process(target=hijoWindows)
        p.start()

        print(f'Iniciando el proceso: {os.getpid()} a las {datetime.datetime.now().strftime("%H:%M:%S")}')
        
        p.join(0)

        sleep(10)
        n += 1

def hijoWindows():
    print(f'Inicando el proceso: {os.getpid()}')
    
    sleep(3)
    
    print(f'Terminado el proceso con PID: {os.getpid()}')
    os._exit(0)

def padreLinux():
    n = 1

    while n < 10:
        
        nuevoPid = os.fork()


        if nuevoPid == 0:
            print(f'Iniciando el proceso: {os.getpid()} a las {datetime.datetime.now().strftime("%H:%M:%S")}')

            hijoLinux()

        sleep(10)
        
        
        n += 1

def hijoLinux():
    print(f'Inicando el proceso: {os.getpid()}')
    
    sleep(3)

    print(f'Terminado el proceso con PID: {os.getpid()}')
    os._exit(0)


def main():
    sistema = platform.system()

    if sistema == 'Windows':
        padreWindows()
    elif sistema == 'Linux':
        padreLinux()

if __name__ == '__main__':
    main()