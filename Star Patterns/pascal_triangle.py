def factorial(num):
    fact=1
    if num==0:
        return 1
    for i in range(1, num+1):
        fact*=i
    return fact

def computations(row, cols):
    rf=factorial(row)
    cf=factorial(cols)
    rc_cf=factorial(row-cols)
    com=rf//(rc_cf*cf)
    return com

r=int(input("Enter the number of rows:\n"))
if r<0:
    print("Invalid no. of rows.")
else:
    l=[]
    for i in range(r):
        col_start=0
        temp_list=[]
        for j in range(i+1):
            value=computations(i, col_start)
            temp_list.append(value)
            col_start+=1
        l.append(temp_list)
    # Displaying the pattern
    c=r
    for i in range(r):
        print(" "*c, end="")
        for j in range(len(l[i])):
            print(l[i][j], end=" ")
        print()
        c-=1