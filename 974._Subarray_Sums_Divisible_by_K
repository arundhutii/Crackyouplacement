class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res=0 
        prefixSums=0
        prefix_cnt=defaultdict(int)
        prefix_cnt[0]=1

        for n in nums:
            prefixSums +=n
            diff=prefixSums % k

            if diff in prefix_cnt:
                res += prefix_cnt[diff]
            prefix_cnt[diff] += 1
        return res
