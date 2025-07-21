from typing import List

class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []
        

    def push(self, val: int) -> None:
        if (val <= self.min):
            self.stack.append(self.min)
            self.min = val
        self.stack.append(val)


    def pop(self) -> None:
        if (self.stack.pop() == self.min):
            self.min = self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min

# Segunda implementação:

    # def __init__(self):
    #     self.min = []
    #     self.stack = []
        

    # def push(self, val: int) -> None:
    #     if (val <= self.min[-1] or not self.min):
    #         self.min.append(val)
    #     self.stack.append(val)


    # def pop(self) -> None:
    #     if (self.stack.pop() == self.min[-1]):
    #         self.min.pop()
        

    # def top(self) -> int:
    #     return self.stack[-1]
        

    # def getMin(self) -> int:
    #     return self.min[-1]

if __name__ == "__main__":
    sol = MinStack()
    lista = [0,1,0]
    for i in lista:
        sol.push(i)
    print(sol.getMin())
    sol.pop()
    print(sol.getMin())