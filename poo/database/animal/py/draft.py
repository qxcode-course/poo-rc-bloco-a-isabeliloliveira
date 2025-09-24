class Animal:
    def __init__(self, species: str, age: int = 0, sound: str): # construtor
        self.species= species # atributos
        self.age: int = age
        self.sound = sound
        
    # def mostrar (species, age, sound)
    #     print("{species}:{age}:sound")
        

def main()
    animal: Animal = Animal("", "", "")
    
    while True:
        line: str = input()
        args: list[str]=line.split(" ")
        
        
        if args[0] == "new":
            species: str = args[1]
            age: int = args[2]
            sound: str = args[3]
            animal = Animal(species, age, sound)
        elif args[0] == "show":
            print(animal)
        elif args[0] =="end":
            break