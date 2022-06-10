#Importar la biblioteca de flask
from re import A
from flask import Flask, render_template, request, redirect, url_for
import json
#ruta donde esta los templates o nombre de la carpeta
app=Flask(__name__, template_folder='template')
pacientes = {}
#Objeto para inicilizar la aplicacion
#nombre por defecto
#Controlador de la ruta por defecto
@app.route('/')
def login():
    return render_template("login.html")
    
@app.route('/sesion', methods =["GET", "POST"])
def sesion():
    if request.method == 'POST':
        correo = request.form.get('correo')
        contraseña = request.form.get('contraseña')

        with open('pacientes.json') as file:
            registro = json.loads(file.read())
            for n in range(len(registro)):   
              print(registro[n]['correo'])
            return redirect(url_for('index'))
            
    else:
      return render_template('/sesion')

@app.route('/index.html')
def index():
    return render_template("index.html")
    

@app.route('/signup.html', methods =["GET", "POST"])
def registro():
    if request.method == 'POST':
        with open('pacientes.json') as file:
            registro = json.load(file)
        #Obtenemos los datos ingresados en el formulario
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        contraseña = request.form.get('contraseña')

        pacientes = {
            'nombre': nombre,
            'correo': correo,
            'contraseña': contraseña
        }
        
        registro.append(pacientes)

        with open('pacientes.json') as file:
            json.dump(registro, file)
        
        return redirect(url_for('/login.html'))
    else:
      return render_template('signup.html')

@app.route('/team.html')
def team():
    return render_template('team.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/class.html')
def classs():
    return render_template('class.html')


@app.route('/testimonials.html')
def blog():
    return render_template('testimonials.html')

#Metodo para correr la aplicacion
if __name__ == '__main__':
    app.run(debug=True)

