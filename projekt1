from typing import Any

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value:Any) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value:Any) -> None:
        new_node = Node(value)
        if (self.head == None):
            self.head = new_node
            return
        current = self.head
        while(current.next):
            current = current.next
        current.next = new_node

    def node(self, at: int) -> Node:
        node = self.head
        if (self.head == None):
            print("empty")
            return
        for x in range(at):
            node = node.next
        return node

    def __len__(self):
        node = self.head
        if (self.head == None):
            return 0
        licznik = 0
        while (node.next):
            node = node.next
            licznik += 1
        return licznik + 1

    def insert(self, value: Any, after: Node) -> None:
        node = Node(value)
        node.next = after.next
        after.next = node

    def remove_last(self) -> Any:
        if (self.head == None):
            print("empty")
            return
        node = self.head
        node2 = self.head
        if (self.head.next == None):
            temp = self.head
            self.head = None
            return temp
        while (node.next != None):
            node = node.next
        while (node2.next != node):
            node2 = node2.next
        temp = node
        node2.next = None
        return temp

    def pop(self) -> Any:
        if (self.head == None):
            print("empty")
            return
        current = self.head
        self.head = current.next
        return current.value

    def remove(self, after: Node) -> Any:
        if (self.head == None):
            print("empty")
            return
        node = after.next
        node2 = node.next
        after.next = node2

    def __str__(self):
        node = self.head
        text = ""
        while node is not None:
            text += str(node.value)
            if node.next is not None:
                text += " -> "
            node = node.next
        return text



# lista = LinkedList()
# print("lista: ")
# lista.append(1)
# lista.append(2)
# lista.append(3)
# lista.append(4)
# lista.append(5)
# lista.append(6)
# lista.append(7)
# print(lista)
# print("\n0 na poczatku: ")
# lista.push(0)
# print(lista)
# print("\nusuniecie ostatniego: ")
# lista.remove_last()
# print(lista)
# print("\nusuniecie pierwszego: ")
# lista.pop()
# print(lista)
# print("\nusuniecie wezla nr 3: ")
# lista.remove(after=lista.node(2))
# print(lista)
# print("\ndlugosc listy: ")
# print(len(lista))




class Stack():
    _storage: LinkedList()

    def __init__(self):
        self.head = None

    def push(self, value: Any) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def __len__(self):
        print(" ")
        node = self.head
        if self.head == None:
            return 0
        licznik = 0
        while (node.next != None):
            node = node.next
            licznik += 1
        return licznik + 1

    def pop(self) -> Any:
        if (self.head == None):
            print("empty")
            return
        current = self.head
        self.head = current.next
        return current.value

    def __str__(self):
        node = self.head
        text = ""
        while node is not None:
            text += str(node.value)
            if node.next is not None:
                text += "\n"
            node = node.next
        return text


# stack = Stack()
# stack.push(20)
# stack.push(30)
# stack.push(40)
# print(stack)
# print(" ")
# print(stack.pop())
# print(" ")
# print(stack)
# print(len(stack))


class Queue():
    _storage: LinkedList

    def __init__(self):
        self.head = None

    def peek(self) -> Any:
        node = self.head
        if (node == None):
            print("empty")
            return
        return node.value

    def enqueue(self, value: Any) -> None:
        new_node = Node(value)
        if (self.head == None):
            self.head = new_node
            return
        current = self.head
        while (current.next):
            current = current.next
        current.next = new_node

    def dequeue(self) -> Any:
        if (self.head == None):
            print("empty")
            return
        current = self.head
        self.head = current.next
        return current.value

    def __len__(self):
        print(" ")
        node = self.head
        if self.head == None:
            return 0
        licznik = 0
        while (node.next != None):
            node = node.next
            licznik += 1
        return licznik + 1

    def __str__(self):
        node = self.head
        text = ""
        while node is not None:
            text += str(node.value)
            if node.next is not None:
                text += ", "
            node = node.next
        return text


# queue = Queue()
# queue.enqueue('klient 1')
# queue.enqueue('klient 2')
# queue.enqueue('klient 3')
# queue.enqueue('klient 4')
# queue.enqueue('klient 5')
# print("pierwszy w kolejce: " + queue.peek())
# print(queue)
# queue.dequeue()
# print(queue)
# print(len(queue))
