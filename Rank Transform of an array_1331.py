class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {num: i for i, num in enumerate(sorted(set(arr)), start=1)}
        
        return [rank[num] for num in arr]



