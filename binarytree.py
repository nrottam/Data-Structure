class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self,data):
        if self.data == data:
            return
        elif self.data > data:
            if self.left :
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        elif self.data < data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self,data):
        if self.data == data:
            return True
        elif self.right is None and self.left is None:
            return False
        if self.data > data:
            return self.left.search(data)
        if self.data < data:
            return self.right.search(data)



    def inorder_traversal(self):
        element = []
        if self.left:
            element += self.left.inorder_traversal()

        element.append(self.data)

        if self.right:
            element += self.right.inorder_traversal()
        return element

    def del_node(self,data):
        pass

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self, val):
        if val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        elif val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        else:
            if self.right is None and self.left is None:
                return None
            elif self.left is None:
                return self.right
            elif self.left is None:
                return self.left
            min_num = self.right.find_min()
            self.data = min_num
            self.right.delete(min_num)
        return self
                

def build_tree(element):
    root = BinarySearchTreeNode(element[0])
    for item in element:
        root.add_child(item)
    return root



if __name__ == '__main__':
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)

    print(country_tree.inorder_traversal())
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:", numbers_tree.inorder_traversal())

    print(numbers_tree.find_max())
    print(numbers_tree.find_min())
    numbers_tree.delete(18)
    print("In order traversal gives this sorted list:", numbers_tree.inorder_traversal())
