import math
import copy
 
# Всхідні данні A*X = B
# x = [1.10202, 0.99091, 1.01111]
 
a = [[10, 1, -1],
     [1, 10, -1],
     [-1, 1, 10]]
     
b = [11, 10, 10]
 
# Перевірка матриці коеф
def isCorrectArray(a):
    for row in range(0, len(a)):
        if( len(a[row]) != len(b) ):
	    print('incorrect length!')
            return False
    
    for row in range(0, len(a)):
        if( a[row][row] == 0 ):
            print('Zero elems on g diagonal!')
            return False
    return True
 
 
# Умова виходу
def isNeedToComplete(x_old, x_new):
    eps = 0.0001
    sum_up = 0
    sum_low = 0
    for k in range(0, len(x_old)):
        sum_up += ( x_new[k] - x_old[k] ) ** 2
        sum_low += ( x_new[k] ) ** 2
        
    return math.sqrt( sum_up / sum_low ) < eps
 
# Рішення
def solution(a, b):
    if( not isCorrectArray(a) ):
        print('input error')
    else:
        count = len(b) # кількість коренів 
        
        x = [1 for k in range(0, count) ] # початкове наближення
        
        numberOfIter = 0  # рахуєм кільк ітерацій
        MAX_ITER = 100    # максимум ітерацій
        while( numberOfIter < MAX_ITER ):
 
            x_prev = copy.deepcopy(x)
            
            for k in range(0, count):
                S = 0
                for j in range(0, count):
                    if( j != k ): S = S + a[k][j] * x[j] 
                x[k] = b[k]/a[k][k] - S / a[k][k]
            
            if isNeedToComplete(x_prev, x) : # перевірка на вихід 
                break
              
            numberOfIter += 1
 
        print('Number of iter: ', numberOfIter)
        
        return x    
                
    
print( 'Solution: ', solution(a, b) ) 