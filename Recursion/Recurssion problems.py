# Printing numbers in ascending order with recurssion(no loops)
def num(i,n):
    if i>n:
        return
    print(i,end=" ")
    num(i+1,n)
n=int(input())
num(1,n)

#Guess Outputs

def num(i,n):
    if i>n:
        print("Base Condition got hit")
        return
    print("Starting Line",i)
    for j in range(1,i):
        print("j",j)
    num(i+1,n)
    print("Ending line",i)
n=int(input())
num(1,n)  

def printThis(position):
    print("Leaving here",position)
    if(position==0):
        print("Base condition got hit")
        return
    if position%2==1:
        print("Even positin:",position)
    else:
        print("odd position",position)
    printThis(position-1)
    for index in range(position,-1,-1):
        print("Index is",index)
    print("Entering here",position)
printThis(4)