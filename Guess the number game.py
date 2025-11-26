# import random
# n=random.randint(1,100)
# a=0
# while(a!=n):
#     a=int(input("gussess the number :"))
#     if(a<n):
#         print("please enter high number")
#         gussess=+1
#     elif(a>n):
#         print("please enter lower number")
#         gussess=+1
    
# print(f"you gussess the number{n}right in {gussess} attempt")


import random
n=random.randint(1,100)
a=0
while(a!=n):
    a=int(input("gussess the number :"))
    if(a<n):
        print("please enter high number")
        gussess=+1
    else:
        print("please enter lower number")
        gussess=+1
print(f"you gussess the number{n} right in {gussess}attempt")