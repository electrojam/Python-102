import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
  fig, ax = plt.subplots() #figura y coord. inicio gráfico
  ax.bar(labels, values) #tipo de gráfica y valores
  plt.show() #se pide que se muestre la gráfica

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots() 
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()
  
if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [100, 200, 80]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)



