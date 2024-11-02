class Solution:
    def makeFancyString(self, s: str) -> str:
        count=1
        res=[]

        for i in range(len(s)):
            if i>0 and s[i]==s[i-1]:
                count+=1
            else:
                count=1

            if count<3:
                res.append(s[i])

        return ''.join(res) 



