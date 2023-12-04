# Pinkulani @ 4.12.2023 
# Use bigger numbers (atleast 100 000 000)
def Pi(Len):
	Pi = 4 / 1
	Minus = True
	for X in range(3, Len, 2):
		if Minus == True:
			Pi = Pi - (4 / X)
			Minus = False			
		else:
			Pi = Pi + (4 / X)
			Minus = True

	return Pi
