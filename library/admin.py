from django.contrib import admin
from .models import Book,StudentExtra,IssuedBook,Events
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)


class StudentExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentExtra, StudentExtraAdmin)


class IssuedBookAdmin(admin.ModelAdmin):
    pass
admin.site.register(IssuedBook, IssuedBookAdmin)


class EventsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Events, EventsAdmin)
