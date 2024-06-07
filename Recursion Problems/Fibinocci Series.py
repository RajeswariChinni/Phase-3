#Dynamic Programing
#Recursion(Time limit exceeds then)-->(Recursion+cache)Memoization-->Tabulation(no recursion only cache)

#RECURSION:

#fibonocci Series
def fibonacci(a,b,n,m):
    if n==m:
        return
    print(a,end=" ")
    t=a
    a=b
    b=a+t
    n+=1
    fibonacci(a,b,n,m)
limit=int(input())
fibonacci(0,1,0,limit)
print()

#Finding the Nth term
def findNthterm(n):
    if n==1 or n==2:
        return 1
    res1=findNthterm(n-1)
    res2=findNthterm(n-2)
    return res1+res2
# n=int(input())
print("Nth Term is:",findNthterm(limit-1))

 
# Using Memoization 
def findNthTermUsingCache(n, cache):
    if n == 1 or n == 2:
        return 1 
    elif cache[n] != -1:
        return cache[n]
 
 
    result1 = findNthTermUsingCache(n - 1, cache)
    result2 = findNthTermUsingCache(n - 2, cache)
    cache[n] = result1 + result2
    return result1 + result2 
 
# Tabulation approach (Ultimate Dynamic programming solution)
def findNthTermUsingTabulation(n):
    cache = [-1] * (n + 1)
    # Whatever base condition we wrote 
    # recursive solutin, we need to 
    # initialize them 
 
    cache[1] = 1 
    cache[2] = 1 
    # 1 - wherever 'n' is present, replace it with index 
    # 2 - wherever 'functionCall' is there replace it with cache 
 
    for index in range(3, n + 1):
        result1 = cache[index - 1]
        result2 = cache[index - 2]
        cache[index] = result1 + result2
 
    return cache[n]
 

n = 8
 
cache = [-1] * (n + 1)
print(findNthTermUsingCache(n-1, cache))
 
print(findNthTermUsingTabulation(n-1))