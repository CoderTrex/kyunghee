class NodeType:
    """ Node Type """

    def __init__(self, item):
        self.info = item
        self.next = None


class UnsortedType:
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
            if item == location.info:
                found = True
            else:
                location = location.next
                moreToSearch = location != None
        return found

    def insert_item(self, item):
        new_node = NodeType(item)
        new_node.next = self.listData
        self.listData = new_node
        self.length += 1

    def delete_item(self, item):
        if item == self.listData.info:
            target = self.listData
            self.listData = self.listData.next
        else:
            loc = self.listData
            while item != loc.next.info:
                loc = loc.next
            target = loc.next
            loc.next = loc.next.next
        self.length -= 1
        del target

    def reset_list(self):
        self.currentPos = None

    def get_next_item(self):
        if self.currentPos == None:
            self.currentPos = self.listData
        else:
            self.currentPos = self.currentPos.next
        return self.currentPos.info

    def __str__(self):
        self.reset_list()
        items = []
        for i in range(0, self.length):
            t = self.get_next_item()
            items.append(str(t))
        return " ".join(items)
