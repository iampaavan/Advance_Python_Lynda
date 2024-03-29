# use iterators functions like enumerate, zip, iter, next


def main():
	# define a list of days in English and French
	days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
	days_french = ['Dim', 'Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam']
	
	# TODO: user iter to create an iterator over a collection
	i = iter(days)
	print(next(i))
	print(next(i))
	print(next(i))
	
	# TODO: iterate using a function and a sentinel
	with open('testfile.txt', 'r') as fp:
		for line in iter(fp.readline, ''):
			print(line)
	print(f'************************************************')
	
	# TODO: use regular iteration over the days
	for m in range(len(days)):
		print(m+1, days[m])
	print(f'************************************************')
	
	# TODO: using enumerate reduce code and provides a counter
	for i, m in enumerate(days, start=1):
		print(i, m)
	print(f'************************************************')
	
	# TODO: use zip to combine sequences
	for m in zip(days, days_french):
		print(m)
	print(f'************************************************')
	
	for i, m in enumerate(zip(days, days_french), start=1):
		print('index ' + str(i), m[0] + ' = ' + m[1] + ' in French')
	
	
if __name__ == '__main__':
	main()