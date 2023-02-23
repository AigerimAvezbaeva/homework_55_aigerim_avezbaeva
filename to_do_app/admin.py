from django.contrib import admin

from to_do_app.models import ToDoParagraph


# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status')
    list_filter = ('id', 'title', 'status', 'completion_date')
    search_fields = ('title', 'status')
    list_editable = ['status']


admin.site.register(ToDoParagraph, TodoAdmin)
