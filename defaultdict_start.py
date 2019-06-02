# Demonstrate the usage of defautdict objects
from collections import defaultdict


def main():
	# define a list of items that we want to count
	fruits = ['apple', 'pear', 'orange', 'banana',
	          'apple', 'grape', 'banana', 'banana']
	
	# use a dictionary to count each element
	fruitCounter = {}
	fruit_obj = defaultdict(int)
	lambda_fruit = defaultdict(lambda: 100)
	
	# Count the elements in the list
	for fruit in fruits:
		if fruit in fruitCounter:
			fruitCounter[fruit] += 1
		else:
			fruitCounter[fruit] = 1
	
	# Count the elements after using defaultdict()
	for f in fruits:
		fruit_obj[f] += 1
		
	for i in fruits:
		lambda_fruit[i] += 1
	
	for (k, v) in fruitCounter.items():
		print(k + ':' + str(v))
		
	print(f'***************************************************')
	
	for key, values in fruit_obj.items():
		print(key + ':' + str(values))
		
	print(f'***************************************************')
	
	for p, q in lambda_fruit.items():
		print(p + ':' + str(q))
		
	
if __name__ == '__main__':
	main()
