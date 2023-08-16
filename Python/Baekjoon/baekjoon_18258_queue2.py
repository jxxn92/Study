
    #TODO vv push X: 정수 X를 큐에 넣는 연산이다.
    #TODO vv pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    #TODO vv size: 큐에 들어있는 정수의 개수를 출력한다.
    #TODO vv empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
    #TODO vv front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    #TODO vv back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    #TODO 이거 최적화 하기 그냥 함수 따로 빼지말고 그냥 한번에 만들어서 정리해버리기 !
import sys

class queue():
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        is_empty = 0
        if len(self.queue) == 0:
            is_empty = 1

        return is_empty
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.isEmpty():
            return -1
        else:
            dequeue_object = self.queue[0]
            del self.queue[0]
            
        return dequeue_object
    
    def size(self):
        return len(self.queue)
    
    def front(self):
        front_object = None
        if self.isEmpty():
            return -1
        else:
            front_object = self.queue[0]
        
        return front_object

    def back(self):
        back_object = None
        if self.isEmpty():
            return -1
        else:
            back_object = self.queue[-1]
        
        return back_object
    
q = queue()

n = int(sys.stdin.readline())

for _ in range(n):
    a = list(sys.stdin.readline().split())
    if a[0] == 'push':
        q.enqueue(a[1])
    elif a[0] == 'front':
        print(q.front())
    elif a[0] == 'back':
        print(q.back())
    elif a[0] == 'size':
        print(q.size())
    elif a[0] == 'empty':
        print(q.isEmpty())
    elif a[0] == 'pop':
        print(q.dequeue())