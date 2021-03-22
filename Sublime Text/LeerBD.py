#-*-coding utf8-8 -*-
import os
import sys
import sqlite3
phyton -m pip install fpdf

'''miConexion = sqlite3.connect("Mirror_PRD")

def Ver():
	miConexion = sqlite3.connect("Mirror_PRD")
	cursor=con.cursor()
	cursor.execute("SELECT * FROM Usuarios")

	for Mostrar in cursor:
		print("rowID" [0])


miConexion.close()		


#from io import open

#Clasificacion_high=open("Clasificacion_High.txt","w")