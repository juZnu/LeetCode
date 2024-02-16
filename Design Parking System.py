class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.space = {
            1: big,
            2: medium,
            3:small
        }

    def addCar(self, carType):
        if self.space[carType]:
            self.space[carType] -= 1
            return True 
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)