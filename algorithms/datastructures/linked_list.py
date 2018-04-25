

class Node():

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return '{}->{}'.format(self.val, self.next.val if self.next else 'None')


def reverse_list(link):
    pre = None
    cur = link
    while cur:
        next = cur.next
        cur.next = pre
        pre, cur = cur, next
    return pre

l = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, ))))))

root = reverse_list(l)

while root:
    print(root)
    root = root.next


def recursive_reverse_list(head, new_head=None):
    if head is None:
        return
    if head.next is None:
        new_head = head
    else:
        new_head = recursive_reverse_list(head.next, new_head)
        head.next.next = head
        head.next = None

    return new_head

l = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, ))))))
root = recursive_reverse_list(l)

while root:
    print(root)
    root = root.next


def swap_pairs(head):
    if head != None and head.next != None:
        next = head.next
        head.next = swap_pairs(next.next)
        next.next = head
        return next
    return head


l = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, ))))))
root = swap_pairs(l)

while root:
    print(root)
    root = root.next

