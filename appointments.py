from flask_app.config.mysqlconnection import connectToMySQL #Importación de la conexión con bd
from flask import flash #flash es el encargado de mandar mensajes/errores

from datetime import datetime  #Manipular fechas

class Appointment:

    def __init__(self, data):
        self.id = data['id']
        self.task = data['task']
        self.date = data['date']
        self.status= data['status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @staticmethod
    def valida_task(formulario):
        es_valido = True

        if formulario['task'] == '':
            flash('task cannot be empty', 'appointments')
            es_valido = False
        
        if formulario['date'] == '':
            flash('Ingrese una fecha', 'appointment')
            es_valido = False
        else:
            date_obj = datetime.strptime(formulario['date'], '%Y-%m-%d') #Estamos transformando un texto a formato de fecha
            hoy = datetime.now() #Me da la fecha de hoy
            if date_obj < hoy:
                flash('La fecha debe ser en futuro', 'appointments')
                es_valido = False
        
        
        if formulario['status'] == '':
            flash('status cannot be empty', 'appointments')
            es_valido = False
        
        return es_valido

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO appointments (task, date, status, user_id) VALUES (%(task)s, %(date)s, %(status)s,%(user_id)s)"
        result = connectToMySQL('appointments').query_db(query, formulario)
        return result
    

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM appointments"
        results = connectToMySQL('appointments').query_db(query) #Lista de Diccionarios
        appointments = []

        for appointment in results:
            appointments.append(cls(appointment)) #1.- cls(grade) crea una instancia en base al diccionario. 2.- grades.append() me agrega esa instancia a mi lista
        
        return appointments

    @classmethod
    def get_by_id(cls, formulario):
        query = "SELECT * FROM appointments WHERE id = %(id)s"
        result = connectToMySQL('appointments').query_db(query, formulario)
        appointment = cls(result[0])
        return appointment
    
    @classmethod
    def update(cls, formulario):
        query = "UPDATE appointments SET task=%(task)s, date=%(date)s, status=%(status)s, user_id=%(user_id)s"
        result = connectToMySQL('appointments').query_db(query, formulario)
        return result
    

    @classmethod
    def delete(cls, formulario):
        query = "DELETE FROM appointments WHERE id = %(id)s"
        result = connectToMySQL('appointments').query_db(query, formulario)
        return result