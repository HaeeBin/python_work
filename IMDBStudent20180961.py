import sys

def read_file(inputpath,outputpath):
	movie = {}

	with open(inputpath, "rt") as ip:
		lines = ip.readlines()
		for line in lines:
			element = line.replace('\n',"")
			fields = element.split('::')
			genres = fields[2].split('|')
			for genre in genres:
				if genre in movie:
					movie[genre] += 1
				else:
					movie[genre] = 1

	with open(outputpath, "wt") as op:
		for key, value in movie.items():
			op.write("{} {}\n".format(key, value))

input = sys.argv[1]
output = sys.argv[2]

read_file(input, output)
