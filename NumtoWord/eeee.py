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
  x = str(x)
  if x[0] == '0':
    return digit[x[1]]
  if x[0] == '1':
    return digit[x]
  else:
    return ten[x[0]] + ' ' + digit[x[1]]

def integer(number, inc):
  number = str(number)
  e = str(inc + 1)  
  if len(number) == 3:  
    if difference == 0:      
      return 'Hundred ' + 'and ' + tens(number[1:3])
    elif number[0] == "0":
      if number[1:3] == "00":
        return ''
      return 'and ' + tens(number[1:3]) + ' ' + factor[e] + ','
    else:
      return 'Hundred ' + 'and ' + tens(number[1:3]) + ' ' + factor[e] + ','
  elif difference == 0:
    return tens(number) 
  else:
    return tens(number) + ' ' + factor[e]


def loopy(x):
  numlist = ([str(x[::-1][i:i+3][::-1]) for i in range(0, len(x), 3)][::-1]) 
  length = len(numlist)
  index = 0
  global difference 
  #pdb.set_trace()
  
  for i in numlist:
    index += 1
    difference = length - index
    if len(numlist[0]) < 3 and index == 1:
      print(f"{integer(i,difference)}", end=" ")  # not quite

    else:    
      print(f"{str(digit[i[0]])} {integer(i,difference)}", end=" ")
  print('\n')


loopy("1")
loopy("10")
loopy("18")
loopy("20")
loopy("99")
loopy("101")
loopy("132")
loopy("1024")  # One Thousand,  Hundred and Twenty Four
loopy("12560")  # Twelve Thousand,  Five Hundred and Sixty  Hundred,
# [120]000[555] One Hundred and Twenty  Million,   Hundred and  Thousand,  Five Hundred and Fifty Five Hundred,
loopy("120000555")
loopy("50342")  # Fifty  Thousand,  Three Hundred and Fourty Two Hundred
loopy("383578325783257032085")
