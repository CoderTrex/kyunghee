MAX_ITEMS = 50


class StackType:
    def __init__(self):
        self._top = -1
        self.items = [None] * MAX_ITEMS

    def is_empty(self):
        return self._top == -1

    def is_full(self):
        return self._top == MAX_ITEMS - 1

    def push(self, item):
        if self.is_full():
            print("Stack is Full")
        else:
            self._top += 1
            self.items[self._top] = item

    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            self._top -= 1

    def top(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            return self.items[self._top]
