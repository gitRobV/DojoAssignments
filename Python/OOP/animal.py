class Animal(object):
    """docstring for Animal."""
    def __init__(self, name, health=160):
        self.name = name
        self.health = health

    def walk(self):
        self.health = self.health - 1
        return self

    def run(self):
        self.health = self.health - 5
        return self

    def display_health(self):
        print "Current Health: " + str(self.health)
        return self


class Dog(Animal):
    """docstring for Dragon."""
    def __init__(self):
        self.health = 150

    def pet(self):
        self.health = self.health + 5
        return self

class Dragon(Animal):
    """docstring for Dragon."""
    def __init__(self):
        self.health = 170

    def fly(self):
        self.health = self.health - 10
        return self

    def display_health(self):
        super(Dragon, self).display_health
        print "I am a Dragon"
        return self


roxy = Dragon()

roxy.walk().run().fly().fly().walk().display_health()
