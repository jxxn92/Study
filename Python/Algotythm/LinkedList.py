
    #TODO LinkedList를 파이썬으로 만드는 방법

class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None
        self.length = 0
    def __len__(self):
        return self.length
    
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
        
    def display(self):
        if self.head is None:
            print("Empty List")
        else:
            node = self.head

            while node.next:
                print(node.data, end = " → ")
                node = node.next
            print(node.data)

    def search(self, item):
        
        node = self.head

        while node:
            if node.data == item:
                return True
            node = node.next
        return False 

    def pop_left(self):
        if self.head is None:
            return None
        node = self.head
        self.head = self.head.next
        self.length -= 1
        return node.data

    def pop_right(self):
        if self.head is None: # 비어있는 리스트
            return None
        node = self.head
        if node.next is None: # 값이 하나있는 리스트 
            self.head = None
        else:
            while node.next is not None: # 값이 두개이상 들어 있는 리스트
                prev = node
                node = node.next
            prev.next = None
        self.length -= 1
        return node.data
        '''
        리스트가 비어있는 경우 출력할 값이 없으므로 그냥 None를 하면 되고
        리스트에 값이 하나 존재하는 경우 그 값을 제거하면 head 가 None이 되므로 NONE로 만들어준다
        리스트에 값이 두개 이상 존재하느 경우 While 문으로 마지막 값까지 가면되는데 마지막값 바로 전 값의 link값이 None값이 되어야 하기 때문에
        While 문에서 다음 값으로 넘어 가는 과정중 prev에 넘어 가려는 값의 바로 전값을 저장 하면서 간다.
        그렇게 되면 마지막 값을 찾아서 While 문을 탈출 할대 prev에는 마지막 바로 전 값이 들어있으므로 그 값의 link 값을 None 로 만들어주면 된다.
        그리고 나서 length 값을 하나 감소 시키면 완성이다.
        '''
    def insert(self, i, item):
        if i <= 0: # 0보다 작으면 앞에 값을 추가하면 되므로 append_left()
            self.append_left(item)
        elif i >= self.length: # 원래 크기보다 크면 오른쪽으로 값을 추가 하면 되므로 append_ritgt()
            self.append_right(item)
        else: # 둘 다 아니라 값을 중간에 끼워 넣어야 한다면
            prev = self.head # 전 노드를 찾기 위해서 prev를 선언

            for _ in range(i-1): 
                prev = prev.next # 값을 넣을 위치 바로 전의 노드를 찾기 위해서 prev에 저장
            
            node = Node(item) # 새롭게 넣을  노드를 생성
            node.next = prev.next # 새롭게 만든 노드는 원래 있던 다음 노드의 값이 들어가야하므로 prev.next 가 가지고 있던 다음 노드의 값을 넣는다.
            prev.next = node # 새롭게 넣은 전의 노드의 next는 이제 새롭게 만든 노드를 가리켜야 하므로 node의 값을 대입한다
            self.length += 1 # 새롭게 값을 추가했으므로 length 를 1 추가한다.

    def remove(self, item):
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





mylist = Linked_list()
for data in (1, 2, 3, 4, 5, 6):
    mylist.append_right(data)

mylist.display()

remove_data = (1, 3, 6, 7)
for data in remove_data:
    if mylist.remove(data):
        mylist.display()
    else:
        print(f"There is no {data}")