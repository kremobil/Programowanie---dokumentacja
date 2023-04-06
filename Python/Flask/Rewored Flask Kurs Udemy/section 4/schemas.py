from marshmallow import Schema, fields


class ItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Str()

class StoreSchema(Schema):
    store_name = fields.Str(required=True)
    id = fields.Str(dump_only=True)

class StoreDeleteSchema(Schema):
    message = fields.Str(dump_only=True)
    store = fields.Dict(dump_only=True)

class ItemDeleteSchema(Schema):
    message = fields.Str(dump_only=True)
    item = fields.Dict(dump_only=True)