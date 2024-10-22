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
        self.tail = None

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def pop(self):
        if self.head is None:
            return None
        node = self.head
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return node.data

    def show_last(self):
        if self.head is None:
            return -1
        return self.head.data

    def __str__(self):
        return str(self.head)


linked_list = LinkedList()

q = int(input())  # количество запросов
for _ in range(q):
    inp = list(input().split())
    request = int(inp[0])
    match request:
        case 1:  # Положить число x в конец очереди
            x = int(inp[1])
            linked_list.push(x)

        case 2:  # удалить первый элемент из очереди
            linked_list.pop()
        case _:
            continue
    print(linked_list.show_last())

