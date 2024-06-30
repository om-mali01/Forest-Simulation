class Tree:
    def __init__(self, age: int=0, alive: bool=True) -> None:
        self.age = age
        self.alive = alive

    def grow(self) -> None:
        self.age += 1
        if self.age > 10:
            self.alive = False