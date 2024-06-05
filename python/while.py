
result = 0 
while result <= 100:
    menu = int(input("Select menu = "))
    
    if menu == 1:
        result = result + 2 
    elif menu == 2:
        result -=  3
    elif menu == 3:
        result = result * 5
    elif menu == 4:
        result / 2
        
    print(result)
