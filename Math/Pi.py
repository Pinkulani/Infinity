# Pinkulani © 2023
def Pi(Resolution):
	Pi = 4 / 1
	Minus = True
	for X in range(3, Resolution, 2):
		if Minus == True:
			Pi = Pi - (4 / X)
			Minus = False			
		else:
			Pi = Pi + (4 / X)
			Minus = True

	return Pi