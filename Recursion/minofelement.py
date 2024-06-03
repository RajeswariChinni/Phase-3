
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

#sir solutions
def findMaxInWay1(index, nums, n, result):
    if index == n:
        print("Max ele is:", result)
        return 
    if nums[index] < result:
        result = nums[index]
    findMaxInWay1(index + 1, nums, n, result)
nums = [12, 32, 11, 10]
result = findMaxInWay1(0, nums, len(nums), nums[0])
 
 
def findMaxInWay2(index, nums, n):
    if index == n - 1:
        return nums[index]
    nextGreater = findMaxInWay2(index + 1, nums, n)
    if nextGreater > nums[index]:
        return nums[index]
    return nextGreater 
 
nums = [12, 32, 11, 10]
result = findMaxInWay2(0, nums, len(nums))
print("Max ele:", result)