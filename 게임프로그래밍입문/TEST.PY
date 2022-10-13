# def new_str(str_in):
#     length = len(str_in)
#     for i in range(0, length):
#         yield str_in[i]
# for char in new_str("hello"):
#     print(char)
# list1 = [1, 3, 6, 10]
# gen = (x**2 for x in list1)
# print(gen)
# print(next(gen))
# print(next(gen))


#######################################
class Ex1 :
    def __init__(self):
        self.x = [11, 12, 13, 14, 15]
    def __iter__(self):
        for xx in self.x:
            yield xx
ex1 = Ex1()
for y1 in ex1:
    print(y1) # 11 12 13 14 15
x1 = iter(ex1)
print(next(x1)) # 11