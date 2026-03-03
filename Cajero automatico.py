#Hecho por Joan/Keiner

import random 
Salir = False
Saldo = 0
Retirar_dinero = 0
Deposito = 0
Movimiento= []

while not Salir:

#OPCION 1: CLAVES
 print("       ""SELECCIONE SU OPERACION"" \n ")
 print("GESTION DE RETIRO RAPIDO \n")
 print("1. CLAVE             2. CONSULTAS DE MOVIMIENTO \n")
 print("3. PAGOS              4. RETIRO\n")
 print("5. CONSULTAR          6. TRANSFERENCIA\n")
 print("7. DEPOSITAR\n") 
 opcion = input( "SELECCIONE UNA OPCION:")

 if opcion == "1":
    print (f"Tu clave es: {random.randint(100000, 999999)}\n")
    while True:

     print ("1. Volver al menu     2. Salir \n")
     sub= input ("Seleccione una opcion\n")
     if sub == "1":
       break
     elif sub == "2":
       print ("¡Hasta luego!")
       Salir = True
       break

#OPCION 2: CONSULTAS DE MOVIMIENTO
 elif opcion == "2":
  while True:  
   print(" ---- MOVIMIENTOS ----\n")
   if len(Movimiento) == 0:
       print("No hay movimientos registrados.")
       break
   else:
       for Mov in Movimiento:
         print(Mov)
       break
     
  print ("1. Volver al menu     2. Salir \n")
  sub= input ("Seleccione una opcion")
  while True:

   if sub == "1":
       
       break
     
   elif sub == "2":
       print ("¡Hasta luego!")
       Salir = True
       break       
     
     #OPCION 3: PAGOS
 elif opcion == "3":
   print("Función de pagos no implementada aún.")
   while True:
     print ("1. Volver al menu     2. Salir \n")
     sub= input ("Seleccione una opcion")
     if sub == "1":
       break
     elif sub == "2":
       print ("¡Hasta luego!")
       Salir = True
       break       
     
     #OPCION 4: RETIRO
 elif opcion == "4": 
   while True:
       Retirar_dinero = float(input("Ingrese el monto a retirar: $"))
       if Retirar_dinero < 0:
         print("El monto no puede ser negativo. Intente nuevamente.")
       elif Retirar_dinero > Saldo:
         print("Fondos insuficientes.")
         break
       else:
         Saldo -= Retirar_dinero
         Movimiento.append(f"Retiro: -${Retirar_dinero}")
         print(f"Retiro exitoso. Nuevo saldo: ${Saldo}")
         break
    
   while True:
     print ("1. Volver al menu     2. Salir \n")
     sub= input ("Seleccione una opcion")
     if sub == "1":
       break
     
     elif sub == "2":
       print ("¡Hasta luego!")
       Salir = True
       break       
     
     #OPCION 5: CONSULTAR SALDO
 elif opcion == "5":
   print(f"Saldo actual: ${Saldo}")
   while True:
     
     print ("1. Volver al menu     2. Salir \n")
     sub= input ("Seleccione una opcion")
     
     if sub == "1":
       break
     
     elif sub == "2":
       print ("¡Hasta luego!")
       Salir = True
       
       break       
     
     #OPCION 6: TRANSFERENCIA
 elif opcion == "6":
   print("Función de transferencia no implementada aún.")
   while True:
     
     print ("1. Volver al menu     2. Salir \n")
     sub= input ("Seleccione una opcion")
     
     if sub == "1":
       break
     
     elif sub == "2":
       print ("¡Hasta luego!")
       Salir = True
       
       break       
     
     #OPCION 7: DEPOSITAR
 elif opcion == "7":
    while True:  
     try:
       Deposito = float(input("Ingrese el monto a depositar: $\n"))
       
       if Deposito < 0:
         print("El monto no puede ser negativo. Intente nuevamente.\n")

       elif Deposito >= 0:
         Saldo += Deposito
         Movimiento.append(f"Depósito: +${Deposito}\n")
         print(f"Depósito exitoso. Nuevo saldo: ${Saldo}\n")
         
      
     
     except ValueError:
       print("Entrada inválida. Por favor, ingrese un número válido.")

     print ("1. Volver al menu     2. Salir \n")
     sub= input ("Seleccione una opcion")
     
     if sub == "1":
       break
     
     elif sub == "2":
       print ("¡Hasta luego!")
       Salir = True
       
       break
 else:
   print("Opción inválida. Por favor, seleccione una opción válida.")     
 