#Importar la biblioteca de flask
from flask import Flask, render_template, request,url_for, redirect


#Objeto para inicilizar la aplicacion
#1. nombre por defecto
#2. ruta donde esta los templates o nombre de la carpeta
app = Flask(__name__, template_folder='KARENCUEVA')

#Clave secreta de la aplicacion


#Controlador de la ruta por defecto
# Ingreso de datos por formulario
# Mostras las tareas pendientes
@app.route('/index.html')
def principal():
    return render_template("index.html")

# which URL is associated function
#@app.route('/', methods =["GET", "POST"])
@app.route('/')
def formulario():
   # if request.method == "POST":
       # getting input with freq = set_freq in HTML form
       #correo = request.form.get("correo") # <--- do whatever you want with that value
       #contraseña = request.form.get("contraseña") # <--- do whatever you want with that value
       #return  + correo + contraseña
    return render_template("login.html")


#@app.route('/signup.html', methods =["GET", "POST"])
@app.route('/signup.html')
def registro():
    #if request.method == "POST":
       # getting input with freq = set_freq in HTML form
       #correo = request.form.get("correo") # <--- do whatever you want with that value
       #ontraseña = request.form.get("contraseña") # <--- do whatever you want with that value
       #return  + correo + contraseña
     return ("signup.html")

@app.route('/team.html')
def team():
    return render_template('team.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/blog.html')
def blog():
    return render_template('blog.html')

#Metodo para correr la aplicacion
if __name__ == '__main__':
    app.run(debug=True)

