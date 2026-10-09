#!/usr/bin/python3

n=int(input("Введите натуральное число"))
factors=[]
d=2
while n>1:
    while n%d==0:
        factors.append(d)
        n= n//d
    d=d+1
print(factors)

