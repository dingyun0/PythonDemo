# 基类，抽象类
class Animal:
    def __init__(self,name):
        self._name=name
    def speak(self):
        raise NotImplementedError("子类必须实现speak方法")
    # @property 是 Python 提供的一个内置装饰器，用于将一个方法变成只读属性。
# 它的作用是让你可以像访问属性一样调用方法，而不需要显式加括号。
    @property
    def name(self):
        return self._name
# 派生类
class Dog(Animal):
    def speak(self):
        return f"{self.name} 说: 汪汪!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} 说: 喵喵!"
def main():
        # 创建对象
    dog = Dog("旺财")
    cat = Cat("咪咪")
    animals=[dog,cat]
    for animal in animals:
        print(animal.name,animal.speak())

if __name__=='__main__':
    main()