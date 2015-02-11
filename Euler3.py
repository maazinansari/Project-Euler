number = 600851475143

def Factorize(x):
	factors = []
	i = x
	while i >= 1:
		if x % i == 0:
			factors.append(i)
		i = i - 1
	return factors

factorsOfNumber = Factorize(number)

numberOfFactors = len(factorsOfNumber)

primeFactors = []

for j in range(1, numberOfFactors):
	nextFactor = factorsOfNumber[j]
	FactorizedFactor = Factorize(nextFactor)
	if len(FactorizedFactor) < 3:
		primeFactors.append(factorsOfNumber[j])
print primeFactors[0]