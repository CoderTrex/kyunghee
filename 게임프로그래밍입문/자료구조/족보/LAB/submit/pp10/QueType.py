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
        if self.is_full():
            print("Failed to Enqueue")
        else:
            newNode = NodeType(item)
            if self.rear == None:
                self.front = newNode
            else:
                self.rear.next = newNode
            self.rear = newNode

    def dequeue(self):
        if self.is_empty():
            print("Failed to Dequeue")
            return
        else:
            tempPtr = self.front
            item = self.front.info
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            del tempPtr
            return item
