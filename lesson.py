def open_1(f):
    with open (f, 'r') as file:
        print(file.read())

def open_2(f,content):
    with open (f, 'a') as file:
        print(file.write(content))


def open_3(f):
    with open (f, 'w') as file:
        pass

open_1(r'C:\Users\User\Desktop\Projects\text1.txt')
open_2(r'C:\Users\User\Desktop\Projects\text1.txt','content')
open_3(r'C:\Users\User\Desktop\Projects\text1.txt')


2
def max(list):
    max = list[0]
    for i in  list:
        if i<max:
            max =  i
    return max 


print(max([2,22,54,121]))




user = {
    "Ali": "manager",
    "oroz": "admin"
}

def role(username):
    if username in user:
        return user[username]
    else:
        return "User not found"

print(user["oroz"])

def add_users(ali, admin):
    user[ali] = admin

add_users("ali", "admin")
print(user)

def add_users(oroz, manager):
    user[oroz] = manager

add_users("oroz", "manager")
print(user)

def del_ali(ali):
    del user[ali]  
    print(user)

del_ali("Ali") 


{'Ali': 'admin', 'oroz': 'admin'}
{'Ali': 'admin', 'oroz': 'manager'}
{'oroz': 'manager'}



