#Finding the count of vowels in string
#--->recurssion
def findVowels(i,n,s,count,li):
    if i==n:
        print(count)
        return 
    else:
        if s[i] in li:
            count+=1
        findVowels(i+1,n,s,count,li)
s="ramsai"
n=len(s)
count=0
li=['A','E','I','O','U','a','e','i','o','u']
findVowels(0,n,s,count,li)
#-->backtracking
def findVowels(i,n,s,count,li):
    if i==n:
        return count
    else:
        if s[i] in li:
            count+=1
        return findVowels(i+1,n,s,count,li)
s="ramsai"
n=len(s)
count=0
li=['A','E','I','O','U','a','e','i','o','u']
print(findVowels(0,n,s,count,li))

#Sir Solutions
def countVowelsWay1(word, index, n, result):
    if index == n:
        print("Vowels count is:", result)
        return 
    vowels = "aeiouAEIOU"
    if word[index] in vowels:
        result += 1 
    countVowelsWay1(word, index + 1, n, result)
 
 
word = "abcdeefuigh"
countVowelsWay1(word, 0, len(word), 0)
 
 
 
 
def countVowelsWay2(word, index, n):
    if index == n:
        return 0 
    nextVowelsCount = countVowelsWay2(word, index + 1, n)
    vowels = "aeiouAEIOU"
    if word[index] in vowels:
        nextVowelsCount += 1 
    return nextVowelsCount
word = "abcdeefuigh"
result = countVowelsWay2(word, 0, len(word))
print("Vowels count is:", result)