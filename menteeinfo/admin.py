from django.contrib import admin

# from import_export.admin import ImportExportModelAdmin
from .models import Registration
# Register your models here.
# admin.site.register(Mentee)
# admin.site.register(Mentor)
# admin.site.register(temp)
admin.site.register(Registration)
# class MentorAdmin(ImportExportModelAdmin):
#     list_display = ('id', 'rollno', 'department', 'degree', 'graduation_year', 'workprofile', 'company', 'experience', 'field', 'specialization')
