def mostrar_menu():
  print("\nTOTEM AUTOATENCIÓN CAFECONLECHE")
  print("1.- Comprar entrada a Cats.")
  print("2.- Cambio de función.")
  print("3.- Mostrar stock de funciones.")
  print("4.- Salir.")

def comprar_entrada(compradores, Stockv, StockS):
  nombre = input("Ingrese el nombre del comprador: ")
  if nombre in compradores:
    print("El nombre del comprador ya existe.")
    return compradores, Stockv, StockS

  print("\nSeleccione la función:")
  print("1. Cats Día Viernes (Stock:", Stockv, ")")
  print("2. Cats Día Sábado (Stock:", StockS, ")")

  try:
    opcion_funcion = int(input("Ingrese el número de la función: "))
    if opcion_funcion == 1:
      if Stockv > 0:
        compradores[nombre] = "Función 1"
        Stockv -= 1
        print("Compra exitosa para la Función 1.")
      else:
        print("No hay stock disponible para la Función 1.")
    elif opcion_funcion == 2:
      if StockS > 0:
        compradores[nombre] = "Función 2"
        StockS -= 1
        print("Compra exitosa para la Función 2.")
      else:
        print("No hay stock disponible para la Función 2.")
    else:
      print("Opción de función inválida.")
  except ValueError:
    print("Debe ingresar un número válido para la función.")

  return compradores, Stockv, StockS

def cambio_funcion(compradores, Stockv, StockS):
  """Permite cambiar la función de un comprador."""
  nombre = input("Ingrese el nombre del comprador para el cambio de función: ")
  if nombre not in compradores:
    print("El comprador no existe.")
    return compradores, Stockv, StockS

  funcion_actual = compradores[nombre]
  print(f"El comprador {nombre} tiene entrada para la {funcion_actual}.")

  confirmar = input("¿Desea cambiar de función? (s/n): ").lower()
  if confirmar == 's':
    if funcion_actual == "Función 1":
      if StockS > 0:
        compradores[nombre] = "Función 2"
        Stockv += 1
        StockS -= 1
        print("Cambio exitoso a la Función 2.")
      else:
        print("No hay stock disponible para la Función 2.")
    elif funcion_actual == "Función 2":
      if Stockv > 0:
        compradores[nombre] = "Función 1"
        StockS += 1
        Stockv -= 1
        print("Cambio exitoso a la Función 1.")
    else:
      print("Error: Función actual desconocida.")
  elif confirmar == 'n':
    print("No se realizó el cambio de función.")
  else:
    print("Respuesta inválida. No se realizó el cambio.")

  return compradores, Stockv, StockS

def mostrar_stock(Stockv, StockS):
  """Muestra el stock disponible de cada función y el total."""
  print("\nStock de Funciones:")
  print("Función 1 (Cats Día Viernes):", Stockv, "entradas disponibles")
  print("Función 2 (Cats Día Sábado):", StockS, "entradas disponibles")
  print("Total de entradas disponibles:", Stockv + StockS)
  print("Total de entradas vendidas:", 150 + 180 - (Stockv + StockS))


if __name__ == "Principal":
  compradores = {}
  Stockv = 150
  StockS = 180

  while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")

    if opcion == '1':
      compradores, Stockv, StockS = comprar_entrada(compradores, Stockv, StockS)
    elif opcion == '2':
      compradores, Stockv, StockS = cambio_funcion(compradores, Stockv, StockS)
    elif opcion == '3':
      mostrar_stock(Stockv, StockS)
    elif opcion == '4':
      print("Programa terminado...")
      break
    else:
      print("Debe ingresar una opción válida!!")