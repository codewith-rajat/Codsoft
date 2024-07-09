import random
a=int(input("Enter password length:"))
b="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@1234567890."
c=random.sample(b,a)
d="".join(c)
print(d)
