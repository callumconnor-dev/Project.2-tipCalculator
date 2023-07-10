print("Welcome to the tip calculator")
bill = float(input("What was the total bill? £"))
percentageTip = float("1." + (input("What percentage tip would you like to give? 10, 12, or 15? ")))
split = int(input("How many people to split the bill? "))

calculateTip = bill * percentageTip
calculateSplit = "{:.2f}".format(calculateTip / split)

print (f"Each person should pay: £{calculateSplit}")