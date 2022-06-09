import random

import random
AR = [10,20,30,40,50,60,70];
START = random.randint(1,3)
END = random.randint(2,4)
for k in range(START,END+1):
    print(AR[k],end="#")
    
print(START)
print(END)