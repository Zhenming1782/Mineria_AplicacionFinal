from efficient_apriori import apriori
import csv

def data_generator(filename):
  """
  Data generator, needs to return a generator to be called several times.
  """
  def data_gen():
    with open(filename) as file:
      for line in file:
        yield tuple(k.strip() for k in line.split(','))      

  return data_gen

def agregar_compra(compra):
    with open('dataset.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(compra)
    csvFile.close()


min_support=0.01
min_confidence=0.5

while True:

  transactions = data_generator('dataset.csv')
  itemsets, rules = apriori(transactions, min_support, min_confidence)
  print ("Soporte actual:"+str(min_support))
  print ("Confianza actual:"+str(min_confidence))
  compra = []
  opcion = int(input("Desea:\n1-Soporte\n2-Confianza\n3-Agregar Compra\n4-Mostrar productos vendidos\n5-Mostrar Reglas de asociacion\n6-Salir\nOpcion: "))
  if opcion == 1:
    min_support = float(input("Digite el nuevo soporte: "))
  elif opcion == 2:
    min_confidence = float(input("Digite la nueva confianza: "))
  elif opcion == 3:
    cantidad = int(input("Digite la cantidad de articulos comprado: "))
    for i in range(0,cantidad):
      aux = input("Digite el articulo "+ str(1+i)+":")
      compra.append(aux.strip(" "))
    agregar_compra(compra)
  elif opcion == 4:
    print(itemsets)
    break
  elif opcion == 5:
    print(rules)
    break
  elif opcion == 6:
    print("Gracias por usar la aplicacion")
    break
  else:
    print("Error!!! Opcion invalida!")
    
