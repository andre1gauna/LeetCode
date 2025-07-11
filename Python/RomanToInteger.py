class Solution:
    def romanToInt(self, s: str) -> int:
        romanToIntDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}
        i = 0
        output = 0
        for i in range(len(s)):
            if i + 1 < len(s) and romanToIntDict[s[i]] < romanToIntDict[s[i+1]]: 
                output -= romanToIntDict[s[i]]
            else:
                output += romanToIntDict[s[i]]
        return output
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt('MMDC'))