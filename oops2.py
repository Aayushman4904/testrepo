class Car :
    wheels = 4
    sidemirror = 2
    drive = "backwheel"
    doors = 2

    def __init__(self,type) :
        Car.type = type


class ToyotaCar(Car) :
    brand = "Toyota"
    cof = "Japan"


class Supra(ToyotaCar) :
    color = "Milkan Blast"
    def __init__(self,type) :
        super().__init__(type)

c1 = Supra("Petrol")
print(Car.type)    