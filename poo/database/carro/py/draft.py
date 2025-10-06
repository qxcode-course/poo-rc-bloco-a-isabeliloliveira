class Carro:
    def __init__(self, passag: int):
        self.passag: int = passag
        self.passMax: int = 2
        self.gasMax: int = 100
        self.gas: int = 0
        self.km: int = 0
    
    def __str__(self) -> str:
        return f"pass: {self.passag}, gas: {self.gas}, km {self.km}"
    
    
    def enter (self):
        if self.passag >= self.passMax:
            print("fail: limite de pessoas atingido")
        else:
            self.passag+=1
    
    
    
    
    
    
    
    
    
def main():
    carro = Carro(0)
    while True:
        line: str = input()
        print(f"$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "show":
            print(carro)

        elif args[0] == "enter":
            carro.enter()

        elif args[0] == "leave":
            carro.leave()
        elif args[0] == "end":
            break

        elif args[0] == "fuel":
            increment = int(args[1])
            carro.fuel(increment)

        elif args[0] == "drive":
            increment = int(args[1])
            carro.drive(increment)
            
main()