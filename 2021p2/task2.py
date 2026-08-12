#task2.1
def task2_1(filename):
  with open(filename,'r') as file:
    list_of_int = []
    for line in file:
      line = line.strip()
      list_of_int.append(int(line))
  return list_of_int
#file.close()

#main program
result = task2_1('TEN.txt')
print(result)
print(len(result))


#task2.2
def task2_2(list_of_integers):
  for i in range(1,len(list_of_integers)):
    key = list_of_integers[i]
    j = j - 1
    while j >= 0 and list_of_integers[j] > key:
      list_of_integers[j + 1] = list_of_integers[j]
      j = j + 1

    list_of_integers[j + 1] = key

  return list_of_integers

#task2.3
def task2_3(list_of_integers,low = 0,high = None):
  if low < high:
    pivot = partition(list_of_integers,low,high)

    quicksort(list_of_integers,low,pivot -1)
    quicksort(list_of_integers,pivot + 1,high)


def partition(list_of_integers,low,high):
  pivot = list_of_integers[high]
  i = low - 1

  for j in range(low,high):
    if list_of_integerss[j] <= pivot:
      i += 1
      list_of_integers[i],list_of_integers[j] = list_of_integers[j],list_of_integers[i]
  list_of_integers[i + 1],list_of_integers[high] = list_of_integers[high],list_of_integers[i+1]

  return i + 1


#task2.4
import timeit

t1000 = task2_1('THOUSAND.txt')
time1000 = timeit.timeit(lambda: task2_2(t1000), number = 1)
print(time1000)#task2.1
def task2_1(filename):
  with open(filename,'r') as file:
    list_of_int = []
    for line in file:
      line = line.strip()
      list_of_int.append(int(line))
  return list_of_int
#file.close()

#main program
result = task2_1('TEN.txt')
print(result)
print(len(result))


#task2.2
def task2_2(list_of_integers):
  for i in range of (1,len(list_of_integers)):
    key = list_of_integers[i]
    while j = 0 and list_of_integers[j - 1] > list_of_integers[j]:
      list_of_integers[j], list_of_integers[j-1] = list_of_integers[j-1],list_of_integers[j],
