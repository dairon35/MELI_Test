# MELI
Challenge Compliance

El siguiente codigo es generado de acuerdo a la necesidad planteada en el challenge, el archivo que contiene el codigo principal se llama BBDD.py el mismo se encuentra dividido en bloques.

Bloque1 crea la base de datos (Mirror_PRD) y tablas. Al momento de crear la tabla asignamos el rowID como primary KEY ya que este es un dato que no debe de repetirse en un active directory, ni en la creacion de un usuario local.

Bloque2 carga los datos sobre cada tabla.

Bloque3 (incompleto) se comunica con el servidor smtp de gmail, por medio de una cuenta que cree con el objetivo de enviar un email a cada manager de acuerdo al contenido que se almacene en X variable que contega la salida obtenida al realizar una query a la base de datos especificamente que me diga la columna owner, manager y nombre de la tabla cuando el campo confidentiality sea igual a high. 

Todo el bloque 3 tiene que estar dentro de un bucle que salga cuando termine de enviar email a cada uno de los manager.

El bloque 3 seria una de las ideas que se me ocurrio de optimizar el proceso de certificacion anual de las bases de datos.

La segunda forma que se me ocurrio fue generar un PDF a partir de una query contra la base de datos que tenga como objetivo mostrar el owner, manager y nombre de la tabla cuando el campo confidentiality sea igual a high, cabe destacar que esta segunda opcion tendria una parte manual y seria enviar los email.

Importante:
El codigo se encuentra dentro del archivo BBDD.py y la base de datos se llama Mirror_PRD.
La base de datos esta creada en sqlite3 y el editor de texto usado es sublime text.
Los demas archivos son intentos de completar el ejercicio.
