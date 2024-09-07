from django.contrib import admin
from .models import Answer, AnswerDetail, Option, Question, Quiz

# Register your models here.
admin.site.register(Answer)
admin.site.register(AnswerDetail)
admin.site.register(Option)
admin.site.register(Question)
admin.site.register(Quiz)
