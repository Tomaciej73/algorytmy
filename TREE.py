from typing import *

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def is_leaf(self) -> bool:
        if len(self.children) == 0:
            return True
        return False

    def add(self, child: 'TreeNode') -> None:
        child.parent = self
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)

        for child in self.children:
            self.for_each_deep_first(visit(child))

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)

        fifo = self.rodzic
        while len(fifo):
            visit(fifo[0])
            print(fifo[0])
            fifo += fifo[0].rodzic
            del fifo[0]

    def get_level(self) -> int:
        poziom = 0
        p = self.parent
        while p:
            poziom += 1
            p = p.parent
        return poziom

    def print_tree(self):
        odstep = '|' * self.get_level() * 3
        if self.parent:
            znaczek = '=>'
        else:
            znaczek = ''
        print(odstep + znaczek + self.value)
        if self.children:
            for child in self.children:
                child.print_tree()

    def printing(self):
        print(self.value)

    def printing_branch(self):
        print(self.value)
        for x in self.children:
            print(x.value)

drzewko = TreeNode("F")
b = TreeNode("B")
a = TreeNode("A")
d = TreeNode("D")
c = TreeNode("C")
e = TreeNode("E")
g = TreeNode("G")
i = TreeNode("I")
h = TreeNode("H")
drzewko.add(b)
b.add(a)
b.add(d)
d.add(c)
d.add(e)
drzewko.add(g)
g.add(i)
i.add(h)

drzewko.print_tree()
