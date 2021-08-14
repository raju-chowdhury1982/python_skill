# example of inheritance

class Human:

    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    # def get_age(self):
    #     return self._age
    #
    #
    # def set_age(self, new_age):
    #     if new_age >= 0:
    #         self._age = new_age
    #     else:
    #         self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age can't be negetive.")

    @property
    def fullname(self):
        return f"{self.fname[0].upper() + self.fname[1:]} {self.lname[0].upper()+self.lname[1:]}"

    @fullname.setter
    def fullname(self, name):
        self.fname, self.lname = name.split(" ")
        # return f"{self.fname} {self.lname}"




adi = Human("aditya", "singh", 14)
# print(adi.age)
# print("before set")
# adi.age = -8
# print(adi.get_age())
# adi.set_age(16)
# print(adi.get_age())

print(adi.age)
print("before set age")
adi.age = 16
print(adi.age)
print(adi.fullname)
print("before fullname set")
adi.fullname = "Adhiraj Saha"
print(adi.__dict__)
