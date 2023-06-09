from django.db import models
from .options import *

# Create your models here.
# class Mentee(models.Model):
# 	# id = models.AutoField(primary_key = True)
# 	full_name = models.CharField(max_length = 255, null=True)
# 	roll_no = models.CharField(max_length = 9, null=True)
# 	department = models.CharField(max_length = 255, null=True)
# 	degree = models.CharField(max_length=255, null=True)
# 	degree_other = models.CharField(max_length=  255, null=True)
# 	contact_number = models.CharField(max_length = 12, null=True)
# 	email_id = models.CharField(max_length = 255, null=True)
# 	preference_1 = models.CharField(max_length = 10, null=True)
# 	preference_2 = models.CharField(max_length = 10, null=True)
# 	preference_3 = models.CharField(max_length = 10, null=True)
# 	preference_4 = models.CharField(max_length = 10, null=True)
# 	preference_5 = models.CharField(max_length = 10, null=True)
# 	SOP = models.TextField(null=True)
# 	suggestion = models.TextField(null=True)
	
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
# 	# hits = models.IntegerField(default = 0, null=True)
# 	# gray_out = models.CharField(max_length = 1000, default = 1, null=True)

# #temp to check preferences
# class temp(models.Model):
# 	preference_1 = models.CharField(max_length = 10)
# 	preference_2 = models.CharField(max_length = 10)
# 	preference_3 = models.CharField(max_length = 10)
# 	preference_4 = models.CharField(max_length = 10)
# 	preference_5 = models.CharField(max_length = 10)

class Registration(models.Model):

    id=models.AutoField(primary_key=True)
    fullname=models.CharField( max_length=255)
    rollno=models.CharField(max_length=9)
    department=models.CharField( max_length=255, choices=BRANCH_CHOICES)
    department_other=models.CharField(max_length=255, blank=True, null=True)
    degree=models.CharField( max_length=255, choices=DEGREE_CHOICES)
    degree_other=models.CharField( max_length=255, blank=True, null=True)
    # graduation_year=models.CharField( max_length=10)
    graduation_year = models.IntegerField()
    experience=models.TextField()
    contact=models.CharField( max_length=12)
    email=models.CharField(max_length=255)
    
    placementOrGrad = models.CharField(max_length=255, choices=OPTIONS)
    
    
    designation=models.CharField(max_length=255, blank=True)
    company_name=models.CharField(max_length=255, blank=True)
    experience=models.TextField()
    
    
    field_pref1 = models.CharField(max_length=255, choices=PLACEMENT_FIELDS, null=True)
    field_pref2 = models.CharField(max_length=255, choices=PLACEMENT_FIELDS, null=True)
    field_pref3 = models.CharField(max_length=255, choices=PLACEMENT_FIELDS, null=True)
    

    
    university_name=models.CharField(max_length=255, blank=True, null=True)

    
    branch = models.CharField(max_length=255, choices=BRANCH_CHOICES, null=True)
    branch_subdivision = models.CharField(max_length=255, blank=True, null=True)

    
    preferred_mentees = models.IntegerField(null=True)
    
    suggestions=models.TextField(blank=True, null=True)
    
    alumni_recommendations = models.TextField(blank=True, null=True)

    # no_of_mentees=models.CharField(max_length=255)
    # referral=models.CharField(max_length=255)
    # profiles=models.CharField(max_length=255)
    # pref1=models.CharField(max_length=255)
    # pref2=models.CharField(max_length=255)
    # core=models.CharField(max_length=100)
    # aerospace = models.CharField(max_length=100)
    # chemical = models.CharField(max_length=100)
    # bsbe = models.CharField(max_length=100)
    # earthscience = models.CharField(max_length=100)
    # ep = models.CharField(max_length=100)
    # mems = models.CharField(max_length=100)
    # maths = models.CharField(max_length=100)
    # ieor = models.CharField(max_length=100)
    # civil = models.CharField(max_length=100)
    # chemistry = models.CharField(max_length=100)
    # electrical = models.CharField(max_length=100)
    # energy = models.CharField(max_length=100)
    # mechanical = models.CharField(max_length=100)
    # other_mentorship=models.CharField(max_length=100)
    # other_department = models.CharField(max_length=100, default="None")

    def __str__(self):
        return self.fullname+"_"+self.field_pref1
