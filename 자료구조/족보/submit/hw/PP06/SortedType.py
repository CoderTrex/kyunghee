import time


class NodeType:
    """ Node Type """

    def __init__(self, item):
        self.info = item
        self.next = None

    def __str__(self):
        return str(self.info)


class SortedType:
    def __init__(self):
        self.listData = None
        self.length = 0
        self.currentPos = None

    def is_full(self):
        try:
            location = NodeType("test")
            return False
        except:
            return True

    def length_is(self):
        return self.length

    def make_empty(self):
        while self.listData != None:
            tempPtr = self.listData.next
            del self.listData
            self.listData = tempPtr
        self.length = 0

    def retrieve_item(self, item):
        location = self.listData
        found = False
        moreToSearch = location != None

        while moreToSearch and not found:
            if location.info < item:
                location = location.next
                moreToSearch = location != None
            elif location.info == item:
                found = True
            else:
                moreToSearch = False

        return found

    @staticmethod
    def __find_mid(left, right):
        slow = left
        fast = left.next
        while fast is not right and fast is not None:
            fast = fast.next
            if fast is not right:
                slow = slow.next
                fast = fast.next
        return slow

    def __find_before(self, item):
        left = self.listData
        right = None
        while right != left or right is not None:
            mid = self.__find_mid(left, right)
            if mid.info < item:
                left = mid
                if mid.next is None or mid.next.info > item:
                    break
                left = mid.next
            elif mid.info > item:
                right = mid
            else:
                break
        return left

    def insert_item(self, item):
        new_item = NodeType(item)
        if self.listData is None:
            self.listData = new_item
        elif item < self.listData.info:
            new_item.next = self.listData
            self.listData = new_item
        else:
            target = self.__find_before(item)
            if target is None:
                self.listData = new_item
            else:
                new_item.next = target.next
                target.next = new_item
        self.length += 1

    def delete_item(self, item):
        bef_target = self.__find_before(item - 1)
        target = bef_target.next
        if target is not None and target.info is item:
            bef_target.next = target.next
            del target
            self.length -= 1

    def reset_list(self):
        self.currentPos = None

    def get_next_item(self):
        if self.currentPos == None:
            self.currentPos = self.listData
        item = self.currentPos.info
        self.currentPos = self.currentPos.next

        return item

    def __str__(self):
        self.reset_list()
        items = []
        for i in range(0, self.length):
            t = self.get_next_item()
            items.append(str(t))
        return " ".join(items)
