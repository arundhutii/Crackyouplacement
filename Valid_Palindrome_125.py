class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        start, last = 0, len(s) - 1
        while start <= last:
            curr_first = s[start]
            curr_last = s[last]
            if not curr_first.isalnum():
                start += 1
            elif not curr_last.isalnum():
                last -= 1
            else:
                if curr_first.lower() != curr_last.lower():
                    return False
                start += 1
                last -= 1
        return True
