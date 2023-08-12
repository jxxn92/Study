class queue():
    def __init__(self):
        self.queue = []
    
    def enqueue_right(self, data):
        self.queue.append(data)
    
    def enqueue_left(self, data):
        self.queue.insert(0,data)
    
    def dequeue_right(self):
        dequeue_right_object = None
        if self.isEmpty():
            pass
        else:
            dequeue_right_object = self.queue.pop()
            self.queue = self.queue[:len(self.queue)-1]
        return dequeue_right_object
    
    def dequeue_left(self):
        dequeue_left_object = None
        if self.isEmpty():
            pass
        else:
            dequeue_left_object = self.queue[0]
            self.queue = self.queue[1:]

        return dequeue_left_object
    
    def size(self):
        return len(self.queue)

    def isEmpty(self):
        is_empty = False
        if len(self.queue) == 0:
            pass
        else:
            is_empty = True
        
        return is_empty
q = queue()

q.enqueue_left(1)
q.enqueue_left(2)
q.enqueue_left(3)
q.enqueue_right(0)

q.dequeue_left()
q.dequeue_right()


print(q.queue)