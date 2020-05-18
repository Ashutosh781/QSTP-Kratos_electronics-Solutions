#! /usr/bin/env python

s = 'Y'
while s != 'n':
    try:
        x = input("Enter the first number : ")
        s = input("Enter the operation : ")
        y = input("Enter the second number : ")
        ans = eval(x+s+y)
        print(f'{x}{s}{y} = {ans}')
    except:
        print("Division by zero is not allowed")
        
    while True:
        s = input("Do you want to use the calculator again (Y/n) : ")
        if (s == 'Y') or (s == 'n'):
            break 

print("\nEnd")        
