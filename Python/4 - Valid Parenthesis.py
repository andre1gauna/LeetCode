class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
        return not stack        
    
    def isValid2(self, s: str) -> bool:
        st = []
        for i in range(len(s)):
            if st:
                last = st[-1]
                if (self.validPair(last, s[i])):
                    st.pop()
                    continue
            st.append(s[i])
        return not st

    def validPair(self, last, current):
        if last == '(' and current == ')' or last == '{' and current == '}' or last == '[' and current == ']':
            return True
        else:
            return False       
        

if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid('([])'))
            