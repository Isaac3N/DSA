class Node:
    def __init__(self, next, data=None):
        self.data = data
        self.next = next


class MergeList:
    def __init__(self):
        self.head = Node

    def merge_list(self, list1, list2):

        merged_list = MergeList()
        current_1 = list1.head
        current_2 = list2.head

        while current_1 or current_2:
            if current_1 and (current_1 >= current_2):
                current_1 += merged_list
                current_1 = current_1.next

            else:
                current_2 += merged_list
                current_2 = current_2.next

            return merged_list
