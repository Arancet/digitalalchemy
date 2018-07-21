#TO RUN: save file and in POWERSHELL type
#PS C:\Users\Trypt> C:\Users\Trypt\AppData\Local\Continuum\anaconda3\python.exe C:\Users\Trypt\OneDrive\Desktop\exercise1.py

def which_is_smaller(x, y):
	if x > y:
		print(y)
		return(y)
	elif x < y:
		print(x)
		return(x)
	else:
		print("EQUAL!")
		return("EQUAL!")

which_is_smaller(4, 8)

