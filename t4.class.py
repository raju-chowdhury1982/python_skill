class Chicken:
    allowed_species = ["Partridge Silkie", "Speckled Sussex"]
    total_eggs = 0

    def __init__(self, name, species, eggs=0):
        if species not in Chicken.allowed_species:
            raise ValueError(f"This {species} type egg not eatable! ")
        self.name = name
        self.species = species
        self.eggs = eggs
        Chicken.total_eggs += eggs

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs

print(Chicken.total_eggs)
print("-----")
c1 = Chicken("hui", "Partridge Silkie")
c2 = Chicken("wui", "Speckled Sussex")
c2.lay_egg()
print(Chicken.total_eggs)
c2.lay_egg()
print(Chicken.total_eggs)
c1.lay_egg()
print(Chicken.total_eggs)
