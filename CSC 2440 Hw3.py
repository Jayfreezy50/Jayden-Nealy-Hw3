#My Node where the data is stored
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#My LinkedList class just keeps all my methods in one organized class
class LinkedList:
    def __init__(self):
        self.head = None

#Inputdata adds the data_list into the LinkedList
    def inputData(self):
        list = [4, 2, 7, 1, 6, 3, 5]
        for data in list:
            self.append(data)

#append adds a node to the head, only the list is empty. If not empty it puts it at the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

#This sorts my list using a merge sort algorithm
    def merge_sort(self, head):
        if head is None or head.next is None:
            return head
        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None
        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)
        sorted_list = self.sorted_merge(left, right)
        return sorted_list

#get_middle just finds the middle node and splits it
    def get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

#sorted_merge merges the two sorted lists back together
    def sorted_merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result

#average_of_even finds the total value of the even numbers
    def average_of_even(self):
        current = self.head
        even_sum = 0
        even_count = 0
        while current:
            if current.data % 2 == 0:
                even_sum += current.data
                even_count += 1
            current = current.next
        return even_sum / even_count if even_count > 0 else 0

#print_list prints the elements of the list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

#This is the driver code
linked_list = LinkedList()
linked_list.inputData()

print("Unsorted List:")
linked_list.print_list()
linked_list.head = linked_list.merge_sort(linked_list.head)

print("Sorted List in Ascending Order:")
linked_list.print_list()

average_even = linked_list.average_of_even()
print("Average of even elements:", average_even)

#Results
# 1) The input of the list is [4, 2, 7, 1, 6, 3, 5]
# 2) With the use of my merge sort algorithm it sorts into Ascending order [1, 2, 3, 4, 5, 6, 7,]
# 3) Finally to find the average of even elements my code does 2 + 4 + 6 and divides by 3 and i get 4.0
