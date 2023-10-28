import msvcrt
import time
import random
import colorama
from colorama import Fore

def resta(n):
    for i in range(40):
        x=random.randint(0,25)
        y=random.randint(0,25)
        print(Fore.BLUE+f"{n+1}:    {x} - {y} = {x-y}")
        time.sleep(0.5)
        n+=1
        if i==19:
            print("----------------------")
            n=suma(n)
            print("----------------------")
            
def suma(n):
    for j in range(30):
        x=random.randint(0,25)
        y=random.randint(0,25)
        print(Fore.GREEN+f"{n+1}:    {x} + {y} = {x+y}")
        time.sleep(0.5)
        n+=1
        if j==14:
            print("----------------------")
            n=division(n)
            print("----------------------")
    return n

def division(n):
    for k in range(25):
        x=random.randint(0,25)
        y=random.randint(1,25)
        print(Fore.YELLOW+f"{n+1}:    {x} / {y} = {round(x/y,2)}")
        time.sleep(0.5)
        n+=1
        if k==9:
            print("----------------------")
            n=multi(n)
            print("----------------------")
    return n

def multi(n):
    for l in range(15):
        x=random.randint(0,25)
        y=random.randint(0,25)
        print(Fore.RED+f"{n+1}:    {x} * {y} = {x*y}")
        time.sleep(0.5)
        n+=1
    return n

if __name__=="__main__":
    n=0
    print("----------------------")
    resta(n)