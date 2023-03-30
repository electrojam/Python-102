import sys 
print(sys.path)

import re  # expresiones regulares, búsqueda de strings que coincida con un texto
text = 'Mi número de teléfono es 311 123 121, el código del pais es 57, mi número de la suerte es 3'
result = re.findall('[0-9]+', text)
print(result)

import time 
timestamp = time.time()
print(timestamp)

local = time.localtime()
result = time.asctime(local)
print(result)

import collections
numbers = [1, 1, 2, 1, 2, 1, 4, 5 , 3, 3, 21]
counter = collections.Counter(numbers)
print(counter)