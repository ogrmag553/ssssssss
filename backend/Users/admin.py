from django.contrib import admin
from .models import Category,Tag,Post,Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin)
    list_display =['name','description']

@admin.register(Tag)   
class TagAdmin(admin.ModelAdmin):
    list_display = ['name'] 

@admin.register(Post) 
class PostAdmin(admin.ModelAdmin):
    list_display =['titell','autor','category','create_ar'] 
    list_filter = ['tag','create_ar','category']  
    list_fields = ['titell','comment']
    
