import MyQ

class QueueOutOfRangeException(Exception):
    pass

class Another(MyQ.MyQ):
    instances = {}
    def __init__(self, name, size):
        super().__init__()
        self.size = size
        self.name = name
        Another.instances[self.name] = self.queue

    def insert(self, value):
        if len(self.queue) == self.size:
            raise QueueOutOfRangeException("cannot insert values into full list")
        else:
            super().insert(value)


q = Another("q1", 3)
q2 = Another("q2", 3)
print(Another.instances)
q.insert("50")
q.insert("50")
q.insert("50")
print(Another.instances)
