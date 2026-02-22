class Player:
    def __init__(self, name: str, age: int, height: int, weight: int) -> None:
        self.name: str = name
        self.age: int = age
        self.height: int = height
        self.weight: int = weight

    def get_age(self) -> str:
        return f"{self.name} is age {self.age}"

    def get_height(self) -> str:
        return f"{self.name} is {self.height}cm"

    def get_weight(self) -> str:
        return f"{self.name} is {self.weight}kg"

p1 = Player("David Jones", 25, 175, 75)

print(p1.get_age())
print(p1.get_height())
print(p1.get_weight())