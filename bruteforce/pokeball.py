class Pokeball():
    max = 0

    def __init__(self, name, power):         
        self.name = name
        self.basePower = power

    def __repr__(self):
        return self.pokemon.name
    
    def catch(self, pokemon):
        