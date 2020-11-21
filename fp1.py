# Write a python program to create a file

import os.path
fn=input("Enter the name of the file:\n")

if os.path.exists(fn):
	print("File name already exists")
else:
	fn=open(fn,'a')
	print(fn,"created")
	fn.close()
