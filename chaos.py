import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from string import ascii_lowercase as alc
import random

random.seed()

letters = {}

for idx, i in enumerate(alc):
    letters[i] = round(-1.2 + 0.1*idx, 2)

numbers = []

str = "lufbbfisgjys"

for c in str:
    numbers.append(letters[c])


def iterate_equations(x_old, y_old, a):
    x_new = a[0] + a[1]*x_old + a[2]*(x_old**2) + a[3]*(x_old*y_old) + a[4]*y_old + a[5]*(y_old**2)
    y_new = a[6] + a[7]*x_old + a[8]*(x_old**2) + a[9]*(x_old*y_old) + a[10]*y_old + a[11]*(y_old**2)
    return (x_new, y_new)

xy = []

n = 500

for i in range(n):
    x = random.random()*0.05
    y = random.random()*0.05
    for j in range(n):
        x,y = (iterate_equations(x,y,numbers))
        if abs(x) > 10**6 or abs(y) > 10**6:
            break
            
        if j > 10:
            xy.append((x,y))
            

only_x, only_y = zip(*xy)
plt.scatter(only_x,only_y,s=0.5)
plt.show(block=True)