from tkinter.tix import MAX


MAX_ITEMS = 100

class QueueType():
    def __init__(self):
        self.info = []

    def enqueue(self, data):
        self.info.append(data)

    def dequeue(self):
        return self.info.pop(0)

    def is_empty(self):
        return len(self.info) == 0

    def is_full(self):
        return len(self.info) == MAX_ITEMS

    def make_empty(self):
        self.info.clear()