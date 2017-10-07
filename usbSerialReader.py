import serial
import MySQLdb

conn = MySQLdb.connect(host= "localhost",
                  user="rpi",
                  passwd="",
                  db="rpi")
x = conn.cursor()



s = serial.Serial('/dev/ttyUSB0')
line = s.readline()
print line
datos = line.split(';')
print datos


sql = "INSERT INTO data (humedad, temperatura, humedad_suelo, lluvia, timestamp) VALUES ('"+datos[0]+"','"+datos[1]+"','"+datos[2]+"','"+datos[3]+"',now());"

print sql
try:
	x.execute(sql)
	conn.commit()
except:
	conn.rollback()

conn.close()

