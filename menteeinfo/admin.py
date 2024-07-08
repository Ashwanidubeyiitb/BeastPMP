from django.contrib import admin
from .forms import MentorAdminForm
# from import_export.admin import ImportExportModelAdmin
from .models import Mentee, Mentor, Registration

# Register your models here.

admin.site.register(Mentee)
# admin.site.register(Mentor)
# admin.site.register(gradMentor)
# admin.site.register(temp)


# class MentorAdmin(ImportExportModelAdmin):
#     list_display = ('id', 'rollno', 'department', 'degree', 'graduation_year', 'workprofile', 'company', 'experience', 'field', 'specialization')

class Mentee():
    list_display = ('id', 'full_name', 'rollno', 'department', 'dept_other', 'degree', 'degree_other', 'contact_number', 'email_id', 'SOP', 'suggestion', 'preference_1', 'preference_2', 'preference_3', 'preference_4', 'preference_5')


class MentorAdmin(admin.ModelAdmin):
    form = MentorAdminForm

admin.site.register(Mentor, MentorAdmin)
admin.site.register(Registration)