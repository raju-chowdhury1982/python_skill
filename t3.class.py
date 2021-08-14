# creating permissible pieces of def():

class Pet:

    allowed_species = ["cat", "dog", "bird", "fish", "rat"]

    def __init__(self, name, species,color="white" ):
        if species not in Pet.allowed_species:
            raise ValueError(f"You can not have {species} as pet!")
        self.name = name
        self.color = color
        self.species = species



pet1 = Pet("lila", "cat","gray")
pet2 = Pet("Moti","dog", "black")
pet3 = Pet("tuni", "bird","green")
pet4 = Pet("moli", "fish", "red" )
#pet4 = Pet("sheru", "tiger", "yellow")


print(pet4.species)
