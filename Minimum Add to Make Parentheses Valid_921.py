class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened=0
        res=0
        for c in s:
            if c =="(":
                opened+=1
            else:
                opened-=1
                if opened <0:
                    opened=0
                    res +=1
        return res+opened
