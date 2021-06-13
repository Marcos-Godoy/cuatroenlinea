from src.prototipo import contenidoFila

def test_contenido_fila():
	tablero = [
		[1, 2, 1, 2, 1, 2, 1],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		]

	assert [1, 2, 1, 2, 1, 2, 1] == contenidoFila(0, tablero)