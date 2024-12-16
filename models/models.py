# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, date

#Definimos el modelo de datos
class autoescuela(models.Model):
# Nombre y descripcion del modelo de datos
    _name = 'autoescuela.autoescuela'
    _description = 'autoescuela.autoescuela'

    name = fields.Char()
    domicilio = fields.Char()
    localidad = fields.Char()
    provincia = fields.Char()
    examen_ids = fields.Many2many()
    profesor_ids = fields.One2many()
    alumno_ids = fields.One2many()
    contacto = fields.Char()
# value = fields.Integer()
# value2 = fields.Float(compute="_value_pc", store=True)
# description = fields.Text()
#
# @api.depends('value')
# def _value_pc(self):
# for record in self:
# record.value2 = float(record.value) / 100

#Definimos el modelo de datos
class profesor(models.Model):
# Nombre y descripcion del modelo de datos
    _name = 'autoescuela.profesor'
    _description = 'autoescuela.autoescuela'
    name = fields.Char(required=True)
    dni= fields.Char(required=True)
    coche = fields.Char()
    matricula = fields.Char()
    autoescuela_id = fields.Many2one()
    incorporacion = fields.Date()
    antiguedad = fields.Integer(compute = "calcular_antiguedad", store = True)
    alumno_ids = fields.One2many()
    @api.depends('incorporacion') 
    def calcular_antiguedad(self):
        for record in self:
            fecha = date.today()
            record.antiguedad = fecha.years - record.incorporacion.years 

#Definimos el modelo de datos
class alumno(models.Model):
# Nombre y descripcion del modelo de datos
    _name = 'autoescuela.alumno'
    _description = 'autoescuela.autoescuela'
    name = fields.Char(required=True)
    dni = fields.Char(required=True)
    autoescuela_id = fields.Many2one()
    profesor_id = fields.Many2one()
    examenes_ids = fields.One2many()
    domicilio = fields.Char()
    matricula = fields.Char()

#Definimos la clase examen
class examen(models.Model):
# Nombre y descripcion del modelo de datos
    _name = 'examen.autoescuela'
    _description = 'autoescuela.autoescuela'
    name = fields.Char(compute = "create", store = True)
    fecha = fields.Date()
    autoescuela_ids = fields.Many2many()
    alumno_id = fields.Many2one(required= True)
    moneda_id= fields.Many2one('res.currency', string="Moneda")
    precio = fields.Float() # en el enunciado de la practica pone tipo Monetary pero da fallo
    clases= fields.Integer()
    carnet = fields.Char(required=True, help="AM = Ciclomotores (hasta 50 cc), \
    A1 = Motocicletas (potencia máxima 11 KW), \
    A2 = Motocicletas (potencia máxima 35 KW), \
    A = Motocicletas y triciclos de motor, \
    B = Automóviles (MMA hasta 3.500 kg)")
    aprobado = fields.Boolean()

#Pag 10 - se incluye la funcionalidad para generar la secuencia para el código de examen
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name',_('Autogenerado')) == _('Autogenerado'):
                vals['name'] = (self.env['ir.sequence'].
                next_by_code('autoescuela.examen'))
    #Definimos el modelo de datos
class autoescuela_examen(models.Model):
    # Nombre y descripcion del modelo de datos
    _name = 'autoescuela.autoescuela_examen'
    _description = 'autoescuela.autoescuela'
    examen_ids = fields.Many2many()
    autoescuela_ids = fields.Many2many()


