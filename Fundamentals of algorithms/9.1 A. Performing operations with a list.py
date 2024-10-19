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

    def push_front(self, data):
        temp = Node(data)
        temp.set_next(self.head)
        self.head = temp

    def push_back(self, data):
        if self.is_empty():
            self.push_front(data)
        else:
            temp = Node(data)
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(temp)

    def push_choice(self, place, data):  # +
        if place == 0:
            temp = Node(data)
            temp.set_next(self.head)
            self.head = temp
        else:
            temp = Node(data)
            current = self.head
            i = 1
            while i != place:
                current = current.get_next()
                i += 1
            temp.set_next(current.get_next())
            current.set_next(temp)

    def find_choice(self, place):  # +
        current = self.head
        i = 1
        while i != place:
            current = current.get_next()
            i += 1
        return current.get_data()

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

    def delit_choice(self, place):
        if place == 1:
            current = self.head
            self.head = current.get_next()
        else:
            current = self.head
            i = 1
            while i != place - 1:
                current = current.get_next()
                i += 1
            next = current.get_next()
            current.set_next(next.get_next())


    def __str__(self):
        return str(self.head)


linked_list = LinkedList()
# linked_list.push_choice(0, 5)
# print(linked_list)
# print(linked_list.find_choice(1))
# linked_list.delit_choice(1)
# print(linked_list)

q = int(input())  # количество запросов
for _ in range(q):
    inp = list(input().split())
    request = int(inp[0])
    match request:
        case 1:  # Добавить число y после x-ого числа в списке
            # Если x = 0, то нужно сделать число y новым началом списка
            x, y = int(inp[1]), int(inp[2])
            linked_list.push_choice(x, y)

        case 2:  # Вывести число, которое находится на позиции x в списке
            x = int(inp[1])
            print(linked_list.find_choice(x))
        case 3:  # Удалить число, которое находится на позиции x в списке
            x = int(inp[1])
            linked_list.delit_choice(x)
        case _:
            continue

### request 1 test
# linked_list = LinkedList()
# linked_list.push_front(1)
# linked_list.push_front(2)
# linked_list.push_front(3)
# print(linked_list)
# linked_list.push_choice(5, 1)
# print(linked_list)

### request 2 test
# linked_list = LinkedList()
# linked_list.push_front(6)
# linked_list.push_front(5)
# linked_list.push_front(7)
# print(linked_list)
# print(linked_list.find_choice(2))

### request 3 test
# linked_list.push_front(1)
# linked_list.push_front(2)
# linked_list.push_front(3)
# print(linked_list)
# linked_list.delit_choice(1)
# print(linked_list)
