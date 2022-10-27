from typing import Optional

TESTCASE = [1,2,3,2,1] # True

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mylist = []
        reverseList = []
        while head:
            mylist.append(head.val)
            reverseList.append(head.val)
            head = head.next
        reverseList.reverse()
        return mylist == reverseList
             
linkedList = []
node = ListNode()
for elem in TESTCASE:
    node = ListNode(elem)
    if len(linkedList) != 0:
        linkedList[-1].next = node
    linkedList.append(node)

res = Solution()
print(res.isPalindrome(linkedList[0]))

## leetcode solution 
# class Solution:
#     def isPalindrome(self, head) -> bool:
#         mylist = []
#         reverseList = []
#         while head:
#             mylist.append(head.val)
#             reverseList.append(head.val)
#             head = head.next
#         reverseList.reverse()
#         return mylist == reverseList