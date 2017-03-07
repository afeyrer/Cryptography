"""
cryptography.py
Author: Abby Feyrer
Credit: None

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
z=0
a=list[associations]
while z==0:
    opt=input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if opt=="e":
        y=0
        mes=list(input("Message: "))
        key=list(input("Key: "))
        while y<len(mes):
            k=a.find(mes[y])+a.find(key[y])
            mes[y]=a[k]
        for x in mes: 
            print(x, end="")
    if opt=="d":
        y=0
        mes=input("Message: ")
        key=input("Key: ")
    if opt=="q":
        print("Goodbye!")
        z=1
        
    if opt!="q" and opt!="e" and opt!="d":
        print("Did not understand command, try again.")