bien = "Esta bien escrito"
mal = "No cumple con las reglas de aquí"


def silavas_buscadas (palabra):
	resultado = "Esta mal escrita es: "
	#palabra = palabra.upper()
	contar_tav = palabra.count("TAV")
	contar_tur = palabra.count("TURV")
	contar_tab = palabra.count("TAB")
	contar_tub = palabra.count("TURB")

	if contar_tav == 1:
		palabra = palabra.replace("TAV","TAB")
		resultado = resultado,palabra
		return resultado
	elif contar_tur == 1:
		palabra = palabra.replace("TURV", "TURB")
		resultado = resultado,palabra
		return resultado
	#Esta bien escrita
	elif contar_tab == 1:
		return bien
	elif contar_tub ==1:
		return bien
	#return palabra, contar
	else:
		return mal

def buscar_con_s(palabra):

	resultado = "Esta mal escrita es: "
	#palabra = palabra.upper()
	contar_sav = palabra.count("SAV")
	contar_sov = palabra.count("SOV")
	contar_su = palabra.count("SUV")
	contar_sab = palabra.count("SAB")
	contar_sob = palabra.count("SOB")
	contar_sub = palabra.count("SUB")

	if contar_sav == 1:
		palabra = palabra.replace("SAV","SAB")
		resultado = resultado,palabra
		return resultado
	elif contar_sov == 1:
		palabra = palabra.replace("SOV", "SOB")
		resultado = resultado,palabra
		return resultado
	elif contar_su == 1:
		palabra = palabra.replace("SUV", "SUB")
		resultado = resultado,palabra
		return resultado
	#La palabra esta bien escrita
	elif contar_sab == 1:
		return bien
	elif contar_sob ==1:
		return bien
	elif contar_sub ==1:
		return bien
	else:
		return mal

def buscar_b_v (st):
	b = st.count("B")
	v = st.count("V")
	estado = False
	if b > 0 or v > 0:
		estado = True
		return estado
	else:
		return estado

def constante (caracter):
	resultado = "Esta mal escrita es: "
	#caracter = caracter.upper()
	contar_br = caracter.count("BR")
	contar_bs = caracter.count("BS")
	contar_bl = caracter.count("BL")
	contar_bt = caracter.count("BT")
	contar_vr = caracter.count("VR")
	contar_vs = caracter.count("VS")
	contar_vl = caracter.count("VL")
	contar_vt = caracter.count("VT")
	contar_cub = caracter.count("CUB")
	contar_cuv = caracter.count("CUV")

	if contar_vr == 1:
		caracter = caracter.replace("VR","BR")
		resultado = resultado,caracter
		return resultado
	elif contar_vs == 1:
		caracter = caracter.replace("VS", "BS")
		resultado = resultado,caracter
		return resultado
	elif contar_vl == 1:
		caracter = caracter.replace("VL", "BL")
		resultado = resultado,caracter
		return resultado
	elif contar_vt == 1:
		caracter = caracter.replace("VT", "BT")
		resultado = resultado,caracter
		return resultado
	elif contar_cuv == 1:
		caracter = caracter.replace("CUV", "CUB")
		resultado = resultado,caracter
		return resultado
	#La palabra esta bien escrita
	elif contar_br == 1:
		return bien
	elif contar_bs ==1:
		return bien
	elif contar_bl ==1:
		return bien
	elif contar_bt == 1:
		return bien
	elif contar_cub == 1:
		return bien
	else:
		return mal
