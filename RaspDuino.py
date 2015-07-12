import serial
 
arduino = serial.Serial('/dev/ttyUSB0', 9600)
 
print("-----------------Conectado------------------")
print("COMANDOS: A = adelante, I = adelante + izq, D = adelante + der, r = retroceder, i = retoceder + izq, d = retoceder + der, C = Iniciar capota, c = Parar capota, X = Detener todo")
print("ARCHAS: 1 = Lento, 2 = Media, 3 = Alto") 
print("TIEMPO DE REACCION DEL MOTOR: s = Medio segundo, S = Un segundo")
print("SENSOR ULTRASONICO: Z = DESACTIVADO, z = ACTIVADO")
print("AUTOMATICO: M = ON, m = OFF")
print("LED: ROJO = SENSOR, BERDE = MOTOR, AMARILLO = CAPOTA")
print("CONSULTAR DISTANCIA = O , o")

while True: 
      comando = raw_input('Introduce un comando: ') #Input
      arduino.write(comando) #Mandar un comando hacia Arduino
      if comando == 'A':
            print('ADELANTE')
      elif comando == 'r':
            print('RETROCEDER')
      elif comando == 'I':
	    print('IZQUIERDA + ADELANTE')
      elif comando == 'D':
	    print('DERECHA + ADELANTE')
      elif comando == 'i':
	    print('IZQUIERDA + RETROCEDER')
      elif comando == 'd': 
	    print('DERECHA + RETROCEDER')
      elif comando == 'C':
	    print("INICIANDO CAPOTA")
      elif comando == 'c':
	    print("PARANDO CAPOTA")
      elif comando == 'X':
	    print("SE A DETENIDO TODO")
      elif comando == '1':
	    print("PRIMERA MARCHA")
      elif comando == '2':
	    print("SEGUNDA MARCHA")
      elif comando == '3':
	    print("TERCERA MARCHA")
      elif comando == 's':
	    print("REACCION DEL MOTOR MEDIO SEGUNDO")
      elif comando == 'S':
	    print("REACCION DEL MOTOR UN SEGUNDO")
      elif comando == 'Z':
	    print("SENSOR ULTRASONICO DESACTIVADO")
      elif comando == 'z':
	    print("SENSOR ULTRASONICO ACTIVADO")
      elif comando == 'M':
	    print("MODO AUTOMATICO ACTIVADO")
      elif comando == 'm':
	    print("MODO AUTOMATICO DESACTIVADO")
      elif comando == 'O':
            print("COMPROBANDO DISTANCIA EN SENSOR DELANTERO")
      elif comando == 'o':
	    print("COMPROBANDO DISTANCIA EN SENSOR DELANTERO")
      elif comando == 'man':
	    print("-------------------COMANDOS------------------")
	    print("COAMNDOS: A = adelante, I = adelante + izq, D = adelante + der, r = retroceder, i = retoceder + izq, d = retoceder + der, C = Iniciar capota, c = Parar capota, X = Detener todo")
	    print("MARCHAS: 1 = Lento, 2 = Media, 3 = Alto")
	    print("TIEMPO DE REACCION DEL MOTOR: s = Medio segundo, S = Un segundo")
            print("SENSOR ULTRASONICO: Z = OFF, z = OFF")
            print("AUTOMATICO: M = ON, m = OFF")
	    print("LED: ROJO = SENSOR, VERDE = MOTOR, AMARILLO = CAPOTA")
            print("CONSULTAR DISTANCIA = O , o") 
      else:
	    print("COMANDO INCORRECTO")

arduino.close() #Finalizamos la comunicacion
