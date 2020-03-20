
import datetime
import random


class Animal:


	"""This class reprensent one animal with its attributes.

    Attributes:
        my_type (str) : race of the animal
		my_sex (str) : sex of the animal i.e. "Male" or "Female"
		my_birthdate (datetime) : birth date of the animal
	"""

	def __init__(self, my_type, my_sex, my_birthdate=None):

		"""Instanciation of the class

		Arguments:
			my_type (str)
			my_sex (str)
			my_birthdate (datetime) : optionnal

		If the optionnal argument my_birthdate is not provided, the birthdate of the animal is initialised
		at the current time (the animal was just born).
		"""

		self.my_type = my_type
		self.my_sex = my_sex
		self.my_birthdate = my_birthdate

		if my_birthdate == None :
			global current_farms_date
			self.my_birthdate = current_farms_date


	def __str__(self):

		"""Return the attributes of the animal as a string
		"""

		return "Animal : " + str(self.my_type) + " " + str(self.my_sex) + " " + str(self.my_birthdate)


	def want_reproduce(self):

		"""Return True if the animal is ready to reproduce, else return False.
		"""

		global future_farms_date

		if (self.my_sex == "Female") and ((future_farms_date - self.my_birthdate).days > 365) and ((future_farms_date - self.my_birthdate).days % 365 < 30):

			return True

		else : 
			return False



class Farm:

	"""This class reprensent a farm with its attributes.

    Attributes:
        farm_name (str)
		animal_list (list)
		current_date (datetime)
	"""

	def __init__(self, farm_name=None):

		"""Instanciation of the class

		Arguments:
			farm_name (str) : optionnal
		"""

		self.farm_name = farm_name
		self.animal_list = []
		self.current_date = datetime.datetime.now()


	def __str__(self):

		"""Return the list of animals as a string.
		"""

		return_string = "Farm : " + str(self.farm_name) + "\n"

		for current_animal in self.animal_list:
			
			return_string += current_animal.__str__() + "\n"

		return return_string


	def add_animal(self, my_type, my_sex, my_age=None):

		"""Add one animal to the farm.
		"""

		self.animal_list.append(Animal(my_type, my_sex, my_age))
		print("\t\t=>Farm.add_animal(" + str(my_type) + ", " + str(my_sex) + ", " + str(my_age) + ")")



	def pass_time(self, time_delta_to_advance):
		
		"""Advance time of the farm by time_delta_to_advance.
		Handle reproduction and retirement of animals.
		"""

		global future_farms_date

		for current_animal in self.animal_list:

	
			if(current_animal.want_reproduce() == True):

				print("\t\tAnimal " + str(current_animal.my_type) + "  wants to reproduce (" + str(current_animal.my_sex) 
						+ " " + str((future_farms_date - current_animal.my_birthdate).days) + " days)")

				# We look for a male in the farm
				
				for searched_animal in self.animal_list:
					if (searched_animal.my_type == current_animal.my_type) and (searched_animal.my_sex == "Male") :

						print("\t\tPerfect match ! A baby was born !")

						self.add_animal(current_animal.my_type, random.choice(["Male", "Female"]), my_age=None)
						
						break


			if((future_farms_date - current_animal.my_birthdate).days > 3*365):
				self.animal_list.remove(current_animal)
				print("\t\tGoodby animal !!")



if __name__ == "__main__":

	# Initialize a variable that coutain current date
	global current_farms_date
	current_farms_date = datetime.datetime.now()
	print("We are the : " + str(current_farms_date) + "\n")

	# Create two farms
	farm_list = []
	farm_list.append(Farm("My first farm"))
	farm_list.append(Farm("Another farm"))

	# Populate the two farms with animals
	farm_list[0].animal_list.append(Animal("cow", "Male"))
	farm_list[0].animal_list.append(Animal("sheet", "Male"))
	farm_list[0].animal_list.append(Animal("sheep", "Female"))
	farm_list[0].animal_list.append(Animal("cow", "Female"))
	farm_list[1].animal_list.append(Animal("cow", "Male"))
	farm_list[1].animal_list.append(Animal("sheet", "Male"))
	farm_list[1].animal_list.append(Animal("sheep", "Female"))
	farm_list[1].animal_list.append(Animal("cow", "Female"))

	farm_list[0].add_animal("cow", "Female", datetime.datetime(year=2019, month = 5, day = 3))



	# We print the list of farms (and animals)
	for current_farm in farm_list:
		print(current_farm)


	# We start travelling to the future
	print("\nWe start the time...:\n")

	time_iteration = 0

	while time_iteration < 100:

		# Advance time of 28 days = 4 weeks
		global future_farms_date
		future_farms_date = current_farms_date + datetime.timedelta(days = 28)

		print("\n\tAdvancing to : " + str(future_farms_date))

		time_iteration += 1

		for current_farm in farm_list:
			current_farm.pass_time(datetime.timedelta(weeks = 4))


		current_farms_date = future_farms_date



	# We print the list of farms (and animals)
	for current_farm in farm_list:
		print(current_farm)



