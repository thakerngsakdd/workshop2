class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_address(self):
        return self.address

    def get_info(self):
        return {"name": self.name, "age": self.age}


name = "nopparat wongsa"
age = 21
address = "Bangkok noi"

Person = Person(name, age, address)

print(Person.get_name())
print(Person.get_age())
print(Person.get_address())
print(Person.info())