
# 定义一个类
class Dog:
	# 构造方法
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def get_info(self):
		print(self.name.title() + " is " + str(self.age) + " years old.")

	def sit(self):
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		print(self.name.title() + " rolled over.")


class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer = 0
		self.gas = 0

	def get_des(self):
		des = str(self.year) + " " + self.make + " " + self.model
		return des.title()

	def update_odometer(self, mileage):
		if self.odometer <= mileage:
			self.odometer = mileage
		else:
			print("You can't roll back an odometer.")

	def get_odometer(self):
		print("This car has " + str(self.odometer) + " miles on it.")

	def fill_gas_tank(self):
		self.gas = 100
		print("Tank full.")


# 继承
class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		# 定义子类特有的方法
		self.battery_size = 88

	# 定义子类特有的方法
	def des_battery(self):
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

	# 重写父类方法
	def fill_gas_tank(self):
		print("This car doesn't need a gas tank.")







