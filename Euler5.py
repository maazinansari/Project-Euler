smallestMultiple = 1

def Factorize(x):
	factors = []
	i = 1
	while i <= x:
		if x % i == 0:
			factors.append(i)
		i = i + 1
	return factors

nextNumber = 1

while nextNumber < 21:
	if smallestMultiple % nextNumber != 0:
		factorsOfNextNumber = Factorize(nextNumber)
		smallestMultiple = smallestMultiple * factorsOfNextNumber[1]
	nextNumber += 1

print smallestMultiple