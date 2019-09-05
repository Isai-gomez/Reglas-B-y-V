#importamos los otros modulos
import reglas_b_con_terminaciones_funciones
import b_buscado

continuar = 1
#print(type(continuar))
while continuar == 1:
	palabra = input("Ingresa un VERBO, PREFIJO O PALABRA para saber si se escribe con B o V:_")
	palabra = palabra.upper()
	if palabra =="":
		print("No escribiste nada")

	elif b_buscado.buscar_b_v(palabra) == False:
		print("LA PALABRA", palabra, "NO TINES B ni V\n")

	else:
	#buscar = palabra.find(sub[palabra, start[palabra, end]])
	#print(buscar)
		verbo = reglas_b_con_terminaciones_funciones.regla_b_con_verbos(palabra)
		prefijo = reglas_b_con_terminaciones_funciones.prefijos_con_b(palabra)
		buscar = b_buscado.silavas_buscadas(palabra)
		con_s = b_buscado.buscar_con_s(palabra)
		cons = b_buscado.constante(palabra)

		print("------------------------------------------------")
		print("En el verbo ",palabra, verbo)
		print("-------------------------------------------------")
		print("En elprefijo " ,palabra ,prefijo)
		print("-----------------------------------------------")
#Preguntamos si la palabra esta bien escrita o no
		print("En la palabra ", palabra, buscar)
		print("-----------------------------------------------")
		print("En la palabra ", palabra, con_s)
		print("-----------------------------------------------")
		print("En la palabra ", palabra, cons)
		print("-----------------------------------------------")
	continuar = int(input("DESEA  VERIFICAR UNA PALABRA  1.SÍ 0.NO; "))
	#termina el programa de b con v
#--------fin del while-------------------
