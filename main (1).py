from datetime import datetime 

#defining the amount list
daily = []
thirtyone = [1, 3, 5, 7, 8, 10, 12]
thirty = [2, 4, 6, 9, 11]
month = int(datetime.now().strftime("%m"))
if month in thirtyone:
	count = 31
elif month in thirty:
	count = 30
def delete():
	global thirtyone
	global thirty
	global month
	global daily
	if month in thirtyone and len(daily) == 31:
		daily = []
	elif month in thirty and len(daily) == 30:
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
	sum = 0
	global count
	#check the amount of number in array
	delete()
	while True:
		try:
			amount = int(input("Input amount of Water: "))
			if len(daily) >= 1:
				daily.append(amount)
				#calculate the sum within the daily
				for i in daily:
					sum = sum + i
				#sum 
				results = sum + (daily[-1] * count)
				if amount < sum:
					conclusion = f"{sum - amount}L less than predicted"
				elif amount > sum:
					conclusion = f"{amount - sum}L more than predicted"
				else:
					conclusion = "as predicted"
				#reduce by 1 everyday
				count = count - 1
				#calculate the percentage
				percentage = daily[-1] / daily[-2] * 100
				if percentage > 100:
					status = "more than"
				elif percentage < 100:
					percentage = 100 - percentage
					status = "less than"
				else:
					status = "the same as"
				print(f"Your usage today was {percentage}% {status} yesterday, {conclusion}")
			else: 
				daily.append(amount)
		except TypeError:
			print("Variable entered is not integer")
		

	
if __name__ == "__main__":
	while True:
		getAmount()
	
