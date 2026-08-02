#task1.1
def task1_1(input_value):
  input = str(input_value)
  for char in input:#integer validation
    if char < '0' or char > '9':
      return -1
  
  #finds the sum
  if len(input) == 14:#length validation
    sum = 0
    for num in (input[::2]):
      num = int(num) * 2
      sum = sum + num
    
    #check digit calculation
    remainder = sum % 10
    if remainder == 0:
      return int(remainder)
    
    else:
      return int(remainder)

  
  return -1

#main program
print(task1_1(1457656765493))
print(task1_1(14573567654986))

#task 1.2
print(task1_1('1') == -1)
print(task1_1(3) == -1)
print(task1_1('abcdefg') == -1)
print(task1_1(14573567654986) == 6)


#task1.3
def task1_3(input_value):
  input = str(input_value)
  for char in input:#integer validation
    if char < '0' or char > '9':
      return False

  if len(input) == 15:
    original = input[-1:]
    num = input[:-1]
    check_digit = task1_1(num)
    if check_digit == -1:
      return False
    else:
      return check_digit == int(original)

  return False


#main program
print(not task1_3('1') == -1)
print(not task1_3(3) == -1)
print(not task1_3('abcdefg') == -1)
print(not task1_3(14573567654986) == 6)

