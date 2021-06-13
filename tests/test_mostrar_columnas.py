from src.prototipo import mostrarColumnas

def test_mostrar_columnas():
	columna = [1, 2, 1, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	tablero = [
		[1, 0, 0, 0, 0, 0, 0],
		[2, 0, 0, 0, 0, 0, 0],
		[1, 0, 0, 0, 0, 0, 0],
		[2, 0, 0, 0, 0, 0, 0],
		[1, 0, 0, 0, 0, 0, 0],
		[2, 0, 0, 0, 0, 0, 0],
	]


	assert mostrarColumnas(tablero) == columna