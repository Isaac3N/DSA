class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.before = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True

        else:
            return False

    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, data):
        if self.head is None:
            return

        elif self.head.data == data:
            current = self.head
            current.next = self.head

        else:
            current = self.head

            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                    return
                else:
                    current = current.next
            return "We could not find the data"

    def length(self):
        current = self.head
        count = 1

        while current.next:
            count += 1
            current = current.next

        return count

    def get_index(self, data):
        count = 0
        current = self.head

        while current.next:
            if current.data == data:
                return f"{data} was found at position {count}"

            elif current.data != data:
                count += 1
                current = current.next
            else:
                return "we could not find your data"

    def get_value(self, index):
        count = 0
        if index < 0:
            return "index out of range"

        current = self.head

        while current:
            if index == count:

                return f"at index {index}, {current.data}"
            else:
                count += 1
                current = current.next

        return "we could not find the index"

    def reversed(self):
        prev_node = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
        self.head = prev_node

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


list1 = LinkedList()
list2 = LinkedList()

list1.display()
list1.append(8)
list1.append(9)
list1.prepend(7)
list1.append(10)
list1.display()
print(list1.length())
# list1.remove(10)
list1.display()
print(list1.length())
print(list1.get_index(8))
list1.display()
# list1.reversed()
list1.display()

# print(list1.get_value(5))


list2.append(1)
list2.append(2)

list2.display()
