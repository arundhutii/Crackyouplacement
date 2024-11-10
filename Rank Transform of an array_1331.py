class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranked = {num: rank for rank, num in enumerate(sorted(set(arr)), start=1)}
        
        return [ranked[num] for num in arr]



