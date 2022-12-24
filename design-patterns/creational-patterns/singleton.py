'''
The Singleton pattern is used to ensure that a class has only one instance
and provides a global access point to that instance. In this example, the Singleton
class has a private class attribute __instance that is used to store the instance of
the class. The __init__ method checks if an instance has already been created, and if
not, it creates one. The getInstance method is a class method that returns the instance
of the class.
'''
class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called.")
        else:
            print("Instance already created.", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

s1 = Singleton()
print("Object created.", Singleton.getInstance())
s2 = Singleton()
