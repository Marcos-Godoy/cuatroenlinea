from src.prototipo import tableroVacio

def test_tablero_vacio_tiene_6_filas_y_7_columnas():
	tablero = tableroVacio()
	assert len(tablero[0]) == 7
	assert len(tablero) == 6
