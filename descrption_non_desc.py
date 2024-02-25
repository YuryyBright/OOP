"""
Слід зазначтити що пріортет доступу до дескрипотор даних має найвищий


"""
class NonDataDescript:
    def __set_name__(self, owner, name):
        self.name = '_x'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
class CustomDescriptor:
    """
    crete interface to work with class POINT to avoid duplication next construction:
    @classmethod
    def verify_var(cls, var):
        if type(var) != int:
            raise TypeError

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, var):
        self.verify_var(var)
        self._x = var

    """

    @classmethod
    def verify_var(cls, var):
        if type(var) != int:
            raise TypeError
    def __set_name__(self, owner, name):
        self.name = '_'+name

    def __get__(self, instance, owner):
        return getattr(instance,self.name)
    def __set__(self, instance, val):
        self.verify_var(val)
        setattr(instance,self.name, val)
        print(f'__set__: {self.name} = {val}')


class Point:
    x = CustomDescriptor()
    y = CustomDescriptor()
    z = CustomDescriptor()
    xr = NonDataDescript
    def __init__(self, x=0, y=0, z=0):
        # print('call method __init__ for ' + str(self))
        self.x = x
        self.y = y
        self.z = z

    # @classmethod
    # def verify_var(cls, var):
    #     if type(var) != int:
    #         raise TypeError

    # @property
    # def x(self):
    #     return self._x
    #
    # @x.setter
    #
    #     self.verify_var(var)
    #     self._x = var
p1 = Point(1,2,3)
print(p1.__dict__)