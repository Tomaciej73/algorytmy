from typing import Any, Callable

class BinaryNode:

    def __init__(self, value:Any):
        self.value = value
        self.left: BinaryNode = None
        self.right: BinaryNode = None
        self.parent: BinaryNode = None

    def __str__(self):
        return str(self.value)

    def level_of(self):
        level = 0
        parent = self.parent
        while parent != None:
            level += 1
            parent = parent.parent
        return level

    def is_leaf(self):
        if self.left or self.right:
            return False
        return True

    def add_left_child(self, value:Any):
        self.left = BinaryNode(value)
        self.left.parent = self

    def add_right_child(self, value: Any):
        self.right = BinaryNode(value)
        self.right.parent = self

    def traverse_in_order(self, visit:Callable[['Any'], None]):
        if self.left:
            self.left.traverse_in_order(visit)
        visit(self)
        if self.right:
            self.right.traverse_in_order(visit)
        visit(self)

    def traverse_post_order(self, visit:Callable[['Any'], None]):
        if self.left:
            self.left.traverse_post_order(visit)
        if self.right:
            self.right.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit:Callable[['Any'], None]):
        visit(self)
        if self.left:
            self.left.traverse_pre_order(visit)
        if self.right:
            self.right.traverse_pre_order(visit)
        visit(self)

class BinaryTree:
    def __init__(self, root: BinaryNode):
        self.root = root

    def traverse_in_order(self, visit:Callable[['Any'], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit:Callable[['Any'], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit:Callable[['Any'], None]):
        self.root.traverse_pre_order(visit)

    def show(self):
        spacer = " |-|"
        if type(self) is BinaryTree:
            if self.root.left:
                BinaryTree.show(self.root.left)
            print("|"+str(self.root.value)+"|")
            if self.root.right:
                BinaryTree.show(self.root.right)
        if type(self) is BinaryNode:
            if self.left:
                BinaryTree.show(self.left)

            print(spacer*self.level_of()+str(self.value)+"|")
            if self.right:
                BinaryTree.show(self.right)

def visit(node:BinaryNode):
    print(node.value)

drzewo = BinaryNode(100)
drzewo.add_left_child(10)
drzewo.add_right_child(45)

drzewo.left.add_left_child(20)
drzewo.left.add_right_child(8)
drzewo.right.add_left_child(53)
drzewo.right.add_right_child(70)

drzewo.right.right.add_left_child(81)
drzewo.right.right.add_right_child(24)
drzewo.left.left.add_left_child(25)
drzewo.left.left.add_right_child(15)

drzewo.left.left.left.add_left_child(48)
drzewo.left.left.left.add_right_child(31)
drzewo.left.left.right.add_left_child(17)
drzewo.left.left.right.add_right_child(21)

bt = BinaryTree(drzewo)

bt.show()

#drzewo.traverse_post_order(visit)
print("")
#bt.traverse_post_order(visit)