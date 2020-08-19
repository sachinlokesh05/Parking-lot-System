from django_mongoengine import fields
from django_mongoengine import Document, EmbeddedDocument
from django_mongoengine.mongo_auth.models import User

class User(User):
    roles = (
        ('driver','driver'),
        ('police','police'),
        ('owner','owner')
    )
    role = fields.StringField(
        require = True,
        default = 'driver',
        choices = roles
    )

    # meta ={
    #         'allow_inheritance': True
    # }