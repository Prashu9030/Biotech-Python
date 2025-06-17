class base:
    def __init__(self):
        self.__a=32
        print(self.__a)

class derived(base):
    def __init__(self):
        base()._init_(self)
        print(self.__a+2)

class derived(derived):
    def __init__(self):
        derived().__init__(self)
        print(self._a+3)

a1=derived()