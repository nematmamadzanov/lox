nemb = 6
nema= 3

 
if nemb != nema:
    
    if nemb < nema:
        nema = nema = max(nemb, nema)
    else:
        nemb = nema
else:
    nemb = 0
    nema = 0
 
print(nemb, nema)


x = 5 
result = 0
if x < -2 or x > 2:
 result = 2 * x
else:
 result = -3 * x 

print(result)
