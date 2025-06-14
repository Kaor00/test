class Gamer:
    __count = 0
    def __init__(self, name):
        self.name = name
        Gamer.__count += 1

    def print(self):
        print(f"Gamer: {self.name}")

    @staticmethod
    def amount():
        return Gamer.__count

gamer1 = Gamer(input("Enter your name: "))
gamer2 = Gamer(input("Enter your name: "))
print('Game beginner!' if Gamer.amount()==2 else "await second gamer...")

def first_step():
    print("Game started!")

print("+++++++++")
print("game over")

print("write from git bush")
