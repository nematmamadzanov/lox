N = 5
arr = [30]
D = 4
for i in range(1, N):
    r = arr[0] + i * D
    arr.append(r)
print(arr)