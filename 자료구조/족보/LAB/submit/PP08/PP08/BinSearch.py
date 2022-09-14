def binary_search(info, item, fromLocation, toLocation):
    if fromLocation > toLocation:
        return False
    else:
        midPoint = int((fromLocation + toLocation) / 2)
        if item < info[midPoint]:
            return binary_search(info, item, fromLocation, midPoint-1)
        elif item == info[midPoint]:
            return True
        else:
            return binary_search(info, item, midPoint+1, toLocation)
