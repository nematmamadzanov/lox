def is_prime(n):
     for i in range(2, n):
         if n % i == 0:
             return False
     return True

if is_prime(3):
     print("Простое число")
else:
     print("Составное число")

#29def 
def DigitCount(K, S):
 (K,S)
 i = 0
 for i in 1, 5:
     print('K :')
 else:
    print(K)
 print(DigitCount(K))


# 23 def

def  Quarter(X,Y):
    import random
def Quarter(x,y):
    if((x>0)and(y>0)):
        res="первый четверть"
        
    elif((x<0)and(y>0)):
        res = "второй четверть"
        
    elif((x<0)and(y<=0)):
        res = "третий четверть"
    
    else:
        res = "четвертый четверть"
        
    return res
 
if __name__ == '__main__':
    x=float(input())
    y= float(input())
  
    
    print(Quarter(x,y))