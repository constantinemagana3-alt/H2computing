#task1.1
def encrypt(value):
  ascii_num = ord(value)
  if ascii_num == 32:#if value if !
    ascii_num = 33#changes space to !
    return ascii_num,chr(ascii_num)

  elif ascii_num < 65 or ascii_num > 122:#if it is a character, validation
    return -1

  else:
    new_num = ascii_num + 10#new value
    return new_num,chr(new_num)


#task1.2
print(encrypt('A'))
print(encrypt('a'))
print(encrypt('#'))
print(encrypt(' '))


#task1.3
with open('DATATOENCRYPT.txt','r') as f:
  lines = f.readlines()

char_lst = []
for line in lines:
  for char in line:
    char_lst.append(char)


with open('ENCRYPTEDMESSAGE.txt','w') as file:
  for char in char_lst:
    encrypted = encrypt(char)
    if encrypted != -1:
      file.write(str(encrypted[1]))
