import os

TAX_MINIMUM_NUM = 3500

taxBaseArray  = [1500, 4500, 9000, 35000, 55000, 80000, 999999999]
taxPercentage = [0.03,  0.1,  0.2,  0.25,   0.3,  0.35,      0.45]
# taxMinusNum   = [   0,  105,  555,  1005,  2755,  5505,     13505]
taxMinusNum   = [0]

#below is the data of houseFoundationBase and SocialInsuranceBase for 2016
houseFoundationBase = 19715
SocialInsuranceBase = 12929.76

def computeTaxMinusNum():
	for i in range(1, len(taxBaseArray)):
		taxMinusNum.append(taxBaseArray[i-1]*(taxPercentage[i]-taxPercentage[i-1]) + taxMinusNum[i-1])
	print 'taxMinusNum:'
	print taxMinusNum

def calculateFee(numberToPayTax):
	taxFee = 0

	if numberToPayTax <= 0:
		raise NameError('numberToPayTax <= 0')

	numberRemovedTaxMinumNum = numberToPayTax - TAX_MINIMUM_NUM;

	if numberToPayTax <= 0:
		taxFee = 0
	else:
		for i in range(0, len(taxBaseArray)):
			if taxBaseArray[i] >= numberRemovedTaxMinumNum:
				taxFee = numberRemovedTaxMinumNum * taxPercentage[i] - taxMinusNum[i]
				break
	return taxFee

def numberAfterPayTax(numberToPayTax):

	return numberToPayTax - calculateFee(numberToPayTax)

# -------------- main --------------
if __name__ == '__main__':
	computeTaxMinusNum()
	while True:
		print 'input a number to calculate numberAfterPayTax:'
		numberToPayTax = float(raw_input())
		taxFee = calculateFee(numberToPayTax)
		print 'After pay tax, the number is:'
		print '    ' + str(numberToPayTax - taxFee)
		print '    ' + 'the fee is:' + str(taxFee)
