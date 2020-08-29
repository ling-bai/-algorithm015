# 21. 合并两个有序链表
## 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #prehead永远指向第一个节点
        prehead = ListNode(-1)
        '''
            万分注意这里不可以直接使用prev = ListNode(-1),
        否则会丢失第一个节点的索引!!!
        '''

        #维护一个prev指针（暂且称为指针……）
        prev = prehead

        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            
            else:
                prev.next = l2
                l2 = l2.next
            
            prev = prev.next
        
        prev.next = l1 if l1 is not None else l2

        return prehead.next