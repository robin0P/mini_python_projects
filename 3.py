import math

list = [2, -1, -9, -2, 13, 6]

min = math.inf 
max = -math.inf
for i in range(len(list)):
    if(list[i] < min):
        min = list[i]

    if(list[i] > max):
        max = list[i]

print(F"max = {max}\n min = {min}")