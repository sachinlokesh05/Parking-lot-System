from django_mongoengine import mongo_admin as admin
from .models import User

@admin.register(User)
class BlogPostAdmin(admin.DocumentAdmin):
    pass