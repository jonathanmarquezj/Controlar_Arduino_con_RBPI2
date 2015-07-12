import serial

arduino = serial.Serial('/dev/ttyUSB0', 9600)

print("-----------------Conectado------------------")

while True:

        print(arduino.readline())


arduino.close() #Finalizamos la comunicacion

