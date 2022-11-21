# 파이썬 파일 임포트 해서 사용할 때 폴더의 하위 파일 사용할때 .을 이용해서 구분함.

# from package import *
# 패키지 폴더 안의 모든 것을 임포트한다.

# ◈classmethod
# ◈staticmethod

# class A:
    # data = 10
    # @classmethod
    # def fn1(cls , i ,j):
        # print('A class', cls.data + i + j)
    # @staticmethod
    # def fn2(i , j):
        # print('A class', i + j)

# A.fn1(1, 2)
# A.fn2(1, 2)


# ◈Instance attributes
# [Default]: dynamic creation, Dict , wastes RAM, [__slots__]:
    # fixed
            # --> 이러한 동적 생성과 dict 형태의 생성은 메모리를 많이 사용하게 됨

# class A(object):
# def __init__(self, x, y)
    # # self.x = xself.y = y
# class B(object):
    # __slots__ = ['x', 'y']
    # def init __(self, x, y)
        # self.x
        # self.y -> 슬롯으로 저장이되어 메모리의 공간이 덜 활용됨
# # = xself.y = y
# class C(object):
    # __slots__ = ['x', 'y', '__dict__'] -> x와 y는 고정하고 나머지는 딕셔너리
    # def init __(self, x, y)
        # # self.x = xself.y = y

# ----------------------------------------------------------------------------------------------------#

# staticmethod
# - 부모 클래스에서 정의된 staticmethod는 자식 클래스에서 call할 수 있음
# - 클래스 변수에 접근 가능
# - 생성자 포함 인스턴스 매소드 변수에는 접근 불가능


# class Parent:
#     class_val = 'calss variable'
    
#     def __init__(self) -> None:
#         self.name = 'eunseong'
#         self.age = 21

#     @staticmethod
#     def check_name(name):
#         return name


# class Child(Parent):
#     pass

# child = Child()
# print(child.check_name("check name")) 
# -> 출력값 check name


class Parent:
    class_val = 'calss variable'
    
    def __init__(self) -> None:
        self.name = 'eunseong'
        self.age = 21

    @staticmethod
    def check_name(name):
        return name


class Child(Parent):
    pass

parent = Parent()
print(parent.check_name("check name"))
# -> 출력값 check name

