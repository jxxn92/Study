class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        if self.head is None:
            return "Empty List"
        else:
            node = self.head
            string = ""
            while node.next:
                string += str(node.data) + '->'
                node = node.next
            return string + str(node.data)
        
    def __contains__(self, val):
        node = self.head

        while node:
            if node.data == val:
                return True
            node = node.next
        return False

    def append_left(self, item):
        node = Node(item)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

        self.length += 1
    
    def append_right(self, item):
        node = Node(item)

        if self.head is None:
            self.head = node
        else:
            prev = self.head
            while prev.next:
                prev = prev.next
            prev.next = node
        
        self.length += 1
    
    def pop_left(self):
        if self.head is None:
            return None
        node = self.head
        self.head = self.head.next
        # self.head = node.next 
        # 이거는 불가능한가?
        self.length -= 1

        return node.data
    
    def pop_right(self):
        if self.head is None:
            return None
        node = self.head
        if self.head.next is None:
            self.head = None
        else:
            while node.next:
                prev = node
                node = node.next
            prev.next = None
        self.length -= 1
        
        return node.data

    def insert(self, pos, item):
        if pos <= 0:
            self.append_left(item)
        elif pos >= self.length:
            self.append_right(item)
        else:
            prev = self.head

            for _ in range(pos-1):
                prev = prev.next

            node = Node(item)
            node.next = prev.next
            prev.next = node
            self.length += 1
    
    def delete(self, item):
        if self.head.data == item:
            self.pop_left()
            return True
        prev = self.head
        while prev.next:
            if prev.next.data == item:
                prev.next = prev.next.next
                self.length -= 1
                return True
            prev = prev.next
        
        return False
    
    def reverse(self):
        if self.length <= 1:
            return
        ahead = self.head.next
        prev = self.head
        prev.next = None

        while ahead:
            self.head = ahead
            ahead = ahead.next
            self.head.next = prev
            prev = self.head


    # def display(self):
    #     if self.head is None:
    #         print("Empty List")
    #     else:
    #         node = self.head

    #         while node.next:
    #             print(node.data, end = "->")
    #             node = node.next
    #         print(node.data)
    
    # def search(self, val):

    #     node = self.head

    #     while node:
    #         if node.data == val:
    #             return True
    #         node = node.next
    #     return False

mylist = LinkedList()

for i in range(5):
    mylist.append_right(i)

print("원래 리스트: ", end = " ")
print(mylist)

mylist.reverse()
print("뒤집은 리스트: ", end = " ")
print(mylist)