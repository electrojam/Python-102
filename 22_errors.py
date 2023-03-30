try: 
  print(0 / 0)
  assert 1 != 1, 'Error => Uno no es igual que uno'
  age = 0
  if age < 18:
   raise Exception('No se permiten menores de edad')
except ZeroDivisionError as error:
  print('Nuevo error =>', error)
except AssertionError as error:
  print(error)
except Exception as error:
  print(error)

print('Hola')
print('Hola 2')