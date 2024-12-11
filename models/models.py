# -*- coding: utf-8 -*-

 from odoo import models, fields, api

#Definimos el modelo de datos
class autoescuela(models.Model):
    # Nombre y descripcion del modelo de datos
     _name = 'autoescuela.autoescuela'
     _description = 'autoescuela.autoescuela'

     name = fields.Char()
     domicilio = fields.Char()
     localidad = fields.Char()
     provincia = fields.Char()
     examen_ids = fields.M2M()
     profesor_ids = fields.O2M()
     alumno_ids = fields.O2M()
     contacto = fields.Char()
     
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

#Definimos el modelo de datos
class profesor(models.Model):
    # Nombre y descripcion del modelo de datos
     _name = 'autoescuela.profesor'
     _description = 'autoescuela.autoescuela'


#Definimos el modelo de datos
class alumno(models.Model):
    # Nombre y descripcion del modelo de datos
     _name = 'autoescuela.alumno'
     _description = 'autoescuela.autoescuela'


#Definimos la clase examen
class examen(models.Model):
    # Nombre y descripcion del modelo de datos
     _name = 'examen.autoescuela'
     _description = 'autoescuela.autoescuela'
     
     precio = fields.Float()    # en el enunciado de la practica pone tipo Monetary pero da fallo

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

