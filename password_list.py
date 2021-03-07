import random
characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',1,2,3,4,5,6,7,8,9]

def password_generator():
    password = []
    while len(password) < 4:
        password.append(random.choice(characters))
    return password

def password_lister():
    password_list = []
    while len(password_list) < 5:
        password_list.append(password_generator())
    password_list = str(password_list)
    print(len(password_list))
    return password_list

print(password_generator())
print(password_lister())