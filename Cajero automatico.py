#Hecho por Joan/Keiner

import time

print("Iniciando cajero Automatico...\n")
print("Por favor Espere...\n")

#Cuenta regresiva de 3 segundos

for i in range(5, 0, -1):
  print(f"Iniciando en {i}...")
  time.sleep(1) #Espere 1 segundo

import random 
Salir = False
Saldo = 0
Retirar_dinero = 0
Deposito = 0
Movimiento= []

import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear') #termina el codigo de limpiar pantalla 

while not Salir:

#OPCION 1: CLAVES
 print("\n¡Bienvenido al cajero automatico!\n")  
 print("       ""\033[1mSELECCIONE SU OPERACION\033[0m"" \n ")
 print("GESTION DE RETIRO RAPIDO \n")
 print("1. CLAVE             2. CONSULTAS DE MOVIMIENTO \n")
 print("3. PAGOS              4. RETIRO\n")
 print("5. CONSULTAR          6. TRANSFERENCIA\n")
 print("7. DEPOSITAR\n") 
 opcion = input( "SELECCIONE UNA OPCION:")

 if opcion == "1":
    print (f"Tu clave es: \033[1m\033[34m1{random.randint(100000, 999999)}\033[0m\n")
    while True:

     print ("\033[1m\033[34m1. Volver al menu\033[0m     \033[1m\033[31m2. Salir \n\033[0m")
     sub= input ("Seleccione una opcion\n")
     if sub == "1":
       break
     elif sub == "2":
       print ("\033[33m\033[1m¡HASTA LUEGO!\033[0m")
       Salir = True
       break

#OPCION 2: CONSULTAS DE MOVIMIENTO
 elif opcion == "2":
  while True:  
   print(" ---- MOVIMIENTOS ----\n")
   if len(Movimiento) == 0:
       print("\033[31mNo hay movimientos registrados.\033[0m")
       break
   else:
       for Mov in Movimiento:
         print(Mov)
       break
     
  print ("\033[1m\033[34m1. Volver al menu\033[0m     \033[1m\033[31m2. Salir \n\033[0m")
  sub= input ("Seleccione una opcion")
  while True:

   if sub == "1":
       
       break
     
   elif sub == "2":
       print ("\033[33m\033[1m¡HASTA LUEGO!\033[0m")
       Salir = True
       break       
     
     #OPCION 3: PAGOS
 elif opcion == "3":
   print("\033[31mFunción de pagos no implementada aún.\033[0m")
   while True:
     print ("\033[1m\033[34m1. Volver al menu\033[0m     \033[1m\033[31m2. Salir \n\033[0m")
     sub= input ("Seleccione una opcion")
     if sub == "1":
       break
     elif sub == "2":
       print ("\033[33m\033[1m¡HASTA LUEGO!\033[0m")
       Salir = True
       break       
     
     #OPCION 4: RETIRO
 elif opcion == "4": 
   while True:
       Retirar_dinero = float(input("Ingrese el monto a retirar: $"))
       if Retirar_dinero < 0:
         print("\033[31mEl monto no puede ser negativo. Intente nuevamente.\033[0m")
       elif Retirar_dinero > Saldo:
         print("\033[31mFondos insuficientes.\033[0m")
         break
       else:
         Saldo -= Retirar_dinero
         Movimiento.append(f"Retiro: -${Retirar_dinero}")
         print(f"\033[32mRetiro exitoso. Nuevo saldo: ${Saldo}\033[0m")
         break
    
   while True:
     print ("\033[34m1. Volver al menu\033[0m     \033[31m2. Salir \n\033[0m")
     sub= input ("Seleccione una opcion")
     if sub == "1":
       break
     
     elif sub == "2":
       print ("\033[33m\033[1m¡HASTA LUEGO!\033[0m")
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
   print("Función de transferencia no implementada aún")
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
   print("\033[31mOpción inválida. Por favor, seleccione una opción válida.\033[0m")     
 