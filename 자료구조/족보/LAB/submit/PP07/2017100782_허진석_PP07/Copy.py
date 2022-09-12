from inspect import stack
from tkinter.messagebox import NO


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
        return self.topPtr == None

    def push(self, item):
        if self.is_full():
            print("Failed to Push")
        else:
            location = NodeType(item)
            location.next = self.topPtr
            self.topPtr = location

    def pop(self):
        if self.is_empty():
            print("Failed to Pop")
        else:
            tempPtr = self.topPtr.info
            self.topPtr = self.topPtr.next
            return tempPtr

    def top(self):
        if self.is_empty():
            print("Failed to Top")
        else:
            return self.topPtr.info

    def __str__ (self):

        location = self.topPtr
        items = []
        while location != None:
            items.append(location.info)
            location = location.next

        return " ".join(items)

    def copy(self, anotherStack):
        self.topPtr = None
        tmp = anotherStack.topPtr
        tmpStack = StackType()
        while tmp is not None:
            tmpStack.push(tmp.info)
            tmp = tmp.next
        while tmpStack.is_empty() is False:
            item = tmpStack.pop()
            if item is not None:
                self.push(item)
