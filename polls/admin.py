from django.contrib import admin

# Register your models here

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4
admin.site.register(Choice)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    search_fields = ['question_text']
    list_filter = ['pub_date']	

#, 'op1','op2','op3','op4'
admin.site.register(Question, QuestionAdmin)





