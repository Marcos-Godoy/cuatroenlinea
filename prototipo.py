secuencia = [1, 2, 3, 1]


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

dibujarTablero(
	completarTableroEnOrden(
		secuencia, tableroVacio()
		)
	)
