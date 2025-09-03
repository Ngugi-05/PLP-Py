class Animals:
    def talk(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animals):
    def talk(self):
        return "Woof!"


class Cat(Animals):
    def talk(self):
        return "Meow!"


class Cow(Animals):
    def talk(self):
        return "Moo!"


class Whale(Animals):
    def talk(self):
        return "Whistle!"


for animal in (Dog(), Cat(), Cow(), Whale()):
    print(f"{animal.__class__.__name__}: {animal.talk()}")
