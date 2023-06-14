from django.contrib import admin
from .models import PnuUser, Question, Answer
# Register your models here.
admin.site.register(PnuUser)
admin.site.register(Question)
admin.site.register(Answer)