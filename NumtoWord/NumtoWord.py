import pdb
digit = {
  "0": "",
  "1": "One",
  "2": "Two",
  "3": "Three",
  "4": "Four",
  "5": "Five",
  "6": "Six",
  "7": "Seven",
  '8': 'Eight',
  '9': 'Nine',
  '10': 'Ten',
  '11': 'Eleven',
  '12': 'Twelve',
  '13': 'Thirteen',
  '14': 'Fourteen',
  '15': 'Fithteen',
  '16': 'Sixteen',
  '17': 'Seventeen',
  '18': 'Eighteen',
  '19': "Nineteen"
}
ten = {
    '1': 'Ten',
    '2': 'Twenty',
    '3': 'Thirty',
    '4': 'Fourty',
    '5': 'Fifty',
    '6': 'Sixty',
    '7': 'Seventy',
    '8': 'Eighty',
    '9': 'Ninety'
}
factor = {
    '1': 'Hundred',
    '2': 'Thousand',
    '3': 'Million',
    '4': 'Billion',
    '5': 'Trillion',
    '6': 'Quadrillion',
    '7': 'Quintillion',
    '8': 'Sextillion',
    '9': 'Septillion',
    '10': 'Octillion',
    '11': 'Nonillion',
    '12': 'Decillion',
    '13': 'Undecillion',
    '14': 'Duodecillion',
    '15': 'Tredecillion',
    '16': 'Quattuordecillion',
    '17': 'Quindecillion',
    '18': 'Sexdecillion',
    '19': 'Septendecillion',
    '20': 'Octodecillion',
    '21': 'Novemdecillion',
    '22': 'Vigintillion',
    '23': 'Unvigintillion',
    '24': 'Duovigintillion',
    '25': 'Trevigintillion',
    '26': 'Quattuorvigintillion',
    '27': 'Quinvigintillion',
    '28': 'Sexvigintillion',
    '29': 'Septenvigintillion',
    '30': 'Octovigintillion',
    '31': 'Nonvigintillion',
    '32': 'Trigintillion',
    '33': 'Untrigintillion',
    '34': 'Duotrigintillion'
}

def tens(x):
  #take x as a string for manipulation 
  x = str(x)
  # if the first digit is 0, we know it's [0-9] and we can return the last digit of the number through the digit dictionary 
  if x[0] == '0':
    return digit[x[1]]
  # if the first digit is 1, we know it's 10-19, and we can return the whole number through the digit dictionary
  if x[0] == '1':
    return digit[x]
  # otherwise we know it's 20-99, hence we have to return the tens dictionary for x[0] and the digit dictinary for x[1], hence 87 = eighty & seven
  else:
    return ten[x[0]] + ' ' + digit[x[1]]

def integer(number, inc):
  #take each inputs as strings
  number = str(number)    
  e = str(inc)   
  # if the first number of the current set contains 0
  if number[0] == "0":
    # and if the whole set is 000, return nothing
    if number[1:3] == "00":
      return ''
    # and if it's the final set, return tens with the last two digits as input i.e 'seventeen'
    elif difference == 1:
      return tens(number[1:3])
    #otherwise return tens with last two digits and the factor '34 million'
    return tens(number[1:3]) + ' ' + factor[e] + ', '

  #if the set contains 3 numbers i.e. a hundreds digit - 3 HUNDERED 45 thousand
  elif len(number) == 3:
    #if it's the last set don't return a factor 
    if difference == 1:      
      return digit[number[0]] + ' Hundred ' + 'and ' + tens(number[1:3])
    #otherwise return the same but with the factor included
    else:
      return digit[number[0]] + ' Hundred ' + 'and ' + tens(number[1:3]) + ' ' + factor[e] + ', '  
  #if it's the final set and not of 3 length return tens 
  elif difference == 1:
    return tens(number[0:2])
  # if first set has less than 3 digits, return tens with the factor
  else:
    return tens(number) + ' ' + factor[e] + ', '
# Take a string input of a number to output the "text" version of that number "one hundred"
def loopy(x):
  #use list comprehension to put the string in 'sets of 3' format i,e 12345678 = [12][345][678]
  numlist = ([str(x[::-1][i:i+3][::-1]) for i in range(0, len(x), 3)][::-1])
  #find how many sets the number has, 3 for [12][345][678]. This is equivlent to the factor dictionary, 3 - Millions, 2 thousands, 1 - hundred
  length = len(numlist)
  # define difference as a global variable so it can be accessed in other functions.
  global difference
  #index similarly counts the sets upto length, so we know how far through the number we are.
  index = 0
  #for each set in te number
  for i in numlist:
    index += 1
    #difference helps us find the factor that the specific set is going to be. Plus one alligns it correctly
    difference = (length - index) +1        
    #print the output of the integer function, we want to print each loop on the same line hence end. 
    #i inputs the number in the set, while difference as sated before will find factor of the specifc set
    print(f"{integer(i,difference)}", end="") 
  print('\n')


def test_tens():
  assert tens(18) == "Eighteen"


loopy("1")
loopy("10")
loopy("18")
loopy("20")
loopy("99")
loopy("101")
loopy("132")
loopy("1024")  # One Thousand,  Hundred and Twenty Four
loopy("12560")  # Twelve Thousand,  Five Hundred and Sixty  Hundred,
loopy("120000555") #[120]000[555] One Hundred and Twenty  Million,   Hundred and  Thousand,  Five Hundred and Fifty Five Hundred,
loopy("50342")  # Fifty  Thousand,  Three Hundred and Fourty Two Hundred
loopy("383578325783257032085") #[383]578[325]783[257]032[085]
