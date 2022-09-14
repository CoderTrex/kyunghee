class NodeType:
    """ Node Type """
    def __init__(self, item):
        self.info = item
        self.next = None
        self.back = None

class DoublyLL:
    def __init__(self):
        self.head = NodeType('head')
    
    def find_item(self, item):
        tmp = self.head
        while tmp is not None:
            if tmp.info is item:
                return tmp
            tmp = tmp.next
        return
    
    def insert_item(self, item, new):
        found = self.find_item(item)
        new = NodeType(new)
        if found is not None:
            if found.next is not None:
                next = found.next
                found.next = new.back
                new.back = found
                new.next = next
                next.back = new
            else:
                found.next = new
                new.back = found

    def delete_item(self, item):
        found = self.find_item(item)
        if found is None:
            return
        target = found
        if found.next is not None and found.back is not None:
            found.next.back = found.back
            found.back.next = found.next
        elif found.next is not None:
            found.next.back = None
            self.head = found
        elif found.back is not None:
            found.back.next = None
        del target
            
    def __str__(self):
        cur_node = self.head
        items = []
        while cur_node is not None:
            items.append("(" + str(cur_node.info) + ")\n")
            cur_node = cur_node.next
        return "".join(items)

