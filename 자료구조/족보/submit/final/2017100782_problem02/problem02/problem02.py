class ItemType:
    def __init__(self, name):
        
        self.name = name


class HashTable:
    def __init__(self):
        self.max_items = 10
        self.table = [None for _ in range(self.max_items)]
        self.num_items = 0

    def retrieve_item(self, item):
        hash_value = self.hash(item)

        return self.table[hash_value]

    def hash(self, item):
        
        sum = 0
        for char in item.name:
            sum += ord(char)
        
        return sum % self.max_items

    def insert_item(self, item):
        hash_value = self.hash(item)

        flag = False
        
        while flag is False and self.is_full() is False:
            if self.table[hash_value] is None:
                self.table[hash_value] = item  
                self.num_items += 1
                flag = True
            else:
                hash_value += 1
                hash_value %= self.max_items
    
    def delete_item(self, item):
        hash_value = self.hash(item)

        while hash_value < self.max_items:
            if self.table[hash_value] != None and self.table[hash_value].name == item.name:
                self.table[hash_value] = None
                self.num_items -= 1
                self.rehash()
                return
            hash_value += 1

    def rehash(self):
        new_table = [None for _ in range(self.max_items)]
        for i in range(self.max_items):
            if self.table[i] is None:
                continue
            hash_value = self.hash(self.table[i])
            flag = False

            while flag is False:
                if new_table[hash_value] is None:
                    new_table[hash_value] = self.table[i]
                    flag = True
                else:
                    hash_value += 1
                    hash_value %= self.max_items
        self.table = new_table

    def is_full(self):
        return self.num_items == self.max_items
    
    def is_empty(self):
        return self.num_items == 0

    def __str__(self):

        table = ""    
        for idx, item in enumerate(self.table):
            if item is not None:
                table += f"{idx} : {item.name}\n"
            else:
                table += f"{idx} : None\n"

        return table

if __name__ == "__main__":

    table = HashTable()

    a = ItemType("5") 
    b = ItemType("6") 
    c = ItemType("24")
    d = ItemType("2") 
    e = ItemType("1") 
    f = ItemType("67")
    g = ItemType("3") 
    h = ItemType("4") 

    table.insert_item(a)
    table.insert_item(b)
    table.insert_item(c)
    table.insert_item(d)
    table.insert_item(e)
    table.insert_item(f)
    table.insert_item(g)
    table.insert_item(h)

    print(table)

    print("Delete \"1\"")
    table.delete_item(ItemType("1"))
    print(table)

    print("Delete \"24\"")
    table.delete_item(ItemType("24"))

    print(table)
