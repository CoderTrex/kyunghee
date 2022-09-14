MAX_ITEMS = 10


class NodeType:
    """ Node Type """

    def __init__(self, item):
        self.info = item
        self.next = None


class StackType:
    def __init__(self):
        self.topPtr = None

    def is_full(self):
        try:
            location = NodeType("test")
            del location
            return False
        except:
            return True

    def is_empty(self):
        return self.topPtr is None

    def push(self, item):
        new_item = NodeType(item)
        new_item.next = self.topPtr
        self.topPtr = new_item

    def pop(self):
        target = self.topPtr
        self.topPtr = self.topPtr.next
        del target

    def top(self):
        if self.is_empty():
            print("Failed to Top")
        else:
            return self.topPtr.info

    def __str__(self):
        location = self.topPtr
        while location != None:
            print(location.info, end=" ")
            location = location.next
