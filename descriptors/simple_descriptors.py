class Person(object):

    @property
    def name(self):
        print("Called the getter method")
        return self._name

    @name.setter
    def name(self, v):
        self._name = v
        print(f"Value set to {self._name}")

    @name.deleter
    def name(self):
        print(f"Deleting...{self._name}")
        del self._name


p = Person()

p.name = 'JayD'
print(f"Getting name : {p.name}")

print("Attempting to del a property...")
del p.name