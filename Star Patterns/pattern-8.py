# WAP to print the pattern given below
#       *
#      ***
#     *****
#    *******
#     *****
#      ***
#       *

n=int(input("Enter the row no. of max stars:\n"))
if n<=0:
    print("I have got nothing to print")
else:
    #upper half till the max row of stars:-
    c=1
    k=n-1
    for i in range(n):
        print(" "*k, end="")
        print("*"*c)
        c+=2
        k-=1

    n-=1    
    c=(n*2)-1
    k=1
    for i in range(n,0,-1):
        print(" "*k, end="")
        print("*"*c)
        c-=2
        k+=1