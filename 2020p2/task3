#task3.1
def task3_1(quantity_of_data):
  units = {
      'KB' : 10**3,
      'MB' : 10**6,
      'GB' : 10**9,
      'TB' : 10**12,
  }
  unit = quantity_of_data[-2:]
  if unit not in units:
    return print('invalid data')
  else:
    return ((units[unit]) * int(quantity_of_data[:-2]))

#main program
print(task3_1('8KB'))
print(task3_1('4LB'))



#task3.2
def task3_2(quantity_of_data):
  units = {
      'KiB' : 2**10,
      'MiB' : 2**20,
      'GiB' : 2**30,
      'TiB' : 2**40,
  }

  unit = quantity_of_data[-3:]
  print(unit)
  if unit not in units:
    return print('invalid data')
  else:
    unit = units[unit]
    return (unit * float(quantity_of_data[:-3]))

#main program
print(task3_2('2MiB'))

#task3.3
def task3_3(quantity_of_data, target_unit):
    units = {
        'KiB': 2**10,
        'MiB': 2**20,
        'GiB': 2**30,
        'TiB': 2**40,
        'KB': 10**3,
        'MB': 10**6,
        'GB': 10**9,
        'TB': 10**12,
    }

    if target_unit not in units:
        print("invalid data")
        return "invalid data"

    num_bytes = task3_2(quantity_of_data)

    if num_bytes is None:
        print("invalid data")
        return "invalid data"

    result = num_bytes / units[target_unit]

    print(result)
    return result
