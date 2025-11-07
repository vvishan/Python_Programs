class Listnode:
    def __init__(self,val =0,next=None):
        self.val = val
        self.next = None

    def remove_dup(head:Listnode):
        curr = head

        while curr:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr.next = curr

        return head
    
    def reverse_list(head:Listnode):
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    def merge_two_lists(head:Listnode,list1,list2):
        dummy = Listnode()
        curr = dummy

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
        return dummy.next

    def has_cycle(head:Listnode):
        dummy = Listnode()
        dummy.next = head
        fast = slow = dummy

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow in fast:
                return True
        return False
    def middle_link(head:Listnode):
        curr = head
        slow = fast = curr

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
