class Car:
    def __init__(self, userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel
        
    def full_name(self):
        return f"{self.brand} {self.model}"

my_car = Car("Toyota", "Corolla")

print(my_car.full_name())