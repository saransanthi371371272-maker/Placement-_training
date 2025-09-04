class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def intersectPoint(head1, head2):
    visNodes = set()

    
    curr1 = head1
    while curr1 is not None:
        visNodes.add(curr1)
        curr1 = curr1.next

    
    curr2 = head2
    while curr2 is not None:
        if curr2 in visNodes:
            return curr2  # Intersection point found
        curr2 = curr2.next

    return None


if __name__ == "__main__":

    # 
    head1 = Node(10)
    head1.next = Node(15)
    head1.next.next = Node(30)

    
    head2 = Node(3)
    head2.next = Node(6)
    head2.next.next = Node(9)

    
    head2.next.next.next = head1.next

    interPt = intersectPoint(head1, head2)

    if interPt is None:
        print("-1")
    else:
        print(interPt.data)
