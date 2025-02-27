import random

print ("chces si zahrat hru?")
x = input()

if x == "ano":
    a = random.randint(1, 6)                              
    print("pocitac hodil ")
    print (a)
    b = random.randint(1, 6)                              
    print("tvoje mama hodila ")
    print (b)