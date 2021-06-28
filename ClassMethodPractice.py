from typing import ClassVar


class Myclass:
    ClassVar=0
    def __init__(self, initValue):
        print("MyClass 생성자가 호출되었습니다.")
        self.r=initValue
    def foo(): #객체없이 사용가능
        print("MyClass에 오신 것을 환영합니다.")
    
    def foo1(self):
        print("MyClass 객체를 이용해야만 호출됩니다.")
    def printClass(self,mesg):
        print("%s : r = %d"%(mesg,self.r))

#객체를 하나 생성함.
a = Myclass(10)

#클래스 함수를 호출.
Myclass.foo()

#객체 메소드를 호출.
a.foo1()
Myclass.foo1(a)

a.printClass("멤버변수 출력")

#클래스 변수 출력
b=Myclass(20)
print(a.ClassVar)
print(b.ClassVar)
#a 클래스의 변수만 변경
a.ClassVar = 10
print(a.ClassVar)
print(b.ClassVar)
#클래스 변수를 변경 , 멤버 변수가 우선시 됨(복습)
Myclass.ClassVar = 30
print(a.ClassVar)
print(b.ClassVar)