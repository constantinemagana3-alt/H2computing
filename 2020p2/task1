#task 1.1
def task1_1(string_value):
  h = 0
  i = 0
  for i in range(len(string_value)):
    val = 33 * ord(string_value[i])
    h = (h + val) % 1024
  return h

#main program
print(task1_1("Hello"))
print(task1_1("Hallo"))
print(task1_1("Hullo"))

#task 1_2
def task1_2(seed, string_value):
  new_string_value = seed + string_value
  return task1_1(new_string_value)

#main program
print(task1_2("seed-one","Hello"))
print(task1_2("seed-two","Hello"))
print(task1_2("seed-three","Hello"))

