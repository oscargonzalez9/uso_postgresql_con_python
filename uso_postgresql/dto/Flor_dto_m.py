from marshmallow import Schema, fields

class Flor_schema(Schema):
    nombre = fields.Str()
    color = fields.Str()
    genero = fields.Str()
    especie = fields.Str()