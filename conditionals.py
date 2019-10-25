# check a temperature and output a result
# the code will chek each if in order, and use the first one that is true
temperature= int (input("input a number between 0 and 100"))

if temperature <= 4:
	print("water is a solid, it is frozen")
elif temperature < 100:
	print("water is a liquid")
else:
	print("water is a gas, it is steam")

