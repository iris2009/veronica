#shit

# Register your models here.
from django.contrib import admin
from app.models import Book,Author

class BookAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Book)
admin.site.register(Author)
