class Car:


    def __init__(self,brand):
        self.brand = brand

    def start(self):
        print(f"my car is {self.brand} and it is starting")

car_name=Car("BMW")
car_name = Car("Toyota")
   
print("BRAND:", {car_name.brand})

car_name.start()
        