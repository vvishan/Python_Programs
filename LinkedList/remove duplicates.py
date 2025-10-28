class Listnode:

    def __init__(self,val=0,next = None):
        self.val = val
        self.next = None
        
    def remove_duplicate(self,head:Listnode):
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur.next = cur
        return head
    def reverse_list(self,head:Listnode):
        cur = head
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
    
    def merge_two_sorted_lists(self,list1:Listnode,list2:Listnode):
        d = Listnode()
        curr = d

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next

        curr.next = list1 if list1 else list2
        return d.next

    def has_cycle(self,head:Listnode):
        dummy = Listnode()
        dummy.next = head
        slow = fast = dummy

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow in fast:
                return True
        return False
    def middle_link(self,head:Listnode):
        curr = head
        slow = fast = curr

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def remove_the_Nth_element_from_last(self,head:Listnode,n:int):

        dummy = Listnode()
        dummy.next = head
        ahead = bhind = head

        for _ in range(n+1):
            ahead = ahead.next

        while ahead:
            bhind = bhind.next
            ahead = ahead.next

        bhind.next = bhind.next.next
        return dummy.next
    
    