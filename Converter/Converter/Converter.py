def calcBinaryBitValue(i, bit):
    value = 0
    if bit == '1':
        value = 1
        for n in range(0,i):
            value = value * 2
    return value

def calcDenFromBin(digits):
    value = 0
    digits = list(digits)
    digits.reverse() #working from left to right to count values
    for i, bit in enumerate(digits):
        value += calcBinaryBitValue(i, bit)
    return value

def calcHexFromDen(digits):
    value = []
    hexAlphaValues = [(10,'A'),(11,'B'),(12,'C'),(13,'D'),(14,'E'),(15,'F')]
    hexDigits = []
    while digits > 15:
        hexDigits.append(digits % 16)
        digits = digits / 16
    hexDigits.append(int(digits % 16))
    hexDigits.reverse()
    for n in hexDigits:
        if n > 9: #replace numeric value with alpha value
            for h in hexAlphaValues: #search through hexAlphaValues for the matching numeric value
                if h[0] == n:
                    value.append(h[1])
                    break
        else:
            value.append(n)
    return value

def calcBinFromDen(digits):
    value = ''
    while digits > 0:
        value = str(digits%2) + value
        digits = digits//2 #floored division, truncates value, rounds to nearest smallest
    return value

def findInitialBase(inputType, digits):
    if inputType == 'b':
        denValue = calcDenFromBin(digits)
        print('Denary value is {}'.format(denValue))
        hexValue = calcHexFromDen(int(denValue))
        hexString = ''.join(str(e) for e in hexValue)
        print('Hex value is {}'.format(hexString))
    elif inputType == 'h':
        print('hex')
    elif inputType == 'd':
        hexValue = calcHexFromDen(int(digits))
        hexString = ''.join(str(e) for e in hexValue)
        binValue = calcBinFromDen(int(digits))
        print('Hex value is {}'.format(hexString))
        print('Binary value is {}'.format(binValue))
    else:
        print('incorrect suffix')

while True:
    value = input("Please enter value followed by b(binary), h(hex) or d(denary): ")
    dataType = value[-1] #capture suffix
    digits = value[0:-1] #capture digits
    findInitialBase(dataType, digits)
