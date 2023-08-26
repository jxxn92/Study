class Node:
    def __init__(self, item, prev = None, next = None):
        self.data = item
        self.prev = prev
        self.next = next
    
class DBList:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def __str__(self):
        node = self.head
        result = ""
        while node is not None:
            result = result + str(node.data) + " "
            node = node.next
    
        return result
    
    def __len__(self):
        node = self.head
        cnt = 0
        while node:
            cnt += 1
            node = node.next
        
        return cnt
    
    def empty(self):
        return not bool(self.head)

    def appendleft(self, item):
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
        else:
            node = self.head
            new_node = Node(item, next=node)
            node.prev = new_node
            self.head = new_node
        
    def append(self, item):
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
        else:
            node = self.tail
            new_node = Node(item, prev=node)
            node.next = new_node
            self.tail = new_node
    
    def insert_before(self, next_data, new_data):
        if self.head is None:
            self.head = Node(new_data)
            self.tail = self.head
        else:
            node = self.tail
            while node.data != next_data:
                node = node.prev
                if node is None:
                    return False
            prev_node = node.prev
            new_node = Node(new_data, prev=prev_node, next=node)

            if prev_node:
                prev_node.next = new_node
            else:
                self.head = new_node
            node.prev = new_node
        return True
    
    def insert_after(self, prev_data, new_data):
        if self.head is None:
            self.head = Node(new_data)
            self.tail = self.head
        else:
            node = self.head
            while node.data != prev_data:
                node = node.next
                if node is None:
                    return False
            next_node = node.next
            new_node = Node(new_data,prev=node,next=next_node)

            if next_node:
                next_node.prev = new_node
            else:
                self.tail = new_node
        node.next = new_node
        return True
    
    def pop(self):
        if self.head is None:
            raise IndexError("Linked list is Empty")
        item = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = None

        return item
    
    def popleft(self):
        if self.head is None:
            raise IndexError("Linked list is Empty")
        item = self.head.data
        self.head = self.head.next
        self.head.prev = None
        return item

if __name__ == '__main__':
    DL = DBList()
    DL.append(1); DL.append(3); DL.append(5); print(DL)
    DL.appendleft(100); print(DL)
    DL.insert_after(1, 2); print(DL)
    DL.insert_before(5, 4); print(DL); print(len(DL))
    DL.pop(); print(DL)
    DL.popleft(); print(DL)
    print(len(DL))