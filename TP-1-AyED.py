import getpass
correo_admin = ("admin@ventaspasajes777.com")
passw_admin = ("admin")
intentos = 0
max_intentos = 3



correo_resultado = input("ingrese su correo electronico: ")
contraseña_resultado = input("ingrese su contraseña: ")

if correo_resultado == correo_admin and contraseña_resultado == passw_admin:
    print("ingreso exitoso")
    print("""1. Gestión de Aerolíneas | 2. Aprobar/Denegar Promociones | 3. Gestión de Novedades | 4. Reportes | 5. Salir""")
else:
 print("el correo o contraseña que ingresaste es incorrecto, intenta nuevamente")

opcion_elegida_menu = 1,2,3,4,5
if opcion_elegida_menu == 1:
 print("""a. Crear Aerolínea
        b. Modificar Aerolínea
        c. Eliminar Aerolínea
        d. Volver""")
elif opcion_elegida_menu == 3:
  print("""a. Crear Novedad
2
b. Modificar Novedad
c. Eliminar Novedad
d. Ver Novedades
e. Volver""")

