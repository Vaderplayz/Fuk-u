from datetime import datetime 

#defining the amount list
daily = []
def delete():
	31days = [1, 3, 5, 7, 8, 10, 12]
	30days = [2, 4, 6, 9, 11]
	month = datetime.now().strftime("%m")
	if month in 31days and len(daily) == 31:
		daily = []
	elif month in 30days and len(daily) == 30:
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
	delete()
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
			print("The amount you entered as exceeded the allowed paramenters. Would you like to hear some advice?")
			while True:
				command = input("%> ")
				if command.lower() == "yes" or command.lower() == "y":
					#enter scenario here
					print("Help")
					break
				elif command.lower() == "no" or command.lower() == "n":
					#enter scenario here
					print("No help")
					break
				else:
					print("Command error, try again!")
			daily.append(amount)
			print(daily)


if __name__ == "__main__":
	while True:
		getAmount()
	
