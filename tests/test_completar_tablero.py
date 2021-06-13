from src.prototipo import completarTableroEnOrden

def test_devuelve_tablero_completo():
	tablero = [
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		]

	assert completarTableroEnOrden([1,2,3,4,5,6,7],tablero) == [
																[0, 0, 0, 0, 0, 0, 0],
																[0, 0, 0, 0, 0, 0, 0],
																[0, 0, 0, 0, 0, 0, 0],
																[0, 0, 0, 0, 0, 0, 0],
																[0, 0, 0, 0, 0, 0, 0],
																[1, 2, 1, 2, 1, 2, 1],
																]