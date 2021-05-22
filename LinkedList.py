# Benifits of LinkedList
# 1.


# Complexity
# Indexing O(n)
#Inserting/Delete Element at Start O(1)

class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def print(self):
        if self.head is None:
            print('LinkedList is Empty')
        itr = self.head
        llstr = ''
        while itr:
            llstr = llstr + str(itr.data) + '--->'
            itr = itr.next
        print(llstr)

    def insert_items(self,listofitem):
        for item in listofitem:
            self.insert_at_end(item)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count = count+1
            itr = itr.next
        return count

    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
            count = count + 1
            itr = itr.next

    def insert_at(self,index,data):
        if index == 0:
            self.insert_at_beg(data)
        elif index == self.get_length():
            self.insert_at_end(data)
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                nn = Node(data,itr.next)
                itr.next = nn
            count = count +1
            itr = itr.next

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        itr = self.head
        while itr:
            if itr.data == data_after:
                nn = Node(data_to_insert,itr.next)
                itr.next = nn
                return
            itr = itr.next

    def remove_by_value(self, data):
        # Remove first node that contains data
        p = self.head
        n = p.next
        if p.data == data:
            self.head = n
        while n:
            if n.data == data:
                p.next = n
            n = n.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_items([1,2,3,4,6])
    ll.print()
#    ll.insert_at(0,5)
    ll.insert_after_value(3,8)
    ll.print()
    ll.remove_by_value(3)
    ll.print()
