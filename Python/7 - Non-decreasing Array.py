from typing import List

class Solution:
   def checkPossibility(self, nums: List[int]) -> bool:
        err = 0
        for i in range (1, len(nums)):
            if nums[i] < nums [i-1]:
                if err or (i > 1 and i < len(nums) - 1 and nums[i-2] > nums[i] and nums[i+1] < nums[i-1]):
                    return False
                err = 1
        return True
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.checkPossibility(nums =
[5,7,1,8]))


#TODO: revisar 3 e 4, repensar 5 e 6
