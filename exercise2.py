def is_char(char):
	if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
		print("True")
		return("True")
	else:
		print("False")
		return("False")

def wordlist(words): #DOESNT WORK
	#count = 0
	for count in words:
		print(len(words[count])) 
		
#def beersong():
#	count = 99
#	while count != 0:
		#print(count " bottles of beer on the wall, " count " bottles of beer. You take one down, you pass it around, " (count-1) " bottles of beer on the wall.")
#		beerstring = count + " bottles of beer on the wall, " + count + " bottles of beer. You take one down, you pass it around, " + (count-1) + " bottles of beer on the wall."
#		print(beerstring)
#		count = count-1
		
def beersong2():
	bottles_of_beer = 99
	while bottles_of_beer > 0:
		print(bottles_of_beer)
		print("bottles of beer on the wall")
		print(bottles_of_beer)
		print("bottles of beer")
		print("you take one down, pass it around")
		print(bottles_of_beer-1)
		print("bottles of beer on the wall!")
		bottles_of_beer = bottles_of_beer-1
		
		
#is_char("a")
#is_char("l")


#wordarray = ["test", "try", "catfish"]
#wordlist(wordarray)


beersong2()



#import syntax
#import math #math is the name of module to import
#math.ceil(5) #use ciel function inside math module, ciel will return cieling of x, the smallest integer greater than or equal to x
#can import just one function, IE from math import ciel
#then use ciel(5)

import pandas as pd

#df = pd.read_csv("iris.csv")
df = pd.read_csv("/Users/Trypt/OneDrive/Desktop/iris.csv")

import numpy as np

num_df = pd.DataFrame(np.random.

def fizz_buzz_ify(cell):
	cell = float(cell)
	If (cell % 3.0 == 0) & (cell % 5.0):
		
		
		
num_df.applymap(fizz_buzz_ify).head()

df.plot('Sepal Length', 'Sepal Width', kind="scatter")





















df.head() #OR
df.describe() #< WORKS



df.rows(5) #WRONG
df.ix[5,] #RIGHT

df.cells(5,2) #WRONG
df.ix[5,2] #RIGHT

df['Petal Width']

group = df.groupby("Species")
print(group.head())




import matplotlib.pyplot as plt
plt.scatter(df['Sepal Width'], df['Sepal Length'])
plt.xlabel('Sepal Width')
plt.ylabel('Sepal Length')
plt.title('Sepak Width vs Sepal Length')
plt.show()

#df.to_csv("filepath.csv") method will take the data file and export it into a csv file as specified