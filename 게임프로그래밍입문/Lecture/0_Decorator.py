from functools import wraps

def NewDecorator(func):
    def NewAdd(*args, **kwargs):
        # 데코레이터가 먼저 실행되기 때문에 before call가 먼저 출력됨
        print('Before call')
        # 이 때 add가 실행됨
        result = func(*args, **kwargs)
        # add 함수가 실행되고 나서 after call을 출력함
        print('After call')
        return result
    return NewAdd

# @NewDecorator 
# # 데코레이터 : 
# # @NewDecorator : add를 콜할때  @NewDecorator를 먼저 실행함.
# def add(a, b):
#     print('Add')
#     return a + b

# sum = add(1, 3)
# print(sum)
# print(add.__name__)


def add2(a, b):
    print('Add')
    return a + b

add3 = NewDecorator(add2)
print(add3(1, 3))