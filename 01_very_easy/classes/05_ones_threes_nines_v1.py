class ones_threes_nines:
    def __init__(self, value:int) -> None:
        self.value = value

        self.nines : int = 1
        self.threes : int = 1
        self.ones : int = 1

        while True:
            if (self.value - (9 * self.nines)) >= 0:
                self.nines += 1
            else:
                self.nines -= 1
                break
            
        while True:
            if (self.value - (3 * self.threes)) >= 0:
                self.threes += 1
            else:
                self.threes -= 1
                break

        while True:
            if (self.value - (1 * self.ones)) >= 0:
                self.ones += 1
            else:
                self.ones -= 1
                break

n1 = ones_threes_nines(5)
print(n1.nines)
print(n1.ones)
print(n1.threes)