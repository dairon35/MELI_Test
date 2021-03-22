import sqlite3
import smtplib

miConexion=sqlite3.connect("Mirror_PRD")
miCursor=miConexion.cursor()
'''

Documentacion: Este primer bloque es utilizado para crear las tablas dentro de la base de datos
BLOQUE1

miCursor.execute("create table Usuarios (rowID varchar(3) PRIMARY KEY, confidentiality varchar(6), integrity varchar(6), availability varchar(6), owner varchar(20), uid varchar(10), email varchar(25), user_state varchar(10), Manager varchar(25), time_stamp integer)")
miCursor.execute("create table items (rowID varchar(3) PRIMARY KEY, confidentiality varchar(6), integrity varchar(6), availability varchar(6), owner varchar(20), uid varchar(10), email varchar(25), user_state varchar(10), Manager varchar(25), time_stamp integer)")
miCursor.execute("create table locations (rowID varchar(3) PRIMARY KEY, confidentiality varchar(6), integrity varchar(6), availability varchar(6), owner varchar(20), uid varchar(10), email varchar(25), user_state varchar(10), Manager varchar(25), time_stamp integer)")
miCursor.execute("create table sellers1 (rowID varchar(3) PRIMARY KEY, confidentiality varchar(6), integrity varchar(6), availability varchar(6), owner varchar(20), uid varchar(10), email varchar(25), user_state varchar(10), Manager varchar(25), time_stamp integer)")
miCursor.execute("create table sellers2 (rowID varchar(3) PRIMARY KEY, confidentiality varchar(6), integrity varchar(6), availability varchar(6), owner varchar(20), uid varchar(10), email varchar(25), user_state varchar(10), Manager varchar(25), time_stamp integer)")
miCursor.execute("create table orders (rowID varchar(3) PRIMARY KEY, confidentiality varchar(6), integrity varchar(6), availability varchar(6), owner varchar(20), uid varchar(10), email varchar(25), user_state varchar(10), Manager varchar(25), time_stamp integer)")
miCursor.execute("create table questions (rowID varchar(3) PRIMARY KEY, confidentiality varchar(6), integrity varchar(6), availability varchar(6), owner varchar(20), uid varchar(10), email varchar(25), user_state varchar(10), Manager varchar(25), time_stamp integer)")
'''


'''

Documentacion: Este Segundo bloque es utilizado para crear registros dentro de las tablas
BLOQUE2

#miCursor.execute ("INSERT INTO Usuarios VALUES ('1', 'low', 'high', 'medium', 'Enzo Trossero', 'etrossero', 'enzo.trossero@mercadolibre.com', 'activo', 'romina.marzovilla@mercadolibre.com', '')")
#miCursor.execute ("INSERT INTO items VALUES ('2', 'medium', 'low', ' ', 'Daniel Bertoni', 'dbertoni', ' ', 'activo', 'romina.marzovilla@mercadolibre.com', '')")
#miCursor.execute ("INSERT INTO locations VALUES ('3', 'high', 'high', 'low', 'Ricardo Bochini', 'rbochini', 'ricardo.bochini@mercadolibre.com', 'activo', 'ernesto.vincelli@mercadolibre.com', '')")
#miCursor.execute ("INSERT INTO sellers1 VALUES ('4', 'low', 'medium', 'low', 'Daniel Garnero', 'dgarnero', 'dani.garnero@mercadolibre.com', 'activo', 'romina.marzovilla@mercadolibre.com', '')")
#miCursor.execute ("INSERT INTO sellers2 VALUES ('5', 'low', 'low', 'medium', 'José Pastoriza', 'jopastoriza', 'ose.omar.pastoriza@mercadolibre.com', 'activo', 'ernesto.vincelli@mercadolibre.com', '')")
#miCursor.execute ("INSERT INTO orders VALUES ('6', 'high', 'high', 'medium', 'Luis Alberto Islas', 'laislas', 'luis.islas@mercadolibre.com', 'activo', 'ernesto.vincelli@mercadolibre.com', '')")
miCursor.execute ("INSERT INTO questions VALUES (' ', 'low', 'low', 'low', 'Albeiro Usuriaga', 'ausuriaga', 'albeiro@mercadolibre.com', ' ', ' ', '')")

'''




'''
Documentacion: Este tercer bloque es utilizado para enviar email a los manager
Bloque 3

message= "Buenos dias Estimado, " " el presente email es generado por la certificacion anual de base datos, entendiendo que usted es el Manager del usuario " " necesitamos nos de su Ok para mantener los permisos sobre la base de datos " " de no estar de acuerdo podemos acordar una meet para detallarlos permisos que hoy tiene el usuario o tambien nos puede confirmar por esta via para darlo de baja "

server= smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("daironphyton@gmail.com", "Kal1Ph1t04meli")
server.sendmail("daironphyton@gmail.com", "daironalvarado35@gmail.com", message)

server.quit()


miConexion.commit()

print ("correo enviado")

miConexion.close()
