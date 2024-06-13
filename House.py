class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors


floor = House()

floor.setNewNumberOfFloors(6)

print(floor.numberOfFloors)
