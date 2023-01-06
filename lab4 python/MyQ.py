
class MyQ:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = 0

    def insert(self,data):
        self.queue.append(data)
        self.rear = self.rear + 1

    def pop(self):
        if self.front == self.rear:
            print("Queue is Empty")
        else:
            self.queue.pop(0)
            self.rear = self.rear - 1

    def is_empty(self):
        if self.front == self.rear:
            print("Queue is Empty")
        else:
            print("the queue is not empty")

    def queueDisplay(self):

        if (self.front == self.rear):
            print("\nQueue is Empty")

        for i in self.queue:
            print(i, "<--", end='')
