from enum import Enum

MAX_ITEMS = 100


class ListFullError(Exception):
    def __str__(self):
        return "info is already full, try to delete item first"


class Compare(Enum):
    LESS = 0
    GREATER = 1
    EQUAL = 2


class ItemType:
    """ Item Type """

    def __init__(self, val):
        self.__val = val

    def compared_to(self, other_item):
        if self.__val < other_item.__val:
            return Compare.LESS
        elif self.__val > other_item.__val:
            return Compare.GREATER
        else:
            return Compare.EQUAL

    def __str__(self):
        return str(self.__val)


class SortedType:
    """ Chapter 3: Sorted List """

    def __init__(self):
        self.__info = [None] * MAX_ITEMS
        self.__length = 0
        self.__current_pos = -1

    def make_empty(self):
        self.__length = 0

    def length_is(self):
        return self.__length

    def is_full(self):
        if self.__length == MAX_ITEMS:
            return True
        return False

    def insert_item(self, item):
        if self.is_full():
            raise ListFullError
        for i in range(self.__length):
            res = self.__info[i].compared_to(item)
            if res is Compare.GREATER or res is Compare.EQUAL:
                for j in reversed(range(i, self.__length)):
                    self.__info[j + 1] = self.__info[j]
                self.__info[i] = item
                self.__length += 1
                return
        self.__info[self.__length] = item
        self.__length += 1

    def retrieve_item(self, item):  # Binary Search
        left = 0
        right = self.__length - 1

        while left < right:
            mid = (left + right) // 2
            res = item.compared_to(self.__info[mid])
            if res is Compare.EQUAL:
                return True
            elif res is Compare.GREATER:
                left = mid + 1
            else:
                right = mid - 1
        if left is right and item.compared_to(self.__info[left]) is Compare.EQUAL:
            return True
        else:
            return False

    def delete_item(self, item):
        for i in range(self.__length):
            if item.compared_to(self.__info[i]) is Compare.EQUAL:
                for j in range(i + 1, self.__length):
                    self.__info[j - 1] = self.__info[j]
                break
        self.__length -= 1

    def reset_list(self):
        self.__current_pos = -1

    def get_next_item(self):
        self.__current_pos += 1
        return self.__info[self.__current_pos]

    def __str__(self):
        ret = ""
        for i in range(self.__length):
            ret += str(self.__info[i])
            if i is not self.__length - 1:
                ret += " "
        return ret
