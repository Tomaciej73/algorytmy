from typing import Any


class Node:
    def __init__(self, value=Any, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value: Any) -> None:
        node = Node(value, self.head)
        self.head = node

    def append(self, value: Any) -> None:
        if self.head is None:
            self.head = Node(value)
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = Node(value)

    def node(self, at: int) -> None:
        node = self.head
        for i in range(at):
            node = node.next
        if node is not None:
            print(node.value)

    def pop(self) -> Any:
        node = self.head
        self.head = node.next
        return node

    def remove_last(self) -> Any:
        node = self.head
        for i in range(self.len() - 2):
            node = node.next
        last = node.next
        node.next = None
        return last

    def print(self):
        itr = self.head
        while itr is not None:
            print(str(itr.value), '->', end=' ')
            itr = itr.next
        print(None)

    def len(self) -> Any:
        node = self.head
        count = 1
        while node.next:
            count += 1
            node = node.next
        return count


class Stack:
    def __init__(self):
        self.head = None

    def push(self, element: Any) -> None:
        node = Node(element, self.head)
        self.head = node

    def pop(self) -> Any:
        node = self.head
        self.head = node.next
        return node

    def print(self):
        itr = self.head
        while itr is not None:
            print(itr.value)
            itr = itr.next

    def len(self) -> Any:
        node = self.head
        count = 1
        while node.next:
            count += 1
            node = node.next
        print(count)


class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self, element: Any) -> None:
        if self.head is None:
            self.head = Node(element)
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = Node(element)

    def dequeue(self) -> Any:
        node = self.head
        self.head = node.next
        return node

    def print(self):
        itr = self.head
        while itr is not None:
            print(itr.value)
            itr = itr.next

    def len(self) -> Any:
        node = self.head
        count = 1
        while node.next:
            count += 1
            node = node.next
        print(count)


list_ = LinkedList()
list_.push(1)
list_.push(0)
list_.print()
list_.append(9)
list_.append(10)
list_.print()
list_.pop()
list_.print()
list_.remove_last()
list_.print()
print(list_.len())
list_.node(1)

print('----------')

stack = Stack()
stack.push(0)
stack.push(1)
stack.push(2)
stack.print()
print('-')
stack.len()
print('-')
stack.pop()
stack.print()
print('-')
stack.len()

print('----------')

queue = Queue()
queue.enqueue("klient1")
queue.enqueue("klient2")
queue.enqueue("klient3")
queue.enqueue("klient4")
queue.print()
queue.len()
queue.dequeue()
queue.dequeue()
queue.print()
queue.len()