Salir = False
Saldo = 0
Retirar_dinero = 0
Deposito = 0
Clave = 123456

while not Salir:

 print("       ""SELECCIONE SU OPERACION"" \n ")
 print("GESTION DE RETIRO RAPIDO \n")
 print("1. CLAVES             2. CONSULTAS DE MOVIMIENTO \n")
 print("3. PAGOS              4. RETIRO\n")
 print("5. CONSULTAR          6. TRANSFERENCIA\n")
 print("7. DEPOSITAR\n") 
 opcion = input( "SELECCIONE UNA OPCION:")

 if opcion == "1":
  print ("1. Ver clave    2. Volver al menu\n")
  opcion = int(input("Seleccione una opcion\n"))
  if opcion == 1:
    print (f"Tus claves son: {Clave}\n")
    while True:

     print ("1. Volver al menu     2. Salir \n")
     sub= input ("Seleccione una opcion\n")
     if sub == "1":
       break
     elif sub == "2":
       print ("¡Hasta luego!")
       Salir = True
       break
  if opcion == "2":
    break

 elif opcion == "2":
   print ("Consultas de movimiento\n")


       

