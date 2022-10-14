
class Singleton(object):
    _object = None

    def __new__(cls):
        if cls._object is None:
            self = cls._object = super(Singleton, cls).__new__(cls)
            # setattr(self, '__pool', [])
            # setattr(self, '__worker', [])
            self.__name = []
            self.__price = []
        
        return cls._object


if __name__ == '__main__':
    c = Singleton()
    d = Singleton()
    print(id(c))
    print(id(d))
    print(dir(c))
