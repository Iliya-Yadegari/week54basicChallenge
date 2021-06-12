import random
lst=[]
for i in range(7):
    r = random.randint(0,35)
    if r not in lst: 
        lst.append(r)

print(lst)