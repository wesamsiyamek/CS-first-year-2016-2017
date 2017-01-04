"""
Does it work on files where no error checking is needed on the fields

>>> sumRows("rows1.csv") == {'tim': 36.0, 'bob': 11.0, 'anna': 54.0}
True

Does it ignore headers if requested?

>>> sumRows("rows1.csv", header=True) == {'tim': 36.0, 'anna': 54.0}
True

Is it returning the right type of result?
>>> type(sumRows("rows1.csv"))
<class 'dict'>

Does it work on files with empty fields or fields which aren't numbers?

>>> sumRows("rows2.csv") == {'tim': 24.0, 'bob': 11.0, 'anna': 13.0}
True

Does it sum columns correctly?
>>> sumColumns("columns.csv") == {'': 0, 'tim': 5.0, 'bob': 41.0, 'anna': 55.0}
True
"""
# *** DO NOT CHANGE CODE ABOVE THIS LINE ***
# *** DO NOT ADD ANY COMMENTS OF YOUR OWN IN THE SUBMITTED SOLUTION ***

import csv
def sumRows(filename, header=False):

	dic = {}
	data_csv = open(filename)
	rdr = csv.reader(data_csv, delimiter= ',')
	
	if header == True:
		next(data_csv)
	
	for row in rdr:
		name, value_1,value_2, value_3 = row
				
		try:
			float(value_1)
		except ValueError:
			value_1 = 0

		try:
			float(value_2)
		except ValueError:
			value_2 = 0

		try:
			float(value_3)
		except ValueError:
			value_3 = 0

		summ = float(value_1) + float(value_2) + float(value_3)
		dic[name] = summ

	return dic

def sumColumns(filename):

	with open(filename) as csvfile:
		headerline=csvfile.readline()

		dic = {}
		names=[]

		for key in headerline.split(","):
			if (key.isalpha() == True):
	
				names.append(key)

			else:

				continue

		for x in range(len(names)):

			csvfile.seek(0)
			csvfile.readline()
			names.insert((x*2)+1,sum(int(r[x]) for r in csv.reader(csvfile)))

		for c in range(len(names)-3):
			dic[names[c*2]]=float(names[(c*2)+1])

		dic[''] = 0

		return dic