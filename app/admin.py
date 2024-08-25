from django.contrib import admin
from .models import Answer, AnswerDetail, Option, Question, QuestionSet, Quiz

# Register your models here.
admin.site.register(Answer)
admin.site.register(AnswerDetail)
admin.site.register(Option)
admin.site.register(Question)
admin.site.register(QuestionSet)
admin.site.register(Quiz)
