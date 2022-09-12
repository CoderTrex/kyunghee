class NodeType:
    """ Node Type """
    def __init__(self, item):
        self.info = item
        self.next = None

class CircularLL:
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

    def find_item(self, listData, item):
        loc = listData
        for _ in range(self.length):
            if loc.info == item:
                return loc
            loc = loc.next
        return

    
    def insert_item(self, item):
        new_item = NodeType(item)
        if self.listData is None:
            self.listData = new_item
            new_item.next = new_item
            self.length = 1
            return
        loc = self.listData
        for _ in range(self.length - 1):
            loc = loc.next
        if self.is_full() is False:
            loc.next = new_item
            new_item.next = self.listData
            self.length += 1


    def delete_item(self, item):
        tmp = self.listData
        for _ in range(self.length):
            if tmp.next.info == item:
                break
            tmp = tmp.next
        target = tmp.next
        if target == self.listData:
            self.listData = target.next
        tmp.next = tmp.next.next
        del target
        self.length -= 1
   

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
