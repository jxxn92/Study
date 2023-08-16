import sys
#TODO 1. 1 X: 정수 X를 덱의 앞에 넣는다. (1 ≤ X ≤ 100,000) => add_rear v
#TODO 2. 2 X: 정수 X를 덱의 뒤에 넣는다. (1 ≤ X ≤ 100,000) => add_fornt v
#TODO 3. 3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다. => delete_front v
#TODO 4. 4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다. => delete_rear v
#TODO 5. 5: 덱에 들어있는 정수의 개수를 출력한다. => size v
#TODO 6. 6: 덱이 비어있으면 1, 아니면 0을 출력한다. => isEmpty v
#TODO 7. 7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다. => get_front
#TODO 8. 8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다. => get_rear

class Deque_up():
    def __init__(self):
        self.deque = []
    
    def isEmpty(self):
        is_empty = 0
        if len(self.deque) == 0:
            is_empty = 1   
        return is_empty
    
    def size(self):
        return len(self.deque)

    def add_rear(self, item):
        self.deque.append(item)

    def add_front(self, item):
        self.deque.insert(0,item)
    
    def delete_front(self):
        del_front_obj = None
        if self.isEmpty():
            print(-1)
        else:
            del_front_obj = self.deque.pop()
        return del_front_obj
    
    def delete_rear(self):
        del_rear_obj = None
        if self.isEmpty():
            print(-1)
        else:
            del_rear_obj = self.deque[0]
            del self.deque[0]
        return del_rear_obj

    def get_back(self):
        get_back_obj = None
        if self.isEmpty():
            print(-1)
        else:
            get_back_obj = self.deque[-1]
        return get_back_obj

    def get_front(self):
        get_front_obj = None
        if self.isEmpty():
            print(-1)
        else:
            get_front_obj = self.deque[0]
        return get_front_obj

d = Deque_up()

n = int(sys.stdin.readline())

for _ in range(n):
    s = sys.stdin.readline().split()

    if s[0] == '1':
        d.add_front(s[1])
    elif s[0] == '2':
        d.add_rear(s[1])
    elif s[0] == '3':
        print(d.delete_front())
    elif s[0] == '4':
        print(d.delete_rear())
    elif s[0] == '5':
        print(d.size())
    elif s[0] == '6':
        print(d.isEmpty())
    elif s[0] == '7':
        print(d.get_front())
    elif s[0] == '8':
        print(d.get_back())