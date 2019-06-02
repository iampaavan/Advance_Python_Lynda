# Demonstrate the usage of OrderedDict objects
from collections import OrderedDict


def main():
	# list of sport teams with wins and losses
	sporteams = [('Royals', (18, 12)), ('Rockets', (24, 6)),
	             ('Cardinals', (20, 10)), ('Dragons', (22, 8)),
	             ('Kings', (15, 15)), ('Chargers', (20, 10)),
	             ('Jets', (16, 14)), ('Warriors', (25, 5))]
	
	# sort the teams by number of wins
	sortedTeams = sorted(sporteams, key=lambda t: t[1][0], reverse=True)
	print(sortedTeams)
	
	# TODO: create an ordered dictionary of the items
	teams = OrderedDict(sortedTeams)
	print(teams)
	
	# TODO: Use popitem to remove the top item
	tm, wl = teams.popitem(False)
	print(f"Top Team: {tm, wl}")
	
	# TODO: What are the next top 4 teams
	print(f"Next Top 4 Teams")
	for index, team in enumerate(teams, start=1):
		print(index, team)
		
		if index == 4:
			break
	
	# TODO: equality check
	a = OrderedDict({"a": 1, "b": 2, "c": 3})
	b = OrderedDict({"a": 1, "b": 2, "c": 3})
	c = OrderedDict({"a": 1, "c": 3, "b": 2})
	d = {"a": 1, "b": 2, "c": 3}
	
	print(f"Equality Check 1: {a == b}")
	print(f"Equality Check 2: {a == c}")
	print(f"Equality Check 3: {a == d}")
	
	
if __name__ == '__main__':
	main()