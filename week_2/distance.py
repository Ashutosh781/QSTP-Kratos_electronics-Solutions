#! /usr/bin/env python

import numpy

##DEFINING FUNCTIONS##
def dist(x1,y1,z1,x2,y2,z2):
    d_a = (((x2-x1)**2) + ((y2-y1)**2) + ((z2-z1)**2))**0.5
    return d_a

def short_distance(a):
    n = a.shape[0]
    
    for i in range(n-1):
        x1 = a[i][0]
        y1 = a[i][1]
        z1 = a[i][2]
        
        for j in range(i+1,n):
            x2 = a[j][0]
            y2 = a[j][1]
            z2 = a[j][2]
            d_b = dist(x1,y1,z1,x2,y2,z2)
            if j == 1:
                short_a = d_b
                h_a = [a[0],a[1]]
            elif d_b < short_a:
                short_a = d_b
                h_a = []
                h_a = [a[i],a[j]]
            elif (d_b == short_a) and (j!=1):
                short_a = d_b
                h_a.append(a[i])
                h_a.append(a[j])
            else:
                pass
        
    return h_a,short_a

##DRIVER CODE##
if __name__ == "__main__":
    s = 'Y'
    while s != 'n':
        R = 0
        while R == 0:
            R = int(input("Enter the number of points : "))

        entries = []
        while len(entries) != (R*3):
            print("Enter the coordinates in x y z format separated by space : ")
            entries = list(map(float,input().split( )))
        
        a = numpy.array(entries).reshape(R,3)
        x,d = short_distance(a)
        y = len(x)

        print(f'Shortest distance is {d}')
        print("The coordinates with the shortest distance are : ")

        for i in range(0,y,2):
            print(f'{x[i]}' ,end=' ')
            print(f'{x[i+1]}')

        print('\n')
        while True:
            s = input('Again ?? (Y/n) : ')
            if (s=='Y') or (s=='n'):
                break

    print("\nEnd")