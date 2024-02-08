class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class MidList:
    def __init__(self):
        self.head = None
        self.len = 0

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        snapshot = self.head
        while snapshot.next:
            snapshot = snapshot.next

        snapshot.next = new_node
        self.len += 1

    # def length(self): 
    #     snapshot = self.head 
    #     self.len = 0  # Reset the length

    #     while snapshot: 
    #         self.len += 1
    #         snapshot = snapshot.next 

    #     return self.len

    def mid_list(self): 
        mid_point = self.len // 2

        snapshot = self.head
        for _ in range(mid_point):
            snapshot = snapshot.next

        return snapshot

    def display(self):
        if not self.head: 
            print("Linked List might be empty")

        snapshot = self.head 
        while snapshot: 
            print(snapshot.data, end="->")
            snapshot = snapshot.next

# Example Usage:
my_list = MidList()
my_list.display()  # This will print "Linked list is empty."

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.display()  # This will print "1->2->3->"
# print("Length:", my_list.length())

mid_node = my_list.mid_list()
print("Midpoint:", mid_node.data)
