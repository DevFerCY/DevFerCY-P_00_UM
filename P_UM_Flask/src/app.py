#Iportar flask
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from flask_mysqldb import MySQL #Importar MySQL
from flask_login import LoginManager, login_user, logout_user, login_required

from config import config #Importar de mi archivo config


# Modelos:
#--------------------------------------------------------------------------------
from Models.ModelUser import ModelUser #Se inmporta el modelo de User

#Entities:
#--------------------------------------------------------------------------------
from Models.entities.User import User


app = Flask(__name__) #Se instancia flask
csrf = CSRFProtect()

db = MySQL(app) #instanciar MySql

login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)



# Rutas
##------------------------------------------------------
## Ruta Index
@app.route('/')
def Index():
    return redirect(url_for('login'))

## Ruta Registro de Usuario
@app.route('/paciente/registro')
def Persona_Registro():
   return render_template('register/registro.html')


## Ruta Login
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        #return request.form
        user = User(0,request.form['InputUsername'],request.form['InputPassword'])
        logged_user = ModelUser.login(db,user)
        if logged_user != None:
            if logged_user.password:
              login_user(logged_user)
              return redirect(url_for('Home'))
            else:
                 flash('Contraseña incorrecta...')
                 return render_template('auth/login.html')
        else:
           
           flash('Usuario no registrado...')
           return render_template('auth/login.html')
    else: 
        return render_template('auth/login.html')
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return 'pagina no encontrada', 404

## Home    
@app.route('/inicio')
@login_required
def Home():
    return render_template('home.html')
    


if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401,status_401 )
    app.register_error_handler(404,status_404 )
    app.run()

#if __name__ == '__main__':
 #   app.run(port=3000, debug=True)