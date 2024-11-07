class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # return len(s) == len(goal) and s in goal + goal 
        for i in range(0,len(s)):
            if s[i]== goal[0]:
                if s[i:]+s[:i] == goal:
                    return True
        return False

        
