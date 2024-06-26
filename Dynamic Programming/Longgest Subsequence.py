def lcs(text1, text2):
        '''n=len(text1)
        m=len(text2)
 
        def recursiveApproach(index1, index2):
            if index1 == n or index2 == m:
                return 0 
            elif text1[index1] == text2[index2]:
                return 1 + recursiveApproach(index1 + 1, index2 + 1)
 
            choice1 = recursiveApproach(index1 + 1, index2)
            choice2 = recursiveApproach(index1, index2 + 1)
            return max(choice1, choice2)
 
        cache = [[-1] * m for i in range(n)]
 
        def memoizationApproach(index1, index2):
            if index1 == n or index2 == m:
                return 0 
            elif cache[index1][index2] != -1:
                return cache[index1][index2]
            elif text1[index1] == text2[index2]:
                cache[index1][index2] = 1 + memoizationApproach(index1 + 1, index2 + 1)
                return cache[index1][index2]
 
            choice1 = memoizationApproach(index1 + 1, index2)
            choice2 = memoizationApproach(index1, index2 + 1)
            cache[index1][index2] = max(choice1, choice2)
            return cache[index1][index2]
 
 
        def tabulationApproach():
            cache = [[0] * (m + 1) for i in range(n + 1)]
            for index1 in range(n - 1, -1, -1):
                for index2 in range(m - 1, -1, -1):
                    if text1[index1] == text2[index2]:
                        cache[index1][index2] = 1 + cache[index1 + 1][index2 + 1]
                    else:
                        choice1 = cache[index1 + 1][index2]
                        choice2 = cache[index1][index2 + 1]
                        cache[index1][index2] = max(choice1, choice2)
 
            return cache[0][0]
 
        return tabulationApproach()
            '''
        common = set(text1).intersection(set(text2))
        if len(common) == 0:
            return 0
        
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        
        text1 = [word for word in text1 if word in common]
        text2 = [word for word in text2 if word in common]
        print(text1,text2)
        dp = [0 for i in range(len(text1))]

        for word in text2:
            tmp = 0
            for i in range(len(text1)):
                if tmp < dp[i]:
                    tmp = dp[i]
                elif word == text1[i]:
                    dp[i] = tmp + 1
        print(dp)
        return max(dp)
text1 = "sxcpqrsvwf"
text2 = "shmtulqrypy" 
print(lcs(text1,text2))