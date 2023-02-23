from flask_app import app

#Importar nuestro controlador, la carpeta se llama "controllers"
from flask_app.controllers import users_controller, appointments_controller

#Ejecutamos variable app
if __name__=="__main__":
    app.run(debug=True)