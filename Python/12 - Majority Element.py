from typing import List, Optional
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorDict = {}

        for elem in nums:
            majorDict[elem] = majorDict.get(elem, 0) + 1

        n = len(nums) // 2
        
        for k, v in majorDict.items():
            if v > n:
                return k
        
        return 0

##TODO: rever 10
    def majorityElement(self, nums: List[int]) -> int:
        maxcount = 0
        candidate = 0
        for num in nums:
            if maxcount == 0:
                candidate = num
        
            if candidate == num:
                maxcount += 1
            else:
                maxcount -= 1
                
        return candidate