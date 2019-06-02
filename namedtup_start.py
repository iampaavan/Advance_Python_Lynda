# Demonstrate the usage of namedtuple objects

import collections


def main():
	# TODO: create a Point namedtuple
	Point = collections.namedtuple("Co_Ordinates", "x y")
	p1 = Point(10, 20)
	p2 = Point(30, 40)
	print(p1, p2)
	print(p1.x, p2.y)

	# TODO: use _replace to create a new instance
	p1 = p1._replace(x=100)
	p2 = p2._replace(y=50)
	print(p1)
	print(p2)


if __name__ =="__main__":
	main()