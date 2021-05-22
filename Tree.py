class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() *3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self,child):
        child.parent = self
        self.children.append(child)


def build_product_tree():
    root = Tree("Electronics")

    laptop = Tree("Laptop")
    laptop.add_child(Tree("Mac"))
    laptop.add_child(Tree("Surface"))
    laptop.add_child(Tree("Thinkpad"))

    cellphone = Tree("Cell Phone")
    cellphone.add_child(Tree("iPhone"))
    cellphone.add_child(Tree("Google Pixel"))
    cellphone.add_child(Tree("Vivo"))

    tv = Tree("TV")
    tv.add_child(Tree("Samsung"))
    tv.add_child(Tree("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    root.print_tree()


if __name__ == '__main__':
    build_product_tree()
