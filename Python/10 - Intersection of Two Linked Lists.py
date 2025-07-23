from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return null
        
        a, b = headA, headB
        
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
def print_list(head):
    nodes = []
    while head:
        nodes.append(str(head.val))
        head = head.next
    print(" -> ".join(nodes))
    
if __name__ == "__main__":
    # Criando a parte comum (intersecção real): 4 -> 5 -> 6
    common = ListNode(4, ListNode(5, ListNode(6)))

    # Lista A: 4 -> 5 -> 6
    headA = common

    # Lista B: 1 -> 2 -> 3 -> 4 -> 5 -> 6
    headB = ListNode(1, ListNode(2, ListNode(3, common)))

    # Exibe as listas (para debug)
    print("List A:")
    print_list(headA)
    print("List B:")
    print_list(headB)

    # Testa interseção
    sol = Solution()
    intersection = sol.getIntersectionNode(headA, headB)
    print("\nIntersection at node:", intersection.val if intersection else "None")