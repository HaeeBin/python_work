import sys
import calendar

def read_file(input, output):
	week = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']
	ubers = {}

	with open(input, "rt") as ip:
		lines = ip.readlines()
		for line in lines:
			element = line.replace("\n", "")
			fields = element.split(",")
			region = fields[0]
			days = fields[1].split("/")
			num = calendar.weekday(int(days[2]), int(days[0]), int(days[1]))
			day = week[num]
			key = region + "," + day
			if key in ubers:
				values = ubers[key]
				value = values.split(",")
				num1 = int(value[0]) + int(fields[2])
				num2 = int(value[1]) + int(fields[3])

				num1 = str(num1)
				num2 = str(num2)
				ubers[key] = num1 + "," + num2		
			else:
				num = fields[2] + "," + fields[3]
				ubers[key] = num
	with open(output, "wt") as op:
		for rKeys, rValues in ubers.items():
			rKey = rKeys.split(",")
			rValue = rValues.split(",")
			op.write("{},{} {},{}\n".format(rKey[0], rKey[1], rValue[0], rValue[1]))

inputpath = sys.argv[1]
outputpath = sys.argv[2]

read_file(inputpath, outputpath)

