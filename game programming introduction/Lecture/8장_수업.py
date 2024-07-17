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


# ------------------------------------------------
# class Parent:
#     class_val = 'calss variable'
    
#     def __init__(self) -> None:
#         self.name = 'eunseong'
#         self.age = 21

#     @staticmethod
#     def check_name(name):
#         print(Parent.class_val)
#         return name


# class Child(Parent):
#     pass

# child = Child()
# print(child.check_name("check name")) 
# # -> 출력값 check name


# ------------------------------------------------
# 인스턴스 메소드는 접근이 불가능하다.
# class Parent:
#     class_val = 'calss variable'
    
#     def __init__(self) -> None:
#         self.name = 'eunseong'
#         self.age = 21

#     @staticmethod
#     def check_name(name):
#         print(Parent.class_val)
#         # print(self.name) <- 이 인스턴스는 접근이 불가능하다.
#         return name


# class Child(Parent):
#     pass

# parent = Parent()
# print(parent.check_name("check name"))
# -> 출력값 check name



# ------------------------------------------------
# classmethod
# - 부모 클래스에서 정의된 클래스 변수와 클래스 메소드는 자식 클래스에서도 선언이 가능함.
# - 클래스 변수에 접근이 가능
# - 생성자 함수 포함 인스턴스 메소드 변수에 접근이 불가능


# class Parent:
#     class_val = 'class variable'
    
#     def __init__(self):
#         self.name = 'eunseong'
#         self.age = 21
    
#     @classmethod
#     def change_class_val(cls, other_va):
#         cls.class_val = other_va
#         return cls.class_val
    
# class Child(Parent):
#     print(Parent.class_val)
#     pass

# 부모 클래스에서 호출 가능
# parent = Parent()
# print(parent.change_class_val('other class variable'))

# 자식 클래스에서 호출 가능
# child = Child()
# print(child.change_class_val('other class variable'))

# ------------------------------------------------

# class Parent:
#     class_val = 'class variable'
    
#     def __init__(self):
#         self.name = 'eunseong'
#         self.age = 21
    
#     @classmethod
#     def change_class_val(cls, other_val)
#         cls.class_val = other_val
#         print(cls.class_val)
#         # print(self.name) <- 인스턴스 값은 접근 못한다.
#         return cls.class_val
    
# class Child(Parent):
#     pass

# parent = Parent()
# print(parent.change_class_val('other class variable'))



# ------------------------------------------------
# staticmethod VS classmethod

# class Parent:
#     name = 'eunseong'
    
#     @staticmethod
#     def change_name(new_name):
#         Parent.name= new_name
    
# class Child(Parent):
#     pass

# parent = Parent()
# child = Child()

# parent.change_name('Heungmin Son')
# print("부모 클래스에서 선언할 때: \n", parent.name, child.name)
# print("-"*50)
# child.change_name("Jisung Park")
# print("자식 클래스에서 선언할 때: \n", parent.name, child.name)

# 결과
# 부모 클래스에서 선언할 때: 
#  Heungmin Son Heungmin Son
# --------------------------------------------------
# 자식 클래스에서 선언할 때: 
#  Jisung Park Jisung Park



# class Parent:
#     name = 'eunseong'
    
#     @classmethod
#     def change_name(cls, new_name):
#         cls.name = new_name

# class Child(Parent):
#     pass

# parent = Parent()
# child = Child()

# parent.change_name('Heungmin Son')
# print("부모 클래스에서 선언할 때: \n", parent.name, child.name)
# print("-"*50)
# child.change_name("Jisung Park")
# print("자식 클래스에서 선언할 때: \n", parent.name, child.name)

# 결과
# 부모 클래스에서 선언할 때: 
#  Heungmin Son Heungmin Son
# --------------------------------------------------
# 자식 클래스에서 선언할 때: 
#  Heungmin Son Jisung Park