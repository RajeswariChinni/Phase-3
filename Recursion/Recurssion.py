'''# Printing numbers in ascending order with recurssion(no loops)
def num(i,n):
    if i>n:
        return
    print(i,end=" ")
    num(i+1,n)
n=int(input())
num(1,n)'''
'''
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
printThis(4)'''
''''
#Finding the sum of the elements in list using recurssion
def add(i,n,arr):#or add(i,n,arr,sum) # #-->recurssion
    if i==n: #---> backtracking
        return 0 #print(sum)
    return arr[i]+add(i+1,n,arr) #or sum=sum+nums[i]  add(i+1,n,arr,sum)
arr=[15,21,85,-50]
n=len(arr)
print(add(0,n,arr)) #or add(0,n,arr,0)000

#Finding the max of the elements in list using recurssion
#max element - backtracking
def maxEle(i,n,nums):
    if i<n:
        return max(nums[i],maxEle(i+1,n,nums))
    else:
        return 0  
nums=[12,450,2300,78]
n=len(nums)
print(maxEle(0,n,nums))  

#max element - recursion
def maxEle(i,n,nums,maxi):
    if i<n:
        if nums[i]>maxi:
            maxi=nums[i]
        maxEle(i+1,n,nums,maxi)
    else:
        print(maxi)
    pass
nums=[12,45,23,78]
n=len(nums)
maxi=nums[0]
maxEle(0,n,nums,maxi)

#Finding the minimum of the elements in list using recurssion
#min element-->recurssion
def minEle(i,n,nums,mini):
    if i<n:
        if nums[i]<mini:
            mini=nums[i]
        minEle(i+1,n,nums,mini)
    else:
        print(mini)
    pass
nums=[12,45,23,78]
n=len(nums)
mini=nums[0]
minEle(0,n,nums,mini)

#min element-->backtracking
def minEle(i,n,nums):
    if i<n:
        return min(nums[i],minEle(i+1,n,nums))
    else:
        return nums[0]   
nums=[12,450,2300,78]
n=len(nums)
print(minEle(0,n,nums))
'''
#sir solutions
def findMaxInWay1(index, nums, n, result):
    if index == n:
        print("Max ele is:", result)
        return 
    if nums[index] > result:
        result = nums[index]
    findMaxInWay1(index + 1, nums, n, result)
 
nums = [12, 32, 11, 10]
result = findMaxInWay1(0, nums, len(nums), 0)
 
 
def findMaxInWay2(index, nums, n):
    if index == n - 1:
        return nums[index]
    nextGreater = findMaxInWay2(index + 1, nums, n)
    if nextGreater < nums[index]:
        return nums[index]
    return nextGreater 
 
nums = [12, 32, 11, 10]
result = findMaxInWay2(0, nums, len(nums))
print("Max ele:", result)

#Finding the count of vowels in string
#--->recurssion
def findVowels(i,n,s,count,li):
    if i==n:
        print(count)
        return count
    else:
        if s[i] in li:
            count+=1
        return findVowels(i+1,n,s,count,li)
s="ramsai"
n=len(s)
count=0
li=['A','E','I','O','U','a','e','i','o','u']
findVowels(0,n,s,count,li)
print(findVowels(0,n,s,count,li))