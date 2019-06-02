# Demonstrate how to use list comprehensions


def main():
	# define two list of numbers
	evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
	odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
	my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	
	# TODO: Perform a mapping and filter functions on a list
	evenSquared = list(map(lambda e: e**2, filter(lambda e:  4 < e < 16, evens)))
	print(evenSquared)
	even = list(filter(lambda e: e % 2 == 0, my_list))
	print(even)
	
	# TODO: Derive a new list of numbers from a given list
	list_even_Squared = [e ** 2 for e in evens]
	print(list_even_Squared)
	
	# TODO: Limit the items operated on with a predicate condition
	odd_Squared = [e ** 2 for e in odds if 3 < e < 17]
	print(odd_Squared)
	
	
if __name__ == '__main__':
	main()
