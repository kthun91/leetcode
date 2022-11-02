from typing import Optional

TESTCASE = [1,2,3,4,5] # [3,4,5]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mylist = []
        while head:
            mylist.append(head)
            head = head.next
        num = len(mylist)//2
        while num:
            mylist.pop(0)
            num -= 1
        return mylist[0]
             
linkedList = []
node = ListNode()
for elem in TESTCASE:
    node = ListNode(elem)
    if len(linkedList) != 0:
        linkedList[-1].next = node
    linkedList.append(node)

res = Solution()
print(res.middleNode(linkedList[0]).val)