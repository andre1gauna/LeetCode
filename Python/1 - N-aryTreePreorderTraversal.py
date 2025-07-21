from typing import List, Optional

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack = [root]
        output = []
        while stack:
            temp = stack.pop()
            output.append(temp.val)
            stack.extend(temp.children[::-1])
        return output
    

#Forma recursiva:
    def preorder (self, root:'Node') -> List['int']:
        result = []
        self.traversePreorder(root, result)
        return result
    
    def traversePreorder(self, root: 'Node', result: List[int]):
        result.append(root.val)
        for child in root.children:
            self.traversePreorder(child, result)
        return result


if __name__ == "__main__":
    # Cria a árvore:
    #         1
    #       / | \
    #      3  2  4
    #     / \
    #    5   6

    node5 = Node(5)
    node6 = Node(6)
    node3 = Node(3, [node5, node6])
    node2 = Node(2)
    node4 = Node(4)
    root = Node(1, [node3, node2, node4])

    solution = Solution()
    result = solution.preorder(root)
    print(result)  # Esperado: [1, 3, 5, 6, 2, 4]