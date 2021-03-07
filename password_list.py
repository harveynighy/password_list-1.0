import random
characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',1,2,3,4,5,6,7,8,9]
password = []
password_list = []
def password_generator():
    print(random.choice(characters))
    while len(password) < 8:
        password.append(random.choice(characters))

def password_lister():
    pass

password_generator()
print(password)