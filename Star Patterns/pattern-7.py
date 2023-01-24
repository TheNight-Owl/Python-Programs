# WAP to print the pattern given below
#       *******
#        *****
#         ***
#          *

n=int(input("Enter the no. of rows:\n"))
if n<=0:
    print("I have got nothing to print")
else:
    c=(n*2)-1
    k=0
    for i in range(n,0,-1):
        print(" "*k, end="")
        print("*"*c)
        c-=2
        k+=1