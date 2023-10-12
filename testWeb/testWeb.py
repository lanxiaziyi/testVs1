import sys
from math import cos,radians
def make_dot_string(x):
    return ' ' * int(20 * cos(radians(x)) + 20) + 'o'


for i in range(0,1800,12):
    s = make_dot_string(i)
    print(s)

print("Hello, Visual Studio")