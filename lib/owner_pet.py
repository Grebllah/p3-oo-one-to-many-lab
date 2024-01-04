class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    def __init__(self, name, pet_type, owner = ""):
        self.name = name
        if pet_type in self.PET_TYPES:
            self.pet_type = pet_type
        else: raise Exception
        self.owner = owner
        Pet.all.append(self)
    pass

class Owner:
    def __init__(self, name):
        self.name = name
    def pets(self):
        pets = [pet for pet in Pet.all if pet.owner == self]
        return pets
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else: raise Exception
    def get_sorted_pets(self):
        pets = [pet for pet in Pet.all if pet.owner == self]
        def get_name(pet):
            return pet.name
        return sorted(pets, key=get_name)