import random
import math

def boom():
    for i in range (10):
        print(random.randint(25,35))
       

def golf(the_list):
    return random.choice(the_list)

def odd():
    return random.randrange(1, 100, 2)


def add_up(a,b):
    a = math.pow(a,2)
    b = math.pow(b,2)
    result = math.sqrt(a + b)
    return result

