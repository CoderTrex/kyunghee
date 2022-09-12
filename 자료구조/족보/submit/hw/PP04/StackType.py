MAX_ITEMS = 100


class StackType:
    def __init__(self):
        self.info = []

    def is_empty(self):
        if len(self.info) == 0:
            return True
        return False

    def is_full(self):
        if len(self.info) == MAX_ITEMS:
            return True
        return False

    def push(self, item):
        if self.is_full() is False:
            self.info.append(item)

    def pop(self):
        if self.is_empty() is False:
            val = self.info.pop()
            return val

    def top(self):
        if self.is_empty() is False:
            return self.info[-1]
        return 'Stack is Empty'
