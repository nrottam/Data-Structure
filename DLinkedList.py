#Implimentation of Doubly Linked List
#
class Node:
    def __init__(self,data=None ,next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self,data):
        node = Node(data,next= self.head, prev = None)
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def print(self):
        itr = self.head
        strdll = ''
        while itr:
            strdll = strdll  + str(itr.data) + '<-->'
            itr = itr.next
        print(strdll)

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        itr = self.head
        while itr:
            if itr.data == data_after:
                nn = Node(data_to_insert,itr.next,itr)
                itr.next = nn
            itr = itr.next

    def remove_by_value(self, data):
        # Remove first node that contains data
        itr = self.head
        while itr:
            if itr.data == data:
                itr.prev.next = itr.next
                itr.next.prev = itr.prev
            itr = itr.next


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_at_beg(3)
    dll.insert_at_beg(5)
    dll.insert_at_beg(12)
    dll.insert_at_beg(34)
    dll.insert_at_beg(22)
    dll.print()
    dll.insert_after_value(12,15)
    dll.print()
    dll.remove_by_value(12)
    dll.print()