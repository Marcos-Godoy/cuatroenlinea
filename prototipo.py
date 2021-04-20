secuencia = [1, 2, 3, 1, 1, 6]

def tableroVacio():
	return [
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
	]

def completarTableroEnOrden(secuencia, tablero):
	for x in range(0, len(secuencia)):
		if x % 2 == 0:
			soltarFichaEnColumna(1, secuencia[x], tablero)
		else:
			soltarFichaEnColumna(2, secuencia[x], tablero)
	return tablero

"""
def validarSecuencia(secuencia):
	ban = 0
	for x in range(0, len(secuencia)):
		if secuencia[x] > 7:
			#print("Secuencia incorrecta!! Por favor vuelva a intentarlo.")
			ban = 1
			break
	return ban
"""

def soltarFichaEnColumna(ficha, columna, tablero):
	for fila in range(6, 0, -1):
		if tablero[fila - 1][columna - 1] == 0:
			tablero[fila - 1][columna - 1] = ficha
			return


def dibujarTablero(tablero):
	for fila in range(0, 6):
		for columna in range(0, 7):
			print(tablero[fila][columna], end = " ")
		print('')


def secuenciaValida(secuencia):
	for columna in secuencia:
		if columna < 1 or columna > 7:
			return False
	return True

if secuenciaValida(secuencia):
	dibujarTablero(completarTableroEnOrden(secuencia, tableroVacio()))
else:
	print("Las columnas deberían ir del 1 al 7")