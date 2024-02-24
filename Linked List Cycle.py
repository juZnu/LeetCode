def hasCycle( head):
    fp = head
    sp = head
    while fp and fp.next:
        sp = sp.next
        fp = fp.next.next
        if sp == fp:
            return True
    return False