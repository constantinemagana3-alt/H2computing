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
  for i in range of (1,len(list_of_integers)):
    key = list_of_integers[i]
    while j = 0 and list_of_integers[j - 1] > list_of_integers[j]:
      list_of_integers[j], list_of_integers[j-1] = list_of_integers[j-1],list_of_integers[j],
