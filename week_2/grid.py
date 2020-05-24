#! /usr/bin/env python
import numpy as np

##DEFINING FUNCTION##
def free_zeros_in_grid(x):
    n = x.shape[0]
    m = x.shape[1]
    counter = 0

    for i in range(n):
        for j in range(m):
            if (i==0) and (j==0):
                if (x[0][0]==0) and (x[0][1]==0) and (x[1][0]==0) and (x[1][1]==0):
                    counter +=1
            
            elif (i==0) and (j==m-1):
                if (x[0][m-1]==0) and (x[0][m-2]==0) and (x[1][m-1]==0) and (x[1][m-2]==0):
                    counter +=1

            elif (i==n-1) and (j==0):
                if (x[n-1][0]==0) and (x[n-1][1]==0) and (x[n-2][0]==0) and (x[n-2][1]==0):
                    counter += 1

            elif (i==n-1) and (j==m-1):
                if (x[n-1][m-1]==0) and (x[n-1][m-2]==0) and (x[n-2][m-1]==0) and (x[n-2][m-2]==0):
                    counter += 1

            elif i==0:
                if (x[0][j]==0) and (x[0][j-1]==0) and (x[0][j+1]==0) and (x[1][j]==0) and (x[1][j-1]==0) and (x[1][j+1]==0):
                    counter += 1

            elif i==n-1:
                if (x[n-1][j]==0) and (x[n-1][j-1]==0) and (x[n-1][j+1]==0) and (x[n-2][j]==0) and (x[n-2][j-1]==0) and (x[n-2][j+1]==0):
                    counter += 1

            elif j ==0:
                if (x[i][0]==0) and (x[i-1][0]==0) and (x[i+1][0]==0) and (x[i][1]==0) and (x[i-1][1]==0) and (x[i+1][1]==0):
                    counter += 1

            elif j==m-1:
                if (x[i][m-1]==0) and (x[i-1][m-1]==0) and (x[i+1][m-1]==0) and (x[i][m-2]==0) and (x[i-1][m-2]==0) and (x[i+1][m-2]==0):
                    counter += 1

            else:
                if (x[i][j]==0) and (x[i][j-1]==0) and (x[i][j+1]==0) and (x[i-1][j]==0) and (x[i-1][j-1]==0) and (x[i-1][j+1]==0) and (x[i+1][j]==0) and (x[i+1][j-1]==0) and (x[i+1][j+1]==0):
                    counter += 1

    
    return counter

##DRIVER CODE##
if __name__ == "__main__":
    s = 'Y'
    while s !='n':
        R = int(input('Enter the number of infected homes : '))
        coordinates = []
        while len(coordinates) != (R*2):
            print("Enter the coordinates in x y format separated by space (x,y<10) : ")
            coordinates = list(map(int,input().split( )))
        
        x = np.array(coordinates).reshape(R,2)
        y = np.zeros([10,10])
        
        for i in range(R):
            y[x[i][0]][x[i][1]] = 1
        
        print('\n')
        print(y)
        safe_homes = free_zeros_in_grid(y)
        print(f'\nNumber of safe houses are {safe_homes}')
        print('\n')
        
        while True:
            s = input('Again ?? (Y/n) : ')
            if (s=='Y') or (s=='n'):
                break
    
    print('\nEnd')