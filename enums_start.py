# define enumerations using the Enum base class
from enum import Enum, unique, auto

@unique
class Fruit(Enum):
	Apple = 1
	Banana = 2
	Orange = 3
	Tomato = 4
	PEAR = auto()
	
	
def main():
	# TODO: enums have human-readable values and types
	print(Fruit.Apple)
	print(type(Fruit.Apple))
	print(repr(Fruit.Apple))
	print(Fruit.Apple.__repr__())
	
	# TODO: enums have name and value properties
	print(Fruit.Apple.name, Fruit.Apple.value)
	
	# TODO: print the auto-generated value
	print(Fruit.PEAR.value)
	
	# TODO: enums are hashable - can be used as keys
	myFruits = {}
	myFruits[Fruit.Banana] = 'Come Mr. Tally-Man'
	print(myFruits[Fruit.Banana])
	
	
if __name__ == '__main__':
	main()
