class queue():
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        is_empty = False
        if len(self.queue) == 0:
            is_empty = True
        return is_empty
    
    def add_rear(self, item):
        self.queue.append(item)

    def add_front(self, item):
        self.queue.insert(0, item)
    
    def delete_rear(self):
        rear_object = None
        if self.isEmpty():
            pass
        else:
            rear_object = self.queue.pop()
        return rear_object
    
    def delete_front(self):
        front_object = self.queue[0]
        if self.isEmpty():
            pass
        else:
            front_object = self.queue.remove(front_object)
        return front_object
    
    def get_rear(self):
        return self.queue[-1]
    
    def get_front(self):
        return self.queue[0]
    
q = queue()

q.add_front(1)
q.add_front(2)
q.add_rear(3)
q.add_rear(4)

q.delete_front()
q.delete_rear()

print(q.queue)
print(q.get_front(), q.get_rear())