from typing import Any

class Node:
    value= Any
    next= None

    def __repr__(self):
        if(self.next==None):
            return f'{self.value}'
        return f'{self.value} -> {self.next}'


class LinkedList:
    head= None
    tail= None

    def push(self, new_value):
        new_obj=Node()
        new_obj.value= new_value
        new_obj.next=self.head
        self.head=new_obj
        if(self.tail==None):
            self.tail=new_obj

    def append(self, new_value):
        new_obj=Node()
        new_obj.value= new_value
        if(self.tail!=None):
            self.tail.next=new_obj
        self.tail=new_obj
        if(self.head==None):
            self.head=new_obj

    def node(self,at): #licząc od 0 to pierwszy object
        temp=self.head
        while(at>0):
            if(temp.next!=None):
                temp=temp.next
                at-=1
            else:
                print("Lista nie posiada tyle pozycji")
                temp=None
                at=-1
        if(at!=0):
            return None
        return temp

    def insert(self, new_value, after):
        new_obj=Node()
        new_obj.value= new_value
        new_obj.next=after.next
        after.next=new_obj

    def pop(self):
        temp=self.head
        self.head=temp.next
        return temp.value

    def remove_last(self):
        temp=self.tail
        last=self.head
        while(last.next.next!=None):
            last=last.next
        last.next=None
        self.tail=last
        return temp.value

    def remove(self, after):
        after.next=after.next.next

    def __repr__(self):
        return f'{self.head}'

    def __len__(self):
        length=0
        temp=self.head
        while(temp!=None):
            length+=1
            temp=temp.next
        return length

list_ = LinkedList()
assert list_.head == None

list_.push(1)
list_.push(0)

assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)

assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)

assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

first_element = list_.node(at=0)
returned_first_element = list_.pop()

assert first_element.value == returned_first_element

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()
assert last_element.value == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(at=1)
list_.remove(second_node)

assert str(list_) == '1 -> 5'

assert 2==len(list_)