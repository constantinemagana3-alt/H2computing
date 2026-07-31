#task 2.1
import random
def task2_1(filename,quantity,maximum):
  with open(filename, 'w') as file:
    for i in range(quantity):
      num = random.randint(0,maximum)
      file = file.write(str(num))

#task 2.2
def task2_2(list_of_integers):
  low = 0
  high = len(list_of_integers) - 1
  if low == high:
    return list_of_integers[low]
  
  mid = (low + high) // 2

  arleft = mergesort(list_of_integer[:mid])#sorts the left array
  arRight = mergesort(list_of_integer[mid:])#sorts the right array

  return merge(arLeft,arRight)


def merge(arLeft,arRight):
  result = []
  i = 0#pointer for left array
  j = 0#pointer for right array
  k = 0#pointer for result array
  while i < len(arLeft) and j < len(arRight):
    if arLeft[i] > arRight[j]:
      result[k] = arRight[j]
      j = j + 1
      k = k + 1
    
    else:
      result[k] = arLeft[i]
      i = i + 1
      k = k + 1
  
  while i < len(arLeft):#remainder of the left array
    result[k] = arLeft[i]
    k += 1
    i += 1

  while j < len(arRight):#remainder of the right array
    result[k] = arRight[j]
    k += 1
    j += 1
  
  return result


#task2.3
def task2_3(filename_in,filename_out):
  with open(filename_in,'r') as file:
    lsit_of_integers = []
    for line in file:
      line = line.strip()
      line = int(line)
      list_of_integers = list_of_integers.append(line)
  
  sorted_array = task2_2(list_of_integers)

  with open(filename_out,'w') as file:
    for value in sorted_array:
      file = file.write(str(value) + '\n')

#main program
task2_3("random_numbers.txt","sorted_numbers.txt")
