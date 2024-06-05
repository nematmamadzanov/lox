A = int(input())
B = int(input())

while A > 0:
    A = A - B 
    print(A + B)


2.
A = int(input())
B = int(input())

while True:
    if A > B:
        break
    else:
        A = B - B
        print(A)




N = int(input())
K = 1 
result = 0 
while result < N:
     result = result + 2 ** K 
if result >= N:
 K = K + 1
print(K)



