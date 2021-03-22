import sqlite3

miConexion=sqlite3.connect("Mirror_PRD")
miCursor=miConexion.cursor()


#miCursor.execute("create table Usuarios (confidentiality varchar(6), integrity varchar(6), availability varchar(6), owner varchar(20), uid varchar(10), email varchar(25), userID integer, user_state varchar(10), Manager varchar(25), time_stamp integer)")

#miCursor.execute ("INSERT INTO Usuarios VALUES ('low', 'high', 'medium', 'Enzo Trossero', 'etrossero', 'enzo.trossero@mercadolibre.com', '1', 'activo', 'romina.marzovilla@mercadolibre.com', '')")

miCursor.execute("SELECT * FROM Usuarios")

confidentiality=miCursor.fetchall()


for producto in confidentiality:
    

    print ("El nivel de confidencialidad es: ",producto[0], "El owner de la Base es: ", producto[3], "Por favor solicitar autorizacion al Manager mediante el email: ",producto[8])


miConexion.commit()


miConexion.close()
