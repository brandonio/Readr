
def make_dict(essay):
	source = open(essay, "r")
	for line in source:
		for word in line.split():
			word = word.lower()
			word = "".join([char for char in word if char not in forbidden])
			if word not in d:
				d[word] = 1
			else:
				d[word] += 1
	print_sorted_dict(d)

def print_sorted_dict(d, n=3, y=3):
	forbidden = [x+1 for x in range(n)]
	d = sorted(d.items(), key=lambda t: t[1], reverse=True)
	for x in range(len(d)):
		if len(d[x][0]) > y:
			to_print = d[x]
			for nah in forbidden:
				if nah in to_print:
					to_print = list(to_print)
			if type(to_print) != list and "" not in to_print:
				print(to_print[0] + ": " + str(to_print[1]))
	

d = {}

forbidden = ["(", ")", "?", "!", "'", "", " ", ",", "-", ".", "\""]

essay = "sample_txt.txt"
	
make_dict(essay)