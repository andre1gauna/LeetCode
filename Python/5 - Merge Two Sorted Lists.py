from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2   
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2

        return dummy.next
    

if __name__ == "__main__":
    # Cria a árvore:
    #         1
    #       / | \
    #      3  2  4
    #     / \
    #    5   6

    node1 = ListNode(1)
    node2 = ListNode(2, node1)
    list1 = ListNode(3, node2)

    node4 = ListNode(4)
    list2 = ListNode(5, node4)

    solution = Solution()
    result = solution.mergeTwoLists(list1,list2)
    print(result) 