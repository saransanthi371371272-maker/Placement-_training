class Solution:

    def length(self, node):
        
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def reverse(self, head):
        
        prev = None
        current = head
        while current:
            next_node = current.next  
            current.next = prev  
            prev = current  
            current = next_node
        return prev

    def subLinkedList(self, head1, head2):
        
        n1 = self.length(head1)
        n2 = self.length(head2)

        
        if n2 > n1:
            head1, head2 = head2, head1

        if n1 == n2:
            t1, t2 = head1, head2
            while t1 and t2 and t1.data == t2.data:
                t1 = t1.next
                t2 = t2.next
                if t1 is None:
                    return Node(0)  # Both numbers are equal

            if t2 and (t1 is None or t2.data > t1.data):
                head1, head2 = head2, head1

        head1 = self.reverse(head1)
        head2 = self.reverse(head2)

        result = None
        t1, t2 = head1, head2

        while t1:
            small = t2.data if t2 else 0

            if t1.data < small:
                if t1.next:
                    t1.next.data -= 1
                t1.data += 10

            new_node = Node(t1.data - small)
            new_node.next = result
            result = new_node

            t1 = t1.next
            if t2:
                t2 = t2.next

        # Remove leading zeros
        while result and result.data == 0:
            result = result.next

        if result is None:
            return Node(0)

        return result
