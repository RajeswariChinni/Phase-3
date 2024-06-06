#Finding the sum of the elements in list using recurssion
def add(i,n,arr):#or add(i,n,arr,sum) # #-->recurssion
    if i==n: #---> backtracking
        return 0 #print(sum)
    return arr[i]+add(i+1,n,arr) #or sum=sum+nums[i]  add(i+1,n,arr,sum)
arr=[15,21,85,-50]
n=len(arr)
print(add(0,n,arr)) #or add(0,n,arr,0)

#Sir Solutions
# Passing data from Parent function to child function
def printSum(index, n, nums, result):
    if index == n:
        print("Sum is:", result)
        return 
 
    result += nums[index]
    #result = result + nums[index]
    printSum(index + 1, n, nums, result)
 
# Passing data from child function to Parent function
def printSum2(index, n, nums):
    if index == n:
        return 0 
    nextElementsSum = printSum2(index + 1, n, nums)
    return nextElementsSum + nums[index]
 
nums = [12, 34, 12, 5, 7]
n = len(nums)
result = printSum2(0, n, nums)
print("Sum is:", result)