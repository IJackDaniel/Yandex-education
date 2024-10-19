class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def __str__(self):
        return f"[{self.data}] -> {self.next}"


class LinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, data):  # +
        temp = Node(data)
        temp.set_next(self.head)
        self.head = temp

    def pop_front(self):  # +
        current = self.head
        self.head = current.get_next()

    def show_last(self):  # +
        if self.head is None:
            return -1
        else:
            current = self.head
            data = current.get_data()
            return data

    def push_back(self, data):
        if self.is_empty():
            self.push_front(data)
        else:
            temp = Node(data)
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(temp)

    def find(self, x):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == x:
                found = True
            current = current.get_next()
        return found

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        cnt = 0
        while current is not None:
            cnt += 1
            current = current.get_next()
        return cnt

    def __str__(self):
        return str(self.head)


linked_list = LinkedList()

q = int(input())  # количество запросов
for _ in range(q):
    inp = list(input().split())
    request = int(inp[0])
    match request:
        case 1:  # Положить число x на вершину стека
            x = int(inp[1])
            linked_list.push_front(x)

        case 2:  # Достать число, лежащее на вершине стекка
            linked_list.pop_front()
        case _:
            continue
    print(linked_list.show_last())
