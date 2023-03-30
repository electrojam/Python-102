with open('./text.txt', 'w+') as file:
  for line in file:
    print(line)
  file.write('nueva línea en este archivo\n')
  file.write('Otra  línea\n')
  file.write('Otra  línea\n')