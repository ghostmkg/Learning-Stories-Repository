# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            # Swapping
            prev.next = second
            first.next = second.next
            second.next = first

            # Move pointers forward
            prev = first
            head = first.next

        return dummy.next


# Helper functions for testing
def create_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def print_linked_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)


# Example usage
head = create_linked_list([1, 2, 3, 4])
obj = Solution()
result = obj.swapPairs(head)
print_linked_list(result)  # Output: [2, 1, 4, 3]
