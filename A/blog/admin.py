from django.contrib import admin
from .models import Article

# admin.site.register(Article,BlogAdmin)
@admin.register(Article)
class BlogAdmin(admin.ModelAdmin):
    list_display=('title','publish','writer','status')
    list_editable=('status',)
    list_filter=('status','writer','publish')
    search_fields=('title','body')
    raw_id_fields=('writer',)
    prepopulated_fields={'slug':('title',)}
    

    



# Register your models here.
