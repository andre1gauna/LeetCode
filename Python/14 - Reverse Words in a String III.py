from typing import List
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(word[::-1] for word in s.split())
        



if __name__ == "__main__":

    sol = Solution()
    reversedString = sol.reverseWords("Let's take LeetCode contest")
    print(reversedString)


#TODO: revisar 9 e 10, repensar 11 e 12
