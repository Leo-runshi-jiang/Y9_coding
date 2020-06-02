limit = input("what is the speed limit?")
speed = input("what is the speed of the car?")

difference = float(speed) - float(limit)

if difference <= 0:
	print("Congratulations, you are within the speed limit!")

if difference >0 and difference <21:
	print("You are speeding and your fine is $100")

if difference > 20 and difference <31:
	print("You are speeding and your fine is $270")

if difference > 30:
	print("You are speeding and your fine is $500")
