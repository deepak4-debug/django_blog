from django.contrib import admin
from .models import Post,UserProfile, Basic, ControlFlow
#from django_summernote.admin import SummernoteModelAdmin

'''
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Post, PostAdmin)

#....directly register to admin site
@admin.register(Comment)

#Customizing the admin area for Comment Model
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']
    
    
    def approve_comments(self, request, queryset):
        queryset.update(active=True)
    
    #def approve_comments(self):
     #   return self.**comments**.filter(approved_comment=True)
'''



""" class PostAdmin(SummernoteModelAdmin):
    list_display = ('title','status', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ['title', 'content']
    
    summernote_fields = ('content',) """
    
    
class PostAdmin(admin.ModelAdmin):
        list_display = ('title','status', 'created_on')
        list_filter = ('status', 'created_on')
        search_fields = ['title', 'content']

admin.site.register(Post, PostAdmin)

'''
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
'''

admin.site.register(UserProfile)
#class SummerAdmin(SummernoteModelAdmin):
   # summernote_fields = ('content',)
   
   
   
""" class BasicAdmin(SummernoteModelAdmin):
    list_display = ('title',)
    summernote_fields = ('basic_programming', 'numbers', 'string', 'basic_list') """
    
class BasicAdmin(admin.ModelAdmin):
        list_display = ('title',)

admin.site.register(Basic, BasicAdmin)


""" class ControlFlowAdmin(SummernoteModelAdmin):
    list_display = ('title',)
    summernote_fields = ('if_Statements', 'for_Statements', 'range_Function', 'break_and_continue_Statements', 'pass_Statements')
 """
 
class ControlFlowAdmin(admin.ModelAdmin):
        list_display = ('title',)
 
admin.site.register(ControlFlow, ControlFlowAdmin)

