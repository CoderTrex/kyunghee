class NodeType:
    """ Node Type """

    def __init__(self, item):
        self.info = item
        self.next = None


class QueType:
    def __init__(self):
        self.front = None
        self.rear = None

    def make_empty(self):
        while self.front != None:
            tempPtr = self.front
            self.front = self.front.next
            del tempPtr
        self.rear = None

    def is_full(self):
        try:
            location = NodeType("test")
            del location
            return False
        except:
            return True

    def is_empty(self):
        return self.front == None

    def enqueue(self, item):
        new_item = NodeType(item)
        if self.rear is None:
            self.front = new_item
        else:
            self.rear.next = new_item
        self.rear = new_item

    def dequeue(self):
        target = self.front
        item = target.info
        self.front = target.next
        if self.front is None:
            self.rear = None
        del target
        return item
