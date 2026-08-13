#task2_1
import random
def task2_1():
  lst = []
  count = 1
  while count <= 100:
    lst.append(random.randint(1,100))
    count += 1
  
  return lst

#task2_2
def task2_2(lst):
  for i in range(0,len(lst) - 1):
    for j in range(0,len(lst) - 1 - i):
      if lst[j] > lst[j + 1]:
        lst[j],lst[j+1] = lst[j+1],lst[j]
  return lst

#task2_3
def task2_3(lst,low,high):
  if low == high:
    return [lst[low]]
  
  mid = (low+ high)//2

  arRight = task2_3(lst,low,mid)
  arLeft = task2_3(lst,mid + 1, high)

  return merge(arRight,arLeft)


def merge(arRight,arLeft):
  i = 0
  j = 0
  k = 0
  result = [None] * (len(arRight) + len(arLeft))

  while i < len(arRight) and j < len(arLeft):
    if arRight[i] < arLeft[j]:
      result[k] = arRight[i]
      i += 1
      k += 1

    else:
      result[k] = arLeft[j]
      j += 1
      k += 1
  
  while i < len(arRight):
      result[k] = arRight[i]
      i += 1
      k += 1    

  while j < len(arLeft):
      result[k] = arLeft[j]
      j += 1
      k += 1
  
  return result


#task2.4
def task2_4(lst,int_value,low ,high):
  if low > high:
    return -1
  
  mid = (low + high) // 2

  if lst[mid] == int_value:
    return mid

  elif lst[mid] < int_value:
    return task2_4(lst,int_value,mid + 1,high)

  else:
    return task2_4(lst,int_value,low,mid - 1)




#main program
lst = task2_1()
while True:
  user_input = input("Please select a sorting algorithm(Bubble or Merge)")
  
  if user_input == "Bubble":
    sorted = task2_2(lst)
    print(sorted)
    break
  
  elif user_input == "Merge":
    sorted = task2_3(lst,0,len(lst) - 1)
    print(sorted)
    break
for i in range(2):
  input2 = int(input("What no. to search for"))
  result = task2_4(sorted,input2,0,len(lst) - 1)
  if result == -1:
    print("Not Found")
  else:
    print(f"Found at index {result}")
