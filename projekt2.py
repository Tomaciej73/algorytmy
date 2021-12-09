from typing import *


class BinaryNode:
    value: Any
    left_child: None
    right_child: None
    parent: None

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

    def __str__(self):
        return str(self.value)

    def is_leaf(self):
        if self.right_child is None and self.left_child is None:
            return True
        return False

    def add_left_child(self, child):
        self.left_child = child
        self.left_child.parent = self

    def add_right_child(self, child):
        self.right_child = child
        self.right_child.parent = self

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        print(self.value)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)
        visit(self)
        print(self.value)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        print(self.value)
        if self.left_child is not None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_pre_order(visit)

    def get_level(self) -> int:
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level



class BinaryTree:
    root: BinaryNode

    def __init__(self, root: BinaryNode):
        self.root = root

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)

    def get_level(self) -> int:
        return 0


def bottom_line(root):
    if root is None:
        return
    head = 0 #wartosc dla root ustawiona na 0
    poziom = dict() #przechowuje pare kluczy jako wartosc
    queque = [] #kolejka do wezlow drzewa 
    root.head = head #przypisze wartosc do poziomu i przypisuje ja
    queque.append(root)

    while len(queque) != 0:
        help = queque[0]
        queque.pop(0)
        head = help.head #bierze wartosc z drzewa
        poziom[head] = help #umieszcza wezel drzewa do kolejki

        if help.left_child is not None:
            help.left_child.head = head - 1 #przechodzi po poziomach jesli dziecko tu jest sprawdza poziom nizej
            queque.append(help.left_child) #dodaj do kolejki lewe dziecko

        if help.right_child is not None:
            help.right_child.head = head + 1 #to samo co na gorze tylko dla prawego dziecko
            queque.append(help.right_child) #dodaj do kolejki prawe dziecka

    for i in sorted(poziom.keys()):
        print(poziom[i], end=' ') #slownik kluczow posortowany
#gdy bedzie nowy poziom umieszcza dane wezla jako klucz 
#Potem klucz jest wartoscia w ten sposob mozna zobaczyc najnizsze wartosci w drzewie
one = BinaryNode(1)
two = BinaryNode(2)
three = BinaryNode(3)
four = BinaryNode(4)
fife = BinaryNode(5)
seven = BinaryNode(7)
eight = BinaryNode(8)
nine = BinaryNode(9)

one.add_left_child(two)
two.add_left_child(four)
two.add_right_child(fife)
four.add_left_child(eight)
four.add_right_child(nine)
one.add_right_child(three)
three.add_right_child(seven)

tree = BinaryTree(one)
bottom_line(tree.root)


