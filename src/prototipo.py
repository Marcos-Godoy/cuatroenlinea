def tableroVacio():
	return [
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
	]

def contenidoColumna(nro_columna, tablero):
	columna = []
	for fila in tablero:
		celda = fila[nro_columna - 1]
		columna.append(celda)
	return columna

def contenidoFila(nro_fila, tablero):
	fila = []
	for x in range(0, 6):
		if nro_fila == x:
			for columna in range(0, 7):
				celda = tablero[x][columna]
				fila.append(celda)
	return fila

def completarTableroEnOrden(secuencia, tablero):
	for x in range(0, len(secuencia)):
		if x % 2 == 0:
			soltarFichaEnColumna(1, secuencia[x], tablero)
		else:
			soltarFichaEnColumna(2, secuencia[x], tablero)
	return tablero


#agregue los returns para hacer los tests.
def mostrarColumnas(tablero):
	columna = []
	for colum in range(0, 7):
		for fil in range(0, 6):
			columna.append(tablero[fil][colum])
			print(tablero[fil][colum], end = ", ")
	return columna

def mostrarFilas(tablero):
	fila = []
	for fil in range(0, 6):
		for colum in range(0, 7):
			fila.append(tablero[fil][colum])
			print(tablero[fil][colum], end = ", ")
	return fila

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
		print('|', end = " ")
		for columna in range(0, 7):
			print(tablero[fila][columna], end = " ")
		print('|')
	print('+', end = "-")
	for x in range(0, 7):
		print('-', end = "-")
	print('+', end = "")


def secuenciaValida(secuencia):
	for columna in secuencia:
		if columna < 1 or columna > 7:
			return False
	return True

secuencia = [1, 2, 3, 1, 1, 6]
tablero = []
"""
secuencia_texto = input("Ingrese la secuencia de numeros: ")
secuencia = []
for items in secuencia_texto.split(','):
	secuencia.append(int(items))

tablero = []
"""
if secuenciaValida(secuencia):
	tablero = completarTableroEnOrden(secuencia, tableroVacio())
	dibujarTablero(tablero)
else:
	print("Las columnas deber??an ir del 1 al 7")

print()
print(contenidoColumna(2, tablero))
print()
print(contenidoFila(5,tablero))
print()
mostrarColumnas(tablero)
print()
mostrarFilas(tablero)