def isPalindrome(x):
	x = str(x)
	totalDigits = len(x)
	lastDigit = (totalDigits - 1)
	x_reverse = "" 
	while lastDigit >= 0:
		x_reverse = x_reverse + x[lastDigit]
		lastDigit = lastDigit - 1
	if x == x_reverse:
		return True
	else:
		return False	
		
number1 = 999
largestPalindrome = 0

while number1 > 100:
	number2 = 999
	while number2 > 100:
		testProduct = number1 * number2
		if isPalindrome(testProduct) and testProduct > largestPalindrome:
			largestPalindrome = testProduct
		number2 -= 1
	number1 -= 1
	
print largestPalindrome