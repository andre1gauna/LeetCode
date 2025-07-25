from typing import List, Optional

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        current_lenght = 1
        max_lenght = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                current_lenght += 1
                max_lenght = max(max_lenght, current_lenght)
            else: 
                current_lenght = 1
        return max_lenght

            



if __name__ == "__main__":
    sol = Solution()
    print(sol.findLengthOfLCIS([1,3,5,4,2,3,4,5]))


#TODO: revisar 7 e 8, repensar 9 e 10
