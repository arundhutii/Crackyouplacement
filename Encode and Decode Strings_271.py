class Solution:

    def encode(self, strs: List[str]) -> str:
        res_enc=''
        for i in strs:    
            res_enc += i+'dhuti'
        return res_enc

    def decode(self, s: str) -> List[str]:
        res_dec= s.split('dhuti')
        res_dec = res_dec[:-1]
        return res_dec 

