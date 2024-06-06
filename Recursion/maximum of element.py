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