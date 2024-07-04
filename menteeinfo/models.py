# from django.db import models
# from .options import *

# # Create your models here.
# class Mentee(models.Model):
# 	id = models.AutoField(primary_key = True)
# 	full_name = models.CharField(max_length = 255, null=True)
# 	roll_no = models.CharField(max_length = 9, null=True)
# 	department = models.CharField(max_length = 255, null=True)
# 	dept_other = models.CharField(max_length = 255, null=True)
# 	degree = models.CharField(max_length=255, null=True)
# 	degree_other = models.CharField(max_length=  255, null=True)
# 	contact_number = models.CharField(max_length = 12, null=True)
# 	email_id = models.CharField(max_length = 255, null=True)
# 	SOP = models.TextField(null=True)
# 	suggestion = models.TextField(null=True)

# 	preference_1 = models.CharField(max_length = 10, null=True)
# 	preference_2 = models.CharField(max_length = 10, null=True)
# 	preference_3 = models.CharField(max_length = 10, null=True)
# 	preference_4 = models.CharField(max_length = 10, null=True)
# 	preference_5 = models.CharField(max_length = 10, null=True)
	
# #mentor data
# class Mentor(models.Model):
# 	id = models.AutoField(primary_key=True)
# 	rollno=models.CharField(max_length=9, null=True)
# 	department=models.CharField( max_length=255, null=True)
# 	degree=models.CharField( max_length=255, null=True)
# 	graduation_year=models.CharField( max_length=10, null=True)
# 	workprofile=models.CharField( max_length=255, null=True)
# 	company=models.CharField( max_length=255, null=True)
# 	experience=models.CharField(max_length=350, null=True)
# 	field = models.CharField(max_length=10, null=True)
# 	specialization = models.CharField(max_length= 100, null=True)
# 	hits = models.IntegerField(default = 0, null=True)
# 	gray_out = models.CharField(max_length = 1000, default = 1, null=True)

# class gradMentor(models.Model):
# 	id = models.AutoField(primary_key=True)
# 	rollno=models.CharField(max_length=9, null=True)
# 	department=models.CharField( max_length=255, null=True)
# 	degree=models.CharField( max_length=255, null=True)
# 	graduation_year=models.CharField( max_length=10, null=True)
# 	university=models.CharField( max_length=255, null=True)
# 	subject=models.CharField( max_length=255, null=True)
# 	experience=models.CharField(max_length=350, null=True)
# 	field = models.CharField(max_length=10, null=True)
	
# # #temp to check preferences
# # class temp(models.Model):
# # 	preference_1 = models.CharField(max_length = 10)
# # 	preference_2 = models.CharField(max_length = 10)
# # 	preference_3 = models.CharField(max_length = 10)
# # 	preference_4 = models.CharField(max_length = 10)
# # 	preference_5 = models.CharField(max_length = 10)

# class Registration(models.Model):
#     id=models.AutoField(primary_key=True)
#     fullname=models.CharField( max_length=255)
#     rollno=models.CharField(max_length=9)
#     department=models.CharField( max_length=255, choices=BRANCH_CHOICES)
#     department_other=models.CharField(max_length=255, blank=True, null=True)
#     degree=models.CharField( max_length=255, choices=DEGREE_CHOICES)
#     degree_other=models.CharField( max_length=255, blank=True, null=True)
#     graduation_year=models.CharField( max_length=50)
#     graduation_year = models.IntegerField(blank=True)
#     experience=models.TextField(blank=True)
#     contact=models.CharField( max_length=12)
#     email=models.EmailField(blank=True)

#     placementOrGrad = models.CharField(max_length=255, choices=OPTIONS, null=True)

#     designation=models.CharField(max_length=255, blank=True)
#     company_name=models.CharField(max_length=255, blank=True)
#     experience=models.TextField(blank=True)
#     field_pref1 = models.CharField(max_length=255, choices=PLACEMENT_FIELDS, null=True)
#     field_pref2 = models.CharField(max_length=255, choices=PLACEMENT_FIELDS, null=True)
#     field_pref3 = models.CharField(max_length=255, choices=PLACEMENT_FIELDS, null=True)    
#     university_name=models.CharField(max_length=255, blank=True, null=True)    
#     branch = models.CharField(max_length=255, choices=BRANCH_CHOICES, null=True)
#     branch_subdivision = models.CharField(max_length=255, blank=True, null=True)    
#     preferred_mentees = models.IntegerField(null=True)
#     suggestions=models.TextField(blank=True, null=True)
#     alumni_recommendations = models.TextField(blank=True, null=True)

#     no_of_mentees=models.CharField(max_length=255, default="None", blank=True, null=True)
#     referral=models.CharField(max_length=255, default="None", blank=True, null=True)
#     profiles=models.CharField(max_length=255, default="None", blank=True, null=True)
#     pref1=models.CharField(max_length=255, default="None", blank=True, null=True)
#     pref2=models.CharField(max_length=255, default="None", blank=True, null=True)
#     core=models.CharField(max_length=100, default="None", blank=True, null=True)
#     # aerospace = models.CharField(max_length=100, default="None", blank=True, null=True)
#     # chemical = models.CharField(max_length=100, default="None", blank=True, null=True)
#     # bsbe = models.CharField(max_length=100, default="None", blank=True, null=True)
#     # earthscience = models.CharField(max_length=100, default="None", blank=True, null=True)
#     # ep = models.CharField(max_length=100, default="None", blank=True, null=True)
#     # mems = models.CharField(max_length=100, default="None", blank=True, null=True)
#     # maths = models.CharField(max_length=100, default="None", blank=True, null=True)
#     # ieor = models.CharField(max_length=100, default="None", blank=True, null=True)
#     # civil = models.CharField(max_length=100, default="None", blank=True, null=True)
#     # chemistry = models.CharField(max_length=100, default="None", blank=True, null=True)
#     # electrical = models.CharField(max_length=100, default="None", blank=True, null=True)
#     # energy = models.CharField(max_length=100, default="None", blank=True, null=True)
#     # mechanical = models.CharField(max_length=100, default="None", blank=True, null=True)
#     # other_mentorship=models.CharField(max_length=100, default="None", blank=True, null=True)
#     # other_department = models.CharField(max_length=100, default="None", blank=True, null=True)

#     def __str__(self):
#         return self.fullname
#         # +"_"+self.field_pref1


from django.db import models
from .options import *

# Create your models here.
class Mentee(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255, null=True)
    roll_no = models.CharField(max_length=9, null=True)
    department = models.CharField(max_length=255, null=True)
    dept_other = models.CharField(max_length=255, null=True)
    degree = models.CharField(max_length=255, null=True)
    degree_other = models.CharField(max_length=255, null=True)
    contact_number = models.CharField(max_length=12, null=True)
    email_id = models.CharField(max_length=255, null=True)
    preference_1 = models.CharField(max_length=10, null=True)
    preference_2 = models.CharField(max_length=10, null=True)
    preference_3 = models.CharField(max_length=10, null=True)
    preference_4 = models.CharField(max_length=10, null=True)
    preference_5 = models.CharField(max_length=10, null=True)
    SOP = models.TextField(null=True)
    suggestion = models.TextField(null=True)
	
#mentor data
class Mentor(models.Model):
    id = models.AutoField(primary_key=True)
    rollno = models.CharField(max_length=9, null=True)
    department = models.CharField(max_length=255, null=True)
    degree = models.CharField(max_length=255, null=True)
    graduation_year = models.CharField(max_length=10, null=True)
    experience = models.CharField(max_length=350, null=True)
    field = models.CharField(max_length=10, null=True)
    specialization = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=10, null=True)  # 'placement' or 'grad'
    
    # Exclusive to 'placement'
    workprofile = models.CharField(max_length=255, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    
    # Exclusive to 'grad'
    university = models.CharField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)

	# hits = models.IntegerField(default = 0, null=True)
	# gray_out = models.CharField(max_length = 1000, default = 1, null=True)

# class gradMentor(models.Model):
# 	id = models.AutoField(primary_key=True)
# 	rollno=models.CharField(max_length=9, null=True)
# 	department=models.CharField( max_length=255, null=True)
# 	degree=models.CharField( max_length=255, null=True)
# 	graduation_year=models.CharField( max_length=10, null=True)
# 	university=models.CharField( max_length=255, null=True)
# 	subject=models.CharField( max_length=255, null=True)
# 	experience=models.CharField(max_length=350, null=True)
# 	field = models.CharField(max_length=10, null=True)
	
# #temp to check preferences
# class temp(models.Model):
# 	preference_1 = models.CharField(max_length = 10)
# 	preference_2 = models.CharField(max_length = 10)
# 	preference_3 = models.CharField(max_length = 10)
# 	preference_4 = models.CharField(max_length = 10)
# 	preference_5 = models.CharField(max_length = 10)

# class Registration(models.Model):
#     id=models.AutoField(primary_key=True)
#     fullname=models.CharField( max_length=255)
#     rollno=models.CharField(max_length=9)
#     department=models.CharField( max_length=255, choices=BRANCH_CHOICES)
#     department_other=models.CharField(max_length=255, blank=True, null=True)
#     degree=models.CharField( max_length=255, choices=DEGREE_CHOICES)
#     degree_other=models.CharField( max_length=255, blank=True, null=True)
#     graduation_year=models.CharField( max_length=50)
#     graduation_year = models.IntegerField(blank=True)
#     experience=models.TextField(blank=True)
#     contact=models.CharField( max_length=12)
#     email=models.EmailField(blank=True)

#     placementOrGrad = models.CharField(max_length=255, choices=OPTIONS, null=True)

#     designation=models.CharField(max_length=255, blank=True)
#     company_name=models.CharField(max_length=255, blank=True)
#     experience=models.TextField(blank=True)
#     field_pref1 = models.CharField(max_length=255, choices=PLACEMENT_FIELDS, null=True)
#     field_pref2 = models.CharField(max_length=255, choices=PLACEMENT_FIELDS, null=True)
#     field_pref3 = models.CharField(max_length=255, choices=PLACEMENT_FIELDS, null=True)    
#     university_name=models.CharField(max_length=255, blank=True, null=True)    
#     branch = models.CharField(max_length=255, choices=BRANCH_CHOICES, null=True)
#     branch_subdivision = models.CharField(max_length=255, blank=True, null=True)    
#     preferred_mentees = models.IntegerField(null=True)
#     suggestions=models.TextField(blank=True, null=True)
#     alumni_recommendations = models.TextField(blank=True, null=True)

#     no_of_mentees=models.CharField(max_length=255, default="None", blank=True, null=True)
#     referral=models.CharField(max_length=255, default="None", blank=True, null=True)
#     profiles=models.CharField(max_length=255, default="None", blank=True, null=True)
#     pref1=models.CharField(max_length=255, default="None", blank=True, null=True)
#     pref2=models.CharField(max_length=255, default="None", blank=True, null=True)
#     core=models.CharField(max_length=100, default="None", blank=True, null=True)
    # aerospace = models.CharField(max_length=100, default="None", blank=True, null=True)
    # chemical = models.CharField(max_length=100, default="None", blank=True, null=True)
    # bsbe = models.CharField(max_length=100, default="None", blank=True, null=True)
    # earthscience = models.CharField(max_length=100, default="None", blank=True, null=True)
    # ep = models.CharField(max_length=100, default="None", blank=True, null=True)
    # mems = models.CharField(max_length=100, default="None", blank=True, null=True)
    # maths = models.CharField(max_length=100, default="None", blank=True, null=True)
    # ieor = models.CharField(max_length=100, default="None", blank=True, null=True)
    # civil = models.CharField(max_length=100, default="None", blank=True, null=True)
    # chemistry = models.CharField(max_length=100, default="None", blank=True, null=True)
    # electrical = models.CharField(max_length=100, default="None", blank=True, null=True)
    # energy = models.CharField(max_length=100, default="None", blank=True, null=True)
    # mechanical = models.CharField(max_length=100, default="None", blank=True, null=True)
    # other_mentorship=models.CharField(max_length=100, default="None", blank=True, null=True)
    # other_department = models.CharField(max_length=100, default="None", blank=True, null=True)

    def _str_(self):
        return self.fullname
        # +"_"+self.field_pref1