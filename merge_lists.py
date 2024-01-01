class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class CreateLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next


class MergeLinkedList:

    def __init__(self):
        self.head = Node()

    def merge_lists(self, list1, list2):

        snapshot = self.head

        while list1 and list2:

            if list1.data > list2.data:
                snapshot.next = list1
                list1 = list1.next

            else:
                snapshot.next = list2
                list2 = list2.next

            snapshot = snapshot.next

        if list1:
            snapshot.next = list1

        if list2:
            snapshot.next = list2

        return self.head.next


list1 = CreateLinkedList()
list2 = CreateLinkedList()

list1.add_node(1)
list1.add_node(2)
list1.add_node(4)
print("List 1:")
list1.display()

list2.add_node(1)
list2.add_node(3)
list2.add_node(5)
print("\nList 2:")
list2.display()

merge_lists = MergeLinkedList().merge_lists(list1, list2)

print("\nMerged List:")
merge_lists.display()
