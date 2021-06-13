from src.prototipo import secuenciaValida

def test_devuelve_validacion():
	secuenciaCorrecta = [1,2,3,4]
	secuenciaIncorrecta = [0,1,2,8] 

	assert secuenciaValida(secuenciaCorrecta)
	assert not(secuenciaValida(secuenciaIncorrecta))