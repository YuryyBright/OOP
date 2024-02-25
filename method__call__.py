import math


class StripChars:
    """
    descriptoin method __call__
    """

    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError(' Need str')

        return args[0].strip(self.__chars)


#
# c = StripChars('/.?!;')
# res = c('Hello world !?')
# print(res)

class Derivate:
    """
    descriptoin method __call__
    """

    def __init__(self, func):
        self.__func = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__func(x + dx) - self.__func(x) / dx)


# def df_sin(x):
#     return math.sin(x)
#
# df_sin = Derivate(df_sin)

@Derivate
def df_sin(x):
    return math.sin(x)


print(df_sin(math.pi / 3))
