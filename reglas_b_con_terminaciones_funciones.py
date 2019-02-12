v = "Se escribe con uve"
bien = "Esta bien escrito"
b = "Se escrbe con be"
mensaje = "No comples las reglas de aquí: "

#función que define el compartamiento de los verbos
def regla_b_con_verbos(palabra):
	resultado = "Esta mal escrita es: "
	#spalabra = palabra.upper()
	verbos = ["VIVIR","SERVIR", "HERVIR"]
	verbos_m = ["BIBIR","SERBIR", "HERBIR"]

	for indice in verbos:
		if palabra== indice:
			return bien, palabra
			break

	for ind in verbos_m:
		if ind == verbos_m[0] and palabra == verbos_m[0]:
			return resultado, verbos[0]
			break
		if palabra == verbos_m[1]:
			return resultado, verbos[1]
			break
		if palabra == verbos_m[2]:
			return resultado, verbos[2]
			break
	# descartamos verbos
	if palabra[-3:] == "BIR" or palabra[-4:] == "BUIR":
		return bien
	elif palabra[-7:] == "BILIDAD":
		return bien
	elif palabra[-2:] == "BA" or palabra[-3:] == "BAS" or palabra[-5:] == "BAMOS" or palabra[-3:] == "BAN":
		return bien
	# verificar mal escrito
	elif palabra[-3:] == "VIR" or palabra[-4:] == "VUIR":
		palabra = palabra.replace("VUIR","BUIR")
		palabra = palabra.replace("VIR","BIR")
		resultado = resultado,palabra
		return resultado
	elif palabra[-7:] == "VILIDAD":
		if palabra[:] == "MOVILIDAD" or palabra[:] == "SERVILIDAD" or palabra[:] == "CIVLILIDAD":
			return bien
		return b
	elif palabra[-2:] == "VA" or palabra[-3:] == "VAS" or palabra[-5:] == "VAMOS" or palabra[-3:] == "BAN":
		return b
	else:
		return mensaje
# Fin de la función validar verbos en pasado y presente

# función que valida prefijos con B
def prefijos_con_b(cadena):
	resultado = "Esta mal escrita es: "
	#cadena = cadena.upper()
	escrito_mal = ["RABIOL", "RABIOLI", "RIBAL", "RIBERA"]
	prefijo = ["RAVIOL", "RAVIOLI", "RIVAL", "RIVERA"]
	for indice in prefijo:
		if cadena == indice:
			return bien, cadena
			break
	for inicio in escrito_mal:
		if cadena == inicio:
			return resultado, indice
			break
	#declaro las reglas de los prefijios
	if cadena[:2] == "BI" or cadena[:3] == "BIS":
		if cadena[:] == "BIBIR":
			return "se escribe VIVIR", "te comento que es un verbo"
		return bien
	elif cadena[:3] == "BIO" or cadena[:3]== "SUB" or cadena[:5] == "BIBLI":
		return bien
	elif cadena[:3] == "RAB" or cadena[:3] == "RIB" or cadena[:3] == "ROB" or cadena[:3] == "RUB":
		return bien
	#buscamos mal escrito
	elif cadena[:2] == "VI" or cadena[:3] == "VIS":
		if cadena[:] == "VIVIR":
			return bien," te comento es un verbo"

	if cadena[:3] == "VIO" or cadena[:3] == "SUV" or cadena[:5] == "VIVLI":
		cadena = cadena.replace("VIO", "BIO")
		cadena = cadena.replace("SUV","SUB")
		cadena = cadena.replace("VIVLI","BIBLI")
		resultado = resultado,cadena
		return resultado
	elif cadena[:3] == "RAV" or cadena[:3] == "RIV" or cadena[:3] == "ROV" or cadena[:3] == "RUV":
		cadena = cadena.replace("RAV","RAB")
		cadena = cadena.replace("RIV","RIB")
		cadena = cadena.replace("ROV","ROB")
		cadena = cadena.replace("RUV","RUB")
		resultado = resultado,cadena
		return resultado
	else:
 		return mensaje
#fin de la función prefijos_con_b
