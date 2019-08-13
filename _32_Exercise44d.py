class Other(object):
    def override(self):
        print("other override")

    def implicit(self):
        print("other implicit")

    def alttered(self):
        print("other altered")

class Child(object):
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("child override")

    def altered(self):
        print("Child before altered")
        self.other.alttered()
        print("child after altered")

son = Child()

son.implicit()
son.override()
son.altered()