import sys

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def insert(self,data):
        new_node = Node(data)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node

    def display(self):
        curr = self.head
        print("head:", end='')
        while curr.next is not None:
            curr = curr.next
            print(f" > {curr.data}", end='')

    def length(self):
        curr = self.head
        total = 0
        while curr.next is not None:
            curr = curr.next
            total = total + 1
        return total

    def delAtIndex(self, index):
        if index>=self.length():
            print("Error: Index out of range")
            return
        curr = self.head
        pos = 0
        while True:
            prev = curr
            curr = curr.next
            if pos==index:
                prev.next = curr.next
                print("deleted")
                return
            pos += 1

    def getAtIndex(self, index):
        if index>=self.length():
            print("Error: Index out of range")
            return
        curr = self.head
        pos = 0
        while True:
            curr = curr.next
            if pos == index:
                print(f"Element at {index} is {curr.data}.")
                return
            pos += 1

ll = LinkedList()

while True:
    print("\nEnter:\n 1 to insert \
                 \n 2 to traverse \
                 \n 3 to delete an element at an index \
                 \n 4 to get an element at at an index \
                 \n 5 to exit.\n")
    ch = int(input())
    if ch == 1:
        ele = input("Enter an element to insert: ")
        ll.insert(ele)
    elif ch == 2:
        ll.display()
    elif ch == 3:
        index = int(input("Enter index of the element to be deleted: "))
        ll.delAtIndex(index)
        ll.display()
    elif ch == 4:
        index = int(input("Enter index of the element to be accessed: "))
        ll.getAtIndex(index)
    else:
        sys.exit()
'''
ll.insert(9)
ll.insert(5)
ll.insert([1,2])
ll.insert(4)
ll.display()
print(f"\nNo. Of elements: {ll.length()}")
ll.delAtIndex(10)
print(ll.getAtIndex(4))
'''
