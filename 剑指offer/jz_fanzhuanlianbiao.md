**题目**

给定一个单链表的头结点pHead(该头节点是有值的，比如在下图，它的val是1)，长度为n，反转该链表后，返回新链表的表头。
![](https://uploadfiles.nowcoder.com/images/20211014/423483716_1634206291971/4A47A0DB6E60853DEDFCFDF08A5CA249)

数据范围： 
$0≤n≤1000$
要求：空间复杂度 $O(1)$ ，时间复杂度 $O(n)$ 。

如当输入链表{1,2,3}时，
经反转后，原链表变为{3,2,1}，所以对应的输出为{3,2,1}。
以上转换过程如下图所示：
![img](https://uploadfiles.nowcoder.com/images/20220115/80192007_1642255925694/D2B5CA33BD970F64A6301FA75AE2EB22)
```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @return ListNode类
#
class Solution:
    def ReverseList(self , head: ListNode) -> ListNode:
        # write code here
        if head == None:
            return None
        if head.next == None:
            return head

        leftPointer = head
        midPointer = head.next
        rightPointer=head.next.next
        leftPointer.next = None

        while rightPointer != None:
            midPointer.next = leftPointer
            leftPointer = midPointer
            midPointer = rightPointer
            rightPointer = rightPointer.next

        midPointer.next = leftPointer
        return midPointer
```