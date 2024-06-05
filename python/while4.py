# 1 for

A = int(input())
B = int(input())
 
result = A * B
 
print("{A} * {B} {result}")

# 2 for

A = int(input())
B = int(input())
 
number = B - A + 1
 
print(" {A}  {B}")
for num in range(A, B + 1):
    print(num, end=" ")
print(f" {number}")

# 3 for

P = int(input())
N = int(input())
 

amb = P - N - 1
 
print(f" {P}  {N} ")
for num in range(P - 1, N, -1):
    print(" {P}  {N} ")
print(f"{amb}")

# 4 for

kg = float(input())
 
print("cost")
for kg in range(1, 11):
    cost = kg * kg
    print(f"{kg} kg: {cost}")

# 5 for

ckoko_kg = float(input())
 
print("Cost")
for kg in range(1, 11):
    cost = kg * 0.1 * ckoko_kg 
    print(f"{0.1 * kg:1f} kg: {cost:2f}")



