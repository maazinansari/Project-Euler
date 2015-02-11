FirstFib = 1
SecondFib = 1
TotalFib = 0
fibSequence = [1]
while TotalFib < 4000000:
	TotalFib = FirstFib + SecondFib
	fibSequence.append(TotalFib)
	FirstFib = SecondFib
	SecondFib = TotalFib
listLength = len(fibSequence)
evenSum = 0
for i in range(0, listLength):
	if fibSequence[i] % 2 == 0:
		evenSum = evenSum + fibSequence[i]
print evenSum