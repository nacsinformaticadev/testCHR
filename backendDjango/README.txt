el proyecto trae por nombre backendDjango

dentro encontraran la carpeta app que contiene una app llamada core
en esta app proceso las 2 vistas para cada template de cada ejercicio otorgado

quise por orden separar las logicas y no hacerla todo dentro de la vista como 
lo hace normalmente la gente.


1.- abrir y llegar hazta la ruta de proyecto backendDjango (altura de settings.py)

2.- usar requirements.txt // pip install -r requirements.txt

3.- en la altra de settings.pu encontraras un archivo llamado conf.json en el cual alojo variables importantes en este caso
	usalo para remplazar los datos de tu base de datos a la cual quieres que se conecte, en caso de que no sepas, dejare la conf de sqlite default
	para descomentar y usar 

4.- vuelve a la altura del manage.py

5.- python manage.py runserver

6.- localhost:8000 para ver el proyecto y localhost:8000/admin para ingresar al panel admin

7.- pass de panel admin  user:admin
			pass:admin



tarea 1 no pude concretar la consulta api porque no era una ruta api consultable
pero deje una app dentro de la carpeta app jurisprudencias que tiene toda la logica 

y la terea 2 en la app concesionemaritimas esta toda la logica de la tarea 2, pero lamentablemente 
por desconocimiento del paquete no pude concretar la tarea.

aun asi deje las logicas y conecciones y todod listo para usar.
