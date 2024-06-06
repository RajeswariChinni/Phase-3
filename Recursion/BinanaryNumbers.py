def printingBinatyNumbers(size,result,n):
    if size==n:
        print(result)
        return 
    printingBinatyNumbers(size+1,result+'1',n)
    printingBinatyNumbers(size+1,result+'0',n)
n=2
printingBinatyNumbers(0,'',n)
'''
#Practice Problems
1.Write a python program to accept a list of integer and print the sum of all 5 divisible numbers using Recursion
2.write a python program to print all even indexed elements in both left to right 
'''