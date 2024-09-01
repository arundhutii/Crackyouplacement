class Solution(object):
    def restoreString(self, s, indices):
        result=""
        for i in range(len(indices)):
            result += s[indices.index(i)]
        return result
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
