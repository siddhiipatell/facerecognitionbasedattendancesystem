from django.contrib import admin
from .models import Contact, Department, Semester, Gender, F_login, S_Login, F_Registration, S_registration, S_code, F_code, Subject

admin.site.register(Contact)
admin.site.register(Department)
admin.site.register(Gender)
admin.site.register(Semester)
admin.site.register(F_login)
admin.site.register(S_Login)
admin.site.register(F_Registration)
admin.site.register(S_registration)
admin.site.register(F_code)
admin.site.register(S_code)
admin.site.register(Subject)
