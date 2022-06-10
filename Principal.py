#Importar la biblioteca de flask
from flask import Flask, render_template, request
#ruta donde esta los templates o nombre de la carpeta
app=Flask(__name__, template_folder='template')
#Objeto para inicilizar la aplicacion
#nombre por defecto
#Controlador de la ruta por defecto
@app.route('/')
def login():
    return render_template("login.html")
    
@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/signup.html')
def signup():
     return render_template("signup.html")

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

