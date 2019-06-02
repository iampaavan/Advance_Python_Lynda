# Use lambdas as in-place functions


def CelciusToFahrenheit(temp):
	return (temp * 9/5) + 32


def FahrenheitToCelcius(temp):
	return (temp - 32) * 5/9


def main():
	ctemps = [0, 12, 34, 100]
	ftemps = [32, 65, 100, 212]
	
	# TODO: Use regular functions to convert temps
	print(list(map(CelciusToFahrenheit, ctemps)))
	print(f'***********************************')
	print(list(map(FahrenheitToCelcius, ftemps)))
	
	print(f'*************************************************************')
	
	# TODO: Use lambdas to accomplish the same thing
	print(list(map(lambda t: (t * 9/5) + 32, ctemps)))
	print(f'****************************************')
	print(list(map(lambda t: (t - 32) * 5/9, ftemps)))
	
	
if __name__ == '__main__':
	main()