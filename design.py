# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name            # public attribute
        self._power = power         # protected attribute (single underscore)
        self.__city = city          # private attribute (double underscore)

    # Method to introduce the hero
    def introduce(self):
        return f"I am {self.name}, protector of {self.__city}!"

    # Method to use power
    def use_power(self):
        return f"{self.name} uses {self._power}!"

    # Getter for private attribute
    def get_city(self):
        return self.__city

    # Setter for private attribute
    def set_city(self, new_city):
        self.__city = new_city


# Derived class (Inheritance)
class FlyingHero(Superhero):
    def __init__(self, name, power, city, fly_speed):
        super().__init__(name, power, city)   # Call base class constructor
        self.fly_speed = fly_speed

    # Polymorphism: overriding method
    def use_power(self):
        return f"{self.name} soars at {self.fly_speed} km/h using {self._power}!"


# Another derived class
class TechHero(Superhero):
    def __init__(self, name, power, city, gadget):
        super().__init__(name, power, city)
        self.gadget = gadget

    # Polymorphism: overriding method
    def use_power(self):
        return f"{self.name} fights using {self.gadget} and {self._power}!"


# --- Testing the classes ---
hero1 = Superhero("ShadowKnight", "invisibility", "Gotham")
hero2 = FlyingHero("SkyHawk", "wind control", "Metropolis", 500)
hero3 = TechHero("IronMind", "super strength", "New York", "Laser Blaster")

print(hero1.introduce())
print(hero1.use_power())

print(hero2.introduce())
print(hero2.use_power())

print(hero3.introduce())
print(hero3.use_power())
