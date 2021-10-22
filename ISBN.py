def ISBN(digits):
    counter = 0    
    for i in range(0,len(digits)):
        if (i % 2) == 0:
            counter += int(digits[i])
        else:
            counter += int(digits[i]) * 3
    DigitTwelth = 10 - counter%10
    return DigitTwelth    

print(ISBN("978030640615"))