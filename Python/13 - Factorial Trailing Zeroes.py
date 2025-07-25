class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n > 0:
            n //= 5
            res += n
        return res

#TODO: revisar 9 e 10, repensar 11 e 12