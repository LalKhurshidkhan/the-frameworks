# class person():
#     name = "khan"
#     age = 23
#     occpation = "DS"

#     def info():
#         print(f"Name: {name}")

# a.person()
# a.info()


class Person:
    def __init__(self, name="khan", age=23, occupation="DS"):
        self.name = name
        self.age = age
        self.occupation = occupation

    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Occupation: {self.occupation}")

a = Person()
a.info()
