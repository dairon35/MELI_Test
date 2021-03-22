import sqlite3

miConexion=sqlite3.connect("Mirror_PRD")
miCursor=miConexion.cursor()


#miCursor.execute("create table Usuarios (confidentiality varchar(6), integrity varchar(6), availability varchar(6), owner varchar(20), uid varchar(10), email varchar(25), userID integer, user_state varchar(10), Manager varchar(25), time_stamp integer)")

miCursor.execute ("INSERT INTO Usuarios VALUES ('low', 'high', 'medium', 'Enzo Trossero', 'etrossero', 'enzo.trossero@mercadolibre.com', '1', 'activo', 'romina.marzovilla@mercadolibre.com')")

#miCursor.execute("SELECT * FROM Usuarios")

#confidentiality=miCursor.fetchall()

#for levelconfidentiality in confidentiality:
    
 #   print("Nivel de confidencialidad: ", levelconfidentiality[0], "nombre del Owner: ",levelconfidentiality[3], "Email del owner: ", levelconfidentiality[5])


miConexion.commit()


miConexion.close()

, "Email de Manager: ", levelconfidentiality[8]