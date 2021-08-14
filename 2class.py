class Character:
    character = 0

    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level
        Character.character += 1

class NPC(Character):

    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)
        # self.speak = speak
    def speak(self, statement):
        return "{} says: {}".format(self.name, statement)


# ------------test segment-------------
rabi = NPC("rabi", 100, 3)
print(Character.character)
print(rabi.speak("I fear the thunder!..."))
