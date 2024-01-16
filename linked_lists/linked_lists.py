class Node: 
    def __init__(self, data= None): 
        self.data = data 
        self.next = None



class LinkedList: 

    def __init__(self): 
        self.head = Node()

    def append(self, data):
        snapshot = self.head 
        new_node = Node(data)

        while snapshot.next: 
            snapshot = snapshot.next 

        snapshot.next = new_node

    def length(self):
        count = 0 
        snapshot = self.head 

        while snapshot.next: 
            snapshot = snapshot.next 
            count +=1 

        return count 


    def get(self, index): 
        snapshot = self.head
        count = 0

        while snapshot: 
            
            if count == index: 
                return snapshot.data

            count +=1 
            snapshot = snapshot.next  


    def remove(self, element): 

        snapshot = self.head

        while snapshot: 
            if snapshot.next.data == element: 
                snapshot.next = snapshot.next.next
            snapshot = snapshot.next 



    
    def display(self): 
        snapshot = self.head

        while snapshot: 
            print(snapshot.data, end= "-->")
            snapshot = snapshot.next 



list1 = LinkedList()

# print(list1.length())
list1.append(7)
list1.append(8)
list1.append(9)
list1.append(10)
list1.remove(10)
print(list1.length())
print("hey",list1.get(2))

list1.display()

    