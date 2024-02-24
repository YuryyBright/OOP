class Point:
    def __new__(cls, *args, **kwargs):
        print('call method __new__ for ' + str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print('call method __init__ for ' + str(self))
        self.x = x
        self.y = y


# point = Point(1, 2)
# print(point)


### Pattern Singleton


class DataBase:

    __instance = None

    def __new__(cls, *args, **kwargs):
        """
        call before created object of class
        :param args:
        :param kwargs:
        """
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def __del__(self):
        DataBase.__instanced = None

    def connect(self):
        print(f"Connect to db {self.user}@{self.psw}:{self.port}")

    def close(self):
        print(f"Close DB")

    def read(self):
        print(f"Read from DB")

    def write(self, data):
        print(f"Write to DB {data}")

db = DataBase('root', '1234', 443)
db1 = DataBase('root_1', '4321', 443)

print(id(db), id(db1))

db.connect()
db1.connect()