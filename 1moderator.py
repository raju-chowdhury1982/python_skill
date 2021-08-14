# crating user class for tracking the user

class User:
    active_user = 0

    @classmethod
    def display_active_user(cls):
        return f"There are {cls.active_user} people active now."

    @classmethod
    def from_string(cls, data_str):
        first_name, last_name, _age, _like = data_str.split(",")
        return cls(first_name, last_name, int(_age), int(_like))

    @property
    def like(self):
        return self._like
    @like.setter
    def like(self, value):
        if value >0:
            self._like += value
        else:
            self._like

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 18:
            return self._age
        else:
            raise ValueError("Minors are not permitted.")


    def __init__(self, first_name, last_name, age, like):
        self.first_name = first_name
        self.last_name = last_name
        self._age = age
        self._like = like
        User.active_user += 1

    def logout(self):
        User.active_user -= 1
        return f"user:\"{self.first_name}\" log out now."
    def login(self):
        User.active_user += 1
        return f"user:\"{self.first_name}\" log in now."
    def full_name(self):
        return f"{self.first_name[0].upper() + self.first_name[1:]} {self.last_name[0].upper() + self.last_name[1:]}"

    def user_initial(self):
        return f"{self.first_name[0].upper()}.{self.last_name[0].upper()}."

    # ----------------moderators----------------
class Moderator(User):
    total_mod_user = 0
    @classmethod
    def active_mod_user(cls):
        return f"There are {cls.total_mod_user} moderator users now."

    def __init__(self, first_name, last_name, _age, _like, community):
        super().__init__(first_name, last_name, _age, _like)
        self.community = community
        Moderator.total_mod_user += 1

    def remove_post(self):
        return f"{self.full_name()} remove a post from {self.community}."

# --------------end of definition--------------
user1=User.from_string("raju,chowdhury,39,4")
user2=User.from_string("mita,bhowmik,33,104")
print(user1.full_name())
print(user1.user_initial())
print(user1.age)
print(user1.like)
print("User Name\t User Initial\t User Age\t User Like")
print(f"{user1.full_name()}\t {user1.user_initial()}\t\t {user1.age}\t\t {user1.like}")
print(f"{user2.full_name()}\t {user2.user_initial()}\t\t {user2.age}\t\t {user2.like}")
print(User.active_user)
print(user1.logout())
print(User.active_user)
kala = Moderator("kala", "bapi", 54, 5,"TMC")
print(kala.full_name())
print(kala.community)
print(kala.remove_post())
print(User.display_active_user())
print(user1.login())
print(User.display_active_user())
futo = Moderator("futo", "katik", 32, 10, "BJP")
print(Moderator.active_mod_user())
print(User.display_active_user())
