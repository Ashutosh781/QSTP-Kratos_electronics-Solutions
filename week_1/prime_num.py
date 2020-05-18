#! /usr/bin/env python

#Asking for input until a list of 10 integers given
while True:
    num = input("Enter a list of 10 integers separated by a ',' : ").split(',')
    l = len(num)
    try:
        for i in range(l):
            num[i] = int(num[i])
        p = (l==10)
        if p:
            break
    except:
        continue



#Finding prime numbers

prime_num = []

for x in num:
    if x > 1:
        for i in range(2,((x//2)+1)):
            if x % i == 0:
                break
        else:
            prime_num.append(x)
    
    elif x == 1: #Number 1 is not considered as prime
        continue
    else: #For any negative numbers or 0
        continue

if len(prime_num) > 0:
    print(f'Prime numbers from the given list are : {prime_num}')
else:
    print("There were no prime numbers in the given list")

print("\nEnd")