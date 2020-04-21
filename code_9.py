from code_9_class import *

snip = Dog("Snip", 12)
snip.get_info()
snip.sit()
snip.roll_over()

willie = Dog("Willie", 8)
willie.get_info()
willie.sit()
willie.roll_over()


new_car = Car("audi", "a4", 2020)
print(new_car.get_des())
new_car.update_odometer(288)
new_car.get_odometer()
new_car.update_odometer(188)


tesla = ElectricCar("tesla", "model s", 2019)
print(tesla.get_des())
tesla.des_battery()
tesla.fill_gas_tank()