
class Demo:
    a = 20

    def __init__(self, b):
        self.b = b

    def access_b(self):
        return self.b

    def change_b(self, new):          ## object method: The method which helps to access and modeify the obejct member
        self.b = new

    @classmethod
    def access_a(cls):
        return cls.a

    @classmethod                        ## class method: the metod which helps to access and modify the class members
    def change_a(cls, new):
        cls.a = new

    @staticmethod
    def Info():
        print('we are using Demo class')

d = Demo(30)
# print(d.b)
print(d.access_b())
# d.b = 40
d.change_b(50)
print(d.access_b())
# print(Demo.a)
# Demo.a = 90
Demo.change_a(80)
print(Demo.access_a())

d.Info()
Demo.Info()

















