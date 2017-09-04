import time

minutos = 1
segundos = 60
minutosPrimo = minutos
segundosPrimo = segundos
for m in range (0,minutos+1):
	for s in range(0,segundos):
		if segundosPrimo == 0:
			minutosPrimo = minutosPrimo - 1
			segundosPrimo = segundos
		segundosPrimo = segundosPrimo - 1
		mm = str(minutosPrimo)
		ss = str(segundosPrimo)
		print(mm + ":" + ss)
		time.sleep(1)

