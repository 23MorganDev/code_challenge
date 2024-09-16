class Person:
    def __init__(self, name, age, gender):

        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("My name is: ", self.name, "am of: ", self.age, "and am a: ", self.gender )

p1 = Person('Tony Stark', 51, 'Male')
p1.introduce()