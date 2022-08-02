class NodeQueue:
    """
    Реализация структуры данных 'Очередь' на кольцевом буфере
    с использованием связного списка.

    Выполнена мною как самостоятельная работа
    в рамках обучения на курсе по 'Pyhton-разработчик'
    при прохождении темы 'Алгоритмы и структуры данных'.

    Пример команд:
    5
    put -34
    put -23
    get
    size
    get
    сначала задаётся общее число команд, затем сами команды.

    Плюс данно реализации в том, что нет ограничения на размер очереди.
    Но при таком способе требуется больше памяти и увеличивается
    время доступа к данным.
   """
    class Node:
        def __init__(self, value=None, next=None) -> None:
            self.value = value
            self.next = next

        def __str__(self) -> str:
            return self.value

    def __init__(self) -> None:
        self.head = self.Node()
        self.tail = self.Node()
        self.size_of = 0

    def is_empty(self):
        return self.size_of == 0

    def get(self):
        if self.is_empty():
            return 'error'
        if self.size_of == 1:
            x = self.head
            self.head = self.Node()
            self.tail = self.Node()
            self.size_of -= 1
            return x
        if self.size_of == 2:
            x = self.head
            self.head = self.tail
            self.size_of -= 1
            return x
        x = self.head
        self.head = self.tail.next.next
        self.tail.next = self.head
        self.size_of -= 1
        return x

    def put(self, item):
        if self.size_of == 0:
            self.head = self.Node(value=item)
            self.tail = self.head
        else:
            self.tail.next = self.Node(value=item)
            self.tail.next.next = self.head
            self.tail = self.tail.next
        self.size_of += 1

    def size(self):
        return self.size_of


quantity = int(input())
n_queue = NodeQueue()
result = []

for item in range(quantity):
    command = input().split()

    if command[0] == 'get':
        result.append(n_queue.get())

    if command[0] == 'put':
        res = n_queue.put(command[1])
        if res == 'error':
            result.append(res)

    if command[0] == 'size':
        result.append(n_queue.size())

for res in result:
    print(res)
