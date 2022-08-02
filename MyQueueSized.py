class MyQueueSized:
    """
    Реализация структуры данных 'Очередь' на кольцевом буфере
    с использованием массива.

    Выполнена мною как самостоятельная работа
    в рамках обучения на курсе по 'Pyhton-разработчик'
    при прохождении темы 'Алгоритмы и структуры данных'.

    Пример команд:
    4
    3
    peek
    push 5
    push 2
    size
    сначала задаётся число команд, затем размер очереди, затем
    непосредственно команды.

    Существенный минус данной реализации - ограничение очереди
    размером массива. Плюс в том, что на такую реализацию
    требуется меньше памяти и доступ к данным происходит быстрее.
    """
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.size_of = 0

    def is_empty(self):
        return self.size_of == 0

    def push(self, item):
        if self.size_of < self.max_n:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_n
            self.size_of += 1
            return 'ok'
        else:
            return 'error'

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size_of -= 1
        return x

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]

    def size(self):
        return self.size_of


quantity = int(input())
max_size = int(input())
queue = MyQueueSized(max_size)
result = []


for item in range(quantity):
    command = input().split()

    if command[0] == 'push':
        act = queue.push(command[1])
        if act == 'error':
            result.append(act)

    if command[0] == 'pop':
        result.append(queue.pop())

    if command[0] == 'peek':
        result.append(queue.peek())

    if command[0] == 'size':
        result.append(queue.size())

for res in result:
    print(res)
