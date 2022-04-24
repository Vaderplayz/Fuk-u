#defining the amount list
daily = []
def checker(amount):
	status = ""
	if amount <= 130 and type(amount) == int:
		#enter if smaller or equal than 30 situation here
		status = "Excellent"
	elif amount > 130 and type(amount) == int:
		#enter if larger than 30 situation here
		status = "Poor"
	else:
		status = "Error"
	return status
def getAmount():
	global daily
	#check the amount of number in array
	if len(daily) == 31:
		print("Reseting array")
		daily = []
	while True:
		try:
			amount = int(input("Type amount of water you used today."))
		except TypeError:
			print("Variable entered is not integer")
	
		if checker(amount=amount) == "Excellent":
			print("Your water usage for today is great!")
			daily.append(amount)
			break
		elif checker(amount=amount) == "Poor":
			print("The amount you entered as exceeded the allowed paramenters. Try to reduce it")
			daily.append(amount)
			print(daily)


if __name__ == "__main__":
	while True:
		getAmount()
	