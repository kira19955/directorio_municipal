# -*- coding: utf-8 -*-
from odoo import models, fields, api


class directorio_municipal(models.Model):
    _name = 'directorio_municipal.directorio_municipal'
    _rec_name ="nombre_area"
    _order = "orden_dependencia asc"


    nivel = fields.Selection(selection=
         [('direccion', 'Direccion'),
         ('subdirec','Subdireccion'),
         ('depart','Departamento'),
         ('unidad','Unidad'),
         ('coordinacion','Coordinacion'),
         ('secretaria','Secretaria'),
         ('tesoreria','Tesoreria'),
         ('cabildo','Cabildo'),
         ('sindicatura','Sindicatura'),
         ('presidencia','Presidencia'),
         ('sipinna','Sipinna'),
         ('otro_nivel','Otro'),
         ('opd','Organismo Público Descentralizado'),], string ="Nivel de dependencia", required=True)
     
    nombre_area = fields.Char(string="Nombre del área",required=True)
    prefijo_titular = fields.Char(string="Prefijo del titular")
    nombre_titular = fields.Char(string="Nombre: ",required=True)
    ubicacion_oficina = fields.Char(string="Ubicación",required=True)
    telefono_area = fields.Char(string="Teléfono del aréa", required=True)
    correo_area = fields.Char(string="Correo eléctronico", required=True)     
    depende_superior = fields.Many2one(comodel_name='directorio_municipal.directorio_municipal', string="Depende de: ")
    address = fields.Char(string="Dirección")
    siglas = fields.Char(string="Siglas")
    orden_dependencia = fields.Float(string="Orden",default=99)