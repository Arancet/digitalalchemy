testlist = [3, 7, 0, 4]
x = 0
for index in range(len(testlist)):
	print testlist[index] + 1
	
for x in testlist:
	print(x+1)
	
while len(testlist) > 0:
	testlist.pop(0)

if 4 == 4.0:
	print(4+4.0)

#function below. Also use pound sign for comments
def plus_one(number):
	return number+1

def minus_one(number):
	return number-1

