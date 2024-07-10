from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mentee, Mentor, Registration
from django.core.exceptions import ValidationError
from django.db.models import F  # Import F from django.db.models
import csv
from rest_framework.decorators import api_view
from .options import *

def mentor_create_view(request, mentor_id):
    mentor = Mentor.objects.get(id=mentor_id)
    saved_field_value = mentor.field
    return render(request, 'change_form.html', {'saved_field_value': saved_field_value})

# Mentee registration
def register(request):
    corementors = Mentor.objects.filter(field="Core", type="placement", hits__lt=F('gray_out'))
    Corementors = Mentor.objects.filter(field="core", type="placement", hits__lt=F('gray_out'))
    consultmentors = Mentor.objects.filter(field="Consultancy", type="placement", hits__lt=F('gray_out'))
    Consultmentors = Mentor.objects.filter(field="consultancy", type="placement", hits__lt=F('gray_out'))
    consulting = Mentor.objects.filter(field="consulting", type="placement", hits__lt=F('gray_out'))
    analyticmentors = Mentor.objects.filter(field="Analytics", type="placement", hits__lt=F('gray_out'))
    finmentors = Mentor.objects.filter(field="Finance", type="placement", hits__lt=F('gray_out'))
    finance = Mentor.objects.filter(field="finance", type="placement", hits__lt=F('gray_out'))
    csmentor = Mentor.objects.filter(field="IT/Software", type="placement", hits__lt=F('gray_out'))
    othermentors = Mentor.objects.filter(field="other", type="placement", hits__lt=F('gray_out'))
    Othermentors = Mentor.objects.filter(field="Other", type="placement", hits__lt=F('gray_out'))
    Othersmentors = Mentor.objects.filter(field="Others", type="placement", hits__lt=F('gray_out'))
    chutiya = Mentor.objects.filter(field="FMCG(product management)", type="placement", hits__lt=F('gray_out'))
    fmcg = Mentor.objects.filter(field="FMCG", type="placement", hits__lt=F('gray_out'))
    bhadwa = Mentor.objects.filter(field="analytics", type="placement", hits__lt=F('gray_out'))
    corecontrol = Mentor.objects.filter(field="Mechanical(core control)", type="placement", hits__lt=F('gray_out'))
    itsoftwar = Mentor.objects.filter(field="it_software", type="placement", hits__lt=F('gray_out'))

    CorementorsGrad = Mentor.objects.filter(field="core", type="grad", hits__lt=F('gray_out'))
    corementorsGrad = Mentor.objects.filter(field="Core", type="grad", hits__lt=F('gray_out'))
    managementmentorsGrad = Mentor.objects.filter(field="management", type="grad", hits__lt=F('gray_out'))
    ManagementmentorsGrad = Mentor.objects.filter(field="Management", type="grad", hits__lt=F('gray_out'))

    context = {
        'mentors_list_core': corementors,
        'mentors_list_consult': consultmentors,
        'mentors_list_analysis': analyticmentors,
        'mentors_list_fin': finmentors,
        'mentors_list_cs': csmentor,
        'mentors_list_other': othermentors,
        'mentors_list_fmcg': fmcg,
        'mentors_list_Core': Corementors,
        'mentors_list_Other': Othermentors,
        'mentors_list_Others': Othersmentors,
        'mentors_list_chutiya': chutiya,
        'bhadwa': bhadwa,
        'corecontrol': corecontrol,
        'Consultmentors': Consultmentors,
        'consulting': consulting,
        'finance': finance,
        'itsoftwar': itsoftwar,
        'mentors_core': corementorsGrad,
        'mentors_Core': CorementorsGrad,
        'mentors_management': managementmentorsGrad,
        'mentors_Management': ManagementmentorsGrad,
    }

    return render(request, "menteeinfo/register.html", context)

def menteereg(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        roll_no = request.POST.get('roll_no')
        department = request.POST.get('department')
        dept_other = request.POST.get('dept_other')
        degree = request.POST.get('degree')
        degree_other = request.POST.get('degree_other')
        contact_number = request.POST.get('contact_number')
        email_id = request.POST.get('email_id')
        preference_1 = request.POST.get('preference_1')
        preference_2 = request.POST.get('preference_2')
        preference_3 = request.POST.get('preference_3')
        preference_4 = request.POST.get('preference_4')
        preference_5 = request.POST.get('preference_5')
        suggestion = request.POST.get('suggestion')
        SOP = request.POST.get('SOP')

        mentee = Mentee(
            full_name=full_name,
            roll_no=roll_no,
            department=department,
            dept_other=dept_other,
            degree=degree,
            degree_other=degree_other,
            contact_number=contact_number,
            email_id=email_id,
            preference_1=preference_1,
            preference_2=preference_2,
            preference_3=preference_3,
            preference_4=preference_4,
            preference_5=preference_5,
            suggestion=suggestion,
            SOP=SOP
        )
        mentee.save()
        context = {}
    return render(request, 'menteeinfo/register_success.html', context)

def export(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow([
        'Fullname',
        'Roll No',
        'Department',
        'Other department',
        'degree',
        'Other Degree',
        'Graduation Year',
        'Contact',
        'Email',
        'Option',
        'Designation',
        'Company Name',
        'University Name',
        'experience',
        'Preference 1',
        'Preference 2',
        'Preference 3',
        'Core',
        'Core Subdivision',
        'Preferred mentees',
        'Suggestions',
        'Recommendations',
    ])
    for registration in Registration.objects.all().values_list(
        'fullname',
        'rollno',
        'department',
        'department_other',
        'degree',
        'degree_other',
        'graduation_year',
        'contact',
        'email',
        'placementOrGrad',
        'designation',
        'company_name',
        'university_name',
        'experience',
        'field_pref1',
        'field_pref2',
        'field_pref3',
        'branch',
        'branch_subdivision',
        'preferred_mentees',
        'suggestions',
        'alumni_recommendations'
    ):
        writer.writerow(registration)

    response['Content-Disposition'] = 'attachment; filename="mentors_pmp23.csv"'
    return response

def index(request):
    return render(request, 'menteeinfo/home.html')

def phonehome(request):
    return render(request, 'menteeinfo/phonehome.html')

def mentorReg(request):
    def __str__(self):
        return self.fullname

    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        rollno = request.POST.get('rollno')
        department = request.POST.get('department')
        department_other = request.POST.get('other_department')
        degree = request.POST.get('degree')
        degree_other = request.POST.get('degree_other')
        graduation_year = request.POST.get('graduation_year')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        placementOrGrad = request.POST.get('placementOrGrad')

        field_pref3 = "NA"

        if placementOrGrad == 'placement':
            experience = request.POST.get('placementExperience')
            field_pref1 = request.POST.get('placementPref1')
            field_pref2 = request.POST.get('placementPref2')
            field_pref3 = request.POST.get('placementPref3')
        else:
            experience = request.POST.get('gradExperience')
            field_pref1 = request.POST.get('gradPref1')
            field_pref2 = request.POST.get('gradPref2')

        designation = request.POST.get('designation')
        company_name = request.POST.get('company_name')
        university = request.POST.get('university_name')
        suggestions = request.POST.get('suggestion')
        recommendations = request.POST.get('referral')
        core_branch = request.POST.get('core')
        branch_subdivision = request.POST.get('subdivisions')

        print(branch_subdivision)

        preferred_mentees = request.POST.get('no_of_mentees')

        registration = Registration(
            fullname=fullname or "NA", email=email or "NA", department=department or "NA", rollno=rollno or "NA", department_other=department_other or "NA",
            degree=degree or "NA", degree_other=degree_other or "NA", graduation_year=graduation_year or "NA", field_pref3=field_pref3 or "NA",
            contact=contact or "NA", placementOrGrad=placementOrGrad or "NA", designation=designation or "NA", company_name=company_name or "NA",
            experience=experience or "NA", field_pref1=field_pref1 or "NA", field_pref2=field_pref2 or "NA", branch=(core_branch or "NA"), branch_subdivision=(branch_subdivision or "NA"),
            preferred_mentees=preferred_mentees or "NA", university_name=(university or "NA"), suggestions=suggestions or "NA", alumni_recommendations=recommendations or "NA"
        )

        registration.save()
        return render(request, 'menteeinfo/thank.html')

    context = {
        'options': OPTIONS,
    }

    return render(request, 'menteeinfo/form.html', context)

def thank(request):
    return render(request, 'menteeinfo/thank.html')

@api_view(['POST'])
def testapi(request):
    req_data = request.data
    alumni_id = req_data['id']
    duration = req_data['duration']
    context = {'alumni_id': alumni_id, 'duration': duration}
    return render(request, 'thank.html', context)







# # from django.shortcuts import render, redirect
# # from django.http import HttpResponse, response
# # from .models import Registration, Mentee, Mentor, gradMentor
# # from django.core.exceptions import ValidationError
# # import csv
# # from rest_framework.decorators import api_view
# # from . import options

# # # # from .resources import MentorResource
# # # # from django.contrib import messages
# # # # from tablib import Dataset

# # # # to upload excel file

# # # # def simple_upload(request):
# # # # 	if(request.method == 'POST'):
# # # # 		mentor_resource = MentorResource()
# # # # 		dataset = Dataset()
# # # # 		new_mentor = request.FILES['myfile']

# # # # 		if not new_mentor.name.endswith('xlsx'):
# # # # 			messages.info(request, 'wrong format')
# # # # 			return render(request, 'upload.html')
# # # # 		imported_data = dataset.load(new_mentor.read(), format = 'xlsx')
# # # # 		for data in imported_data:
# # # # 			value=Mentor(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9])
# # # # 			value.save()
# # # # 	return render(request, 'upload.html')


# # # # Create your views here.
# # # def index(request):
# # # 	return render(request, 'menteeinfo/index.html')

# # # Mentee registration
# # def register(request):
# #     corementors = Mentor.objects.filter(field="Core")
# #     Corementors = Mentor.objects.filter(field="core")
# #     consultmentors = Mentor.objects.filter(field="Consultancy")
# #     Consultmentors = Mentor.objects.filter(field="consultancy")
# #     consulting = Mentor.objects.filter(field="consulting")
# #     analyticmentors = Mentor.objects.filter(field="Analytics")
# #     finmentors = Mentor.objects.filter(field="Finance")
# #     finance = Mentor.objects.filter(field="finance")
# #     csmentor = Mentor.objects.filter(field="IT/Software")
# #     othermentors = Mentor.objects.filter(field="Other")
# #     Othermentors = Mentor.objects.filter(field="Other")
# #     Othersmentors = Mentor.objects.filter(field="Others")
# #     chutiya = Mentor.objects.filter(field="FMCG(product management")
# #     fmcg = Mentor.objects.filter(field="FMCG")
# #     bhadwa = Mentor.objects.filter(field="Analytics,")
# #     randi = Mentor.objects.filter(field="IT/Software,")
# #     corecontrol = Mentor.objects.filter(field="Mechanical(core control)")
# #     itsoftwar = Mentor.objects.filter(field="IT/Softwar")
# #     # allmentors_sorted = allmentors.order_by['gray_out']
# #     context = {
# #         'mentors_list_core': corementors, 
# #         'mentors_list_consult': consultmentors,
# #         'mentors_list_analysis': analyticmentors,
# #         'mentors_list_fin': finmentors,
# #         'mentors_list_cs': csmentor,
# #         'mentors_list_other': othermentors,
# #         'mentors_list_fmcg': fmcg,
# #         'mentors_list_Core': Corementors,
# #         'mentors_list_Other': Othermentors,
# #         'mentors_list_Others': Othersmentors,
# #         'mentors_list_chutiya': chutiya,
# #         'bhadwa': bhadwa,
# #         'randi': randi,
# #         'corecontrol': corecontrol,
# #         'Consultmentors': Consultmentors,
# #         'consulting': consulting,
# #         'finance': finance,
# #         'itsoftwar': itsoftwar,
# #     }

# #     # dict=[]
# #     # allmentors = Mentor.objects.all()
# #     # for mentor in allmentors:
# #     #     exp = mentor.experience
# #     #     explist = exp.split(",")
# #     #     dict[mentor.rollno] = explist
# #     # print (dict[183020060])

# #     return render(request, "menteeinfo/register.html", context)

# # # def mentorexp(request):
# # #     allmentors = Mentor.objects.all()
# # # 	for mentor in allmentors:
# # #     	exp = mentor.experience

# # def gradRegister(request):
# #     corementors = gradMentor.objects.filter(field="Core")
# #     Corementors = gradMentor.objects.filter(field="core")
# #     managementmentors = gradMentor.objects.filter(field="management")
# #     Managementmentors = gradMentor.objects.filter(field="Management")
# #     context = {
# #         'mentors_core': corementors,        
# #         'mentors_Core': Corementors,
# #         'mentors_management': managementmentors,        
# #         'mentors_Management': Managementmentors,
# #     }

# #     return render(request, "menteeinfo/register.html", context)

# # def menteereg(request):
# # 	if request.method == 'POST':
# # 		full_name = request.POST.get('full_name')
# # 		roll_no = request.POST.get('roll_no')
# # 		department = request.POST.get('department')
# # 		degree = request.POST.get('degree')
# # 		degree_other= request.POST.get('degree_other')
# # 		contact_number = request.POST.get('contact')
# # 		email_id = request.POST.get('email_id')
# # 		preference_1 = request.POST.get('preference_1')
# # 		preference_2 = request.POST.get('preference_2')
# # 		preference_3 = request.POST.get('preference_3')
# # 		preference_4 = request.POST.get('preference_4')
# # 		preference_5 = request.POST.get('preference_5')
# # 		# full_name = request.POST.get('full_name')
# # 		suggestion = request.POST.get('suggestion')	

# # 		SOP = request.POST.get('SOP')
# # 		mentee = Mentee(full_name = full_name, roll_no = roll_no,
# # 			department = department, degree = degree, degree_other= degree_other,
# # 			contact_number = contact_number, email_id = email_id,
# # 			preference_1 = preference_1, preference_2 = preference_2,
# # 			preference_3 = preference_3, preference_4 = preference_4, 
# # 			preference_5 = preference_5, suggestion = suggestion, SOP = SOP)
# # 		mentee.save()
# # 		context = {}
# # 	return render(request, 'menteeinfo/register_success.html',)


# # def export(request):
# # 	response = HttpResponse(content_type = 'text/csv')
# # 	writer = csv.writer(response)
# # 	writer.writerow([
# #     'Fullname',
# #     'Roll No',
# #     'Department',
# #     'Other department',
# #     'degree',
# #     'Other Degree',
# #     'Graduation Year',
# #     'Contact',
# #     'Email',
# #     'Option',
# #     'Designation',
# #     'Company Name',
# #     'University Name',
# #     'experience',
# #     'Preference 1',
# #     'Preference 2',
# #     'Preference 3',
# #     'Core',
# #     'Core Subdivision',
# #     'Preferred mentees',
# #     'Suggestions',
# #     'Recommendations',
# # ])
# # 	for registration in Registration.objects.all().values_list(
# #     'fullname',
# #     'rollno',
# #     'department',
# #     'department_other',
# #     'degree',
# #     'degree_other',
# #     'graduation_year',
# #     'contact',
# #     'email',
# #     'placementOrGrad',
# #     'designation', 
# #     'company_name',
# #     'university_name',
# #     'experience',
# #     'field_pref1',
# #     'field_pref2',
# #     'field_pref3',
# #     'branch',
# #     'branch_subdivision',
# #     'preferred_mentees',
# #     'suggestions',
# #     'alumni_recommendations'
# #     ):
# # 		writer.writerow(registration)
	
# # 	response['Content-Disposition'] = 'attachment; filename="mentors_pmp23.csv"'
# # 	return response

# # def index(request):
# #     return render(request, 'menteeinfo/home.html')

# # def phonehome(request):
# #     return render(request, 'menteeinfo/phonehome.html')

# # def mentorReg(request):
# #     def __str__(self):
# #         return self.fullname

# #     if request.method == 'POST':        
# #         fullname=request.POST.get('fullname')
# #         rollno=request.POST.get('rollno')
# #         department=request.POST.get('department')
# #         department_other=request.POST.get('other_department')
# #         degree=request.POST.get('degree')
# #         degree_other=request.POST.get('degree_other')
# #         graduation_year=request.POST.get('graduation_year')
# #         contact=request.POST.get('contact')
# #         email=request.POST.get('email')
# #         placementOrGrad = request.POST.get('placementOrGrad')
        
# #         field_pref3 = "NA"
        
# #         if(placementOrGrad == 'placement'):
# #             experience=request.POST.get('placementExperience')
# #             field_pref1=request.POST.get('placementPref1')
# #             field_pref2=request.POST.get('placementPref2')
# #             field_pref3=request.POST.get('placementPref3')
# #         else:
# #             experience=request.POST.get('gradExperience')
# #             field_pref1=request.POST.get('gradPref1')
# #             field_pref2=request.POST.get('gradPref2')

            
# #         designation=request.POST.get('designation')
# #         company_name=request.POST.get('company_name')
# #         university=request.POST.get('university_name')
# #         suggestions=request.POST.get('suggestion')
# #         recommendations=request.POST.get('referral')        
# #         core_branch=request.POST.get('core')
# #         branch_subdivision=request.POST.get('subdivisions')
        
# #         print(branch_subdivision)
        
        
# #         preferred_mentees = request.POST.get('no_of_mentees')
        
        
# #         registration = Registration(fullname=fullname or "NA", email=email or "NA", department=department or "NA", rollno=rollno or "NA", department_other=department_other or "NA",
# #                                     degree=degree or "NA", degree_other=degree_other or "NA", graduation_year=graduation_year or "NA", field_pref3=field_pref3 or "NA",
# #                                     contact=contact or "NA", placementOrGrad=placementOrGrad or "NA", designation=designation or "NA", company_name=company_name or "NA"
# #                                     , experience=experience or "NA", field_pref1=field_pref1 or "NA", field_pref2=field_pref2 or "NA", branch=(core_branch or "NA"), branch_subdivision=(branch_subdivision or "NA")
# #                                     , preferred_mentees=preferred_mentees or "NA", university_name=(university or "NA"), suggestions=suggestions or "NA", alumni_recommendations=recommendations or "NA")
        
        
        
# #         registration.save()
# #         return render(request, 'menteeinfo/thank.html')
        
       
# #         # profiles=request.POST.get('profiles')
# #         # pref1=request.POST.get('pref1')
# #         # pref2=request.POST.get('pref2')
# #         # core=request.POST.get('core')
# #         # aerospace = request.POST.get('aerospace')
# #         # chemical = request.POST.get('chemical')
# #         # bsbe = request.POST.get('bsbe')
# #         # earthscience = request.POST.get('earthscience')
# #         # ep = request.POST.get('EP')
# #         # mems = request.POST.get('mems')
# #         # maths = request.POST.get('maths')
# #         # ieor = request.POST.get('ieor')
# #         # civil = request.POST.get('civil')
# #         # chemistry = request.POST.get('chemistry')
# #         # electrical = request.POST.get('electrical')
# #         # energy = request.POST.get('energy')
# #         # mechanical = request.POST.get('mechanical')
# #         # other_mentorship=request.POST.get('other_mentorship')
# #         # other_department = request.POST.get('other_department')
# #         # no_of_mentees=request.POST.get('no_of_mentees')
# #         # referral=request.POST.get('referral')
# #         # suggestions=request.POST.get('suggestion')
        
        

# #         # registration=Registration(fullname=fullname, rollno=rollno, department=department, degree=degree, degree_other=degree_other, graduation_year=graduation_year, designation=designation, experience=experience, contact=contact,  email=email, profiles=profiles, pref1=pref1, pref2=pref2, core=core,
# #         # aerospace=aerospace,
# #         # chemical = chemical,
# #         # bsbe = bsbe,
# #         # earthscience = earthscience,
# #         # ep=ep,
# #         # mems = mems,
# #         # maths=maths,
# #         # ieor=ieor,
# #         # civil=civil,
# #         # chemistry = chemistry,
# #         # electrical=electrical,
# #         # energy=energy,
# #         # mechanical=mechanical,
# #         # other_mentorship=other_mentorship ,
# #         # other_department = other_department,
# #         # no_of_mentees=no_of_mentees, referral=referral,  suggestions=suggestions)
# #         # registration.save()
# #         # return redirect('api/thanks')
# #         # thank(request)
# #         # return render(request, 'menteeinfo/thank.html')
        
# #     context = {
# #         'options': options.__dict__,
# #     }
        
# #     return render(request, 'menteeinfo/form.html', context)

# # def thank(request):
# #     return render(request, 'menteeinfo/thank.html')

# # @api_view(['POST'])
# # def testapi(request):
# #     req_data = request.data
# #     alumni_id = req_data['id']
# #     duration = req_data['duration']
# #     context = {'alumni_id': alumni_id, 'duration': duration}
# #     return render(request, 'thank.html', context)









# from django.shortcuts import render, redirect
# from django.http import HttpResponse, response
# from .models import Mentee, Mentor, Registration
# from django.core.exceptions import ValidationError
# import csv
# from rest_framework.decorators import api_view
# # from . import options
# from .options import *

# # # from .resources import MentorResource
# # # from django.contrib import messages
# # # from tablib import Dataset

# # # to upload excel file

# # # def simple_upload(request):
# # # 	if(request.method == 'POST'):
# # # 		mentor_resource = MentorResource()
# # # 		dataset = Dataset()
# # # 		new_mentor = request.FILES['myfile']

# # # 		if not new_mentor.name.endswith('xlsx'):
# # # 			messages.info(request, 'wrong format')
# # # 			return render(request, 'upload.html')
# # # 		imported_data = dataset.load(new_mentor.read(), format = 'xlsx')
# # # 		for data in imported_data:
# # # 			value=Mentor(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9])
# # # 			value.save()
# # # 	return render(request, 'upload.html')


# # # Create your views here.
# # def index(request):
# # 	return render(request, 'menteeinfo/index.html')

# def mentor_create_view(request, mentor_id):
#     mentor = Mentor.objects.get(id=mentor_id)
#     saved_field_value = mentor.field

#     return render(request, 'change_form.html', {
#         'saved_field_value': saved_field_value,
#     })

# # Mentee registration
# def register(request):
#     corementors = Mentor.objects.filter(field="Core", type="placement")
#     Corementors = Mentor.objects.filter(field="core", type="placement")
#     consultmentors = Mentor.objects.filter(field="Consultancy", type="placement")
#     Consultmentors = Mentor.objects.filter(field="consultancy", type="placement")
#     consulting = Mentor.objects.filter(field="consulting", type="placement")
#     analyticmentors = Mentor.objects.filter(field="Analytics", type="placement")
#     finmentors = Mentor.objects.filter(field="Finance", type="placement")
#     finance = Mentor.objects.filter(field="finance", type="placement")
#     csmentor = Mentor.objects.filter(field="IT/Software", type="placement")
#     othermentors = Mentor.objects.filter(field="other", type="placement")
#     Othermentors = Mentor.objects.filter(field="Other", type="placement")
#     Othersmentors = Mentor.objects.filter(field="Others", type="placement")
#     chutiya = Mentor.objects.filter(field="FMCG(product management)", type="placement")
#     fmcg = Mentor.objects.filter(field="FMCG", type="placement")
#     bhadwa = Mentor.objects.filter(field="analytics", type="placement")
#     # randi = Mentor.objects.filter(field="IT/Software", type="placement")
#     corecontrol = Mentor.objects.filter(field="Mechanical(core control)", type="placement")
#     itsoftwar = Mentor.objects.filter(field="it_software", type="placement")

#     CorementorsGrad = Mentor.objects.filter(field="core", type="grad")
#     corementorsGrad = Mentor.objects.filter(field="Core", type="grad")
#     managementmentorsGrad = Mentor.objects.filter(field="management", type="grad")
#     ManagementmentorsGrad = Mentor.objects.filter(field="Management", type="grad")
    
#     context = {
#         'mentors_list_core': corementors, 
#         'mentors_list_consult': consultmentors,
#         'mentors_list_analysis': analyticmentors,
#         'mentors_list_fin': finmentors,
#         'mentors_list_cs': csmentor,
#         'mentors_list_other': othermentors,
#         'mentors_list_fmcg': fmcg,
#         'mentors_list_Core': Corementors,
#         'mentors_list_Other': Othermentors,
#         'mentors_list_Others': Othersmentors,
#         'mentors_list_chutiya': chutiya,
#         'bhadwa': bhadwa,
#         # 'randi': randi,
#         'corecontrol': corecontrol,
#         'Consultmentors': Consultmentors,
#         'consulting': consulting,
#         'finance': finance,
#         'itsoftwar': itsoftwar,
#         'mentors_core': corementorsGrad,        
#         'mentors_Core': CorementorsGrad,
#         'mentors_management': managementmentorsGrad,        
#         'mentors_Management': ManagementmentorsGrad,
#     }

#     # dict=[]
#     # allmentors = Mentor.objects.all()
#     # for mentor in allmentors:
#     #     exp = mentor.experience
#     #     explist = exp.split(",")
#     #     dict[mentor.rollno] = explist
#     # print (dict[183020060])
#     # allmentors_sorted = Mentor.objects.all().order_by['gray_out']
#     return render(request, "menteeinfo/register.html", context)

# # def mentorexp(request):
# #     allmentors = Mentor.objects.all()
# # 	for mentor in allmentors:
# #     	exp = mentor.experience

# # def gradRegister(request):
# #     corementors = gradMentor.objects.filter(field="Core")
# #     Corementors = gradMentor.objects.filter(field="core")
# #     managementmentors = gradMentor.objects.filter(field="management")
# #     Managementmentors = gradMentor.objects.filter(field="Management")
# #     context = {
# #         'mentors_core': corementors,        
# #         'mentors_Core': Corementors,
# #         'mentors_management': managementmentors,        
# #         'mentors_Management': Managementmentors,
# #     }

# #     return render(request, "menteeinfo/register.html", context)

# def menteereg(request):
#     if request.method == 'POST':
#         full_name = request.POST.get('full_name')
#         roll_no = request.POST.get('roll_no')
#         department = request.POST.get('department')
#         dept_other = request.POST.get('dept_other')
#         degree = request.POST.get('degree')
#         degree_other = request.POST.get('degree_other')
#         contact_number = request.POST.get('contact_number')
#         email_id = request.POST.get('email_id')
#         preference_1 = request.POST.get('preference_1')
#         preference_2 = request.POST.get('preference_2')
#         preference_3 = request.POST.get('preference_3')
#         preference_4 = request.POST.get('preference_4')
#         preference_5 = request.POST.get('preference_5')
#         suggestion = request.POST.get('suggestion')
#         SOP = request.POST.get('SOP')
        
#         mentee = Mentee(
#             full_name=full_name,
#             roll_no=roll_no,
#             department=department,
#             dept_other=dept_other,
#             degree=degree,
#             degree_other=degree_other,
#             contact_number=contact_number,
#             email_id=email_id,
#             preference_1=preference_1,
#             preference_2=preference_2,
#             preference_3=preference_3,
#             preference_4=preference_4,
#             preference_5=preference_5,
#             suggestion=suggestion,
#             SOP=SOP
#         )
#         mentee.save()
#         context = {}
#     return render(request, 'menteeinfo/register_success.html', context)


# def export(request):
# 	response = HttpResponse(content_type = 'text/csv')
# 	writer = csv.writer(response)
# 	writer.writerow([
#     'Fullname',
#     'Roll No',
#     'Department',
#     'Other department',
#     'degree',
#     'Other Degree',
#     'Graduation Year',
#     'Contact',
#     'Email',
#     'Option',
#     'Designation',
#     'Company Name',
#     'University Name',
#     'experience',
#     'Preference 1',
#     'Preference 2',
#     'Preference 3',
#     'Core',
#     'Core Subdivision',
#     'Preferred mentees',
#     'Suggestions',
#     'Recommendations',
# ])
# 	for registration in Registration.objects.all().values_list(
#     'fullname',
#     'rollno',
#     'department',
#     'department_other',
#     'degree',
#     'degree_other',
#     'graduation_year',
#     'contact',
#     'email',
#     'placementOrGrad',
#     'designation', 
#     'company_name',
#     'university_name',
#     'experience',
#     'field_pref1',
#     'field_pref2',
#     'field_pref3',
#     'branch',
#     'branch_subdivision',
#     'preferred_mentees',
#     'suggestions',
#     'alumni_recommendations'
#     ):
# 		writer.writerow(registration)
	
# 	response['Content-Disposition'] = 'attachment; filename="mentors_pmp23.csv"'
# 	return response

# def index(request):
#     return render(request, 'menteeinfo/home.html')

# def phonehome(request):
#     return render(request, 'menteeinfo/phonehome.html')

# def mentorReg(request):
#     def _str_(self):
#         return self.fullname

#     if request.method == 'POST':        
#         fullname=request.POST.get('fullname')
#         rollno=request.POST.get('rollno')
#         department=request.POST.get('department')
#         department_other=request.POST.get('other_department')
#         degree=request.POST.get('degree')
#         degree_other=request.POST.get('degree_other')
#         graduation_year=request.POST.get('graduation_year')
#         contact=request.POST.get('contact')
#         email=request.POST.get('email')
#         placementOrGrad = request.POST.get('placementOrGrad')
        
#         field_pref3 = "NA"
        
#         if(placementOrGrad == 'placement'):
#             experience=request.POST.get('placementExperience')
#             field_pref1=request.POST.get('placementPref1')
#             field_pref2=request.POST.get('placementPref2')
#             field_pref3=request.POST.get('placementPref3')
#         else:
#             experience=request.POST.get('gradExperience')
#             field_pref1=request.POST.get('gradPref1')
#             field_pref2=request.POST.get('gradPref2')

            
#         designation=request.POST.get('designation')
#         company_name=request.POST.get('company_name')
#         university=request.POST.get('university_name')
#         suggestions=request.POST.get('suggestion')
#         recommendations=request.POST.get('referral')        
#         core_branch=request.POST.get('core')
#         branch_subdivision=request.POST.get('subdivisions')
        
#         print(branch_subdivision)
        
        
#         preferred_mentees = request.POST.get('no_of_mentees')
        
        
#         registration = Registration(fullname=fullname or "NA", email=email or "NA", department=department or "NA", rollno=rollno or "NA", department_other=department_other or "NA",
#                                     degree=degree or "NA", degree_other=degree_other or "NA", graduation_year=graduation_year or "NA", field_pref3=field_pref3 or "NA",
#                                     contact=contact or "NA", placementOrGrad=placementOrGrad or "NA", designation=designation or "NA", company_name=company_name or "NA"
#                                     , experience=experience or "NA", field_pref1=field_pref1 or "NA", field_pref2=field_pref2 or "NA", branch=(core_branch or "NA"), branch_subdivision=(branch_subdivision or "NA")
#                                     , preferred_mentees=preferred_mentees or "NA", university_name=(university or "NA"), suggestions=suggestions or "NA", alumni_recommendations=recommendations or "NA")
        
        
        
#         registration.save()
#         return render(request, 'menteeinfo/thank.html')
        
       
#         # profiles=request.POST.get('profiles')
#         # pref1=request.POST.get('pref1')
#         # pref2=request.POST.get('pref2')
#         # core=request.POST.get('core')
#         # aerospace = request.POST.get('aerospace')
#         # chemical = request.POST.get('chemical')
#         # bsbe = request.POST.get('bsbe')
#         # earthscience = request.POST.get('earthscience')
#         # ep = request.POST.get('EP')
#         # mems = request.POST.get('mems')
#         # maths = request.POST.get('maths')
#         # ieor = request.POST.get('ieor')
#         # civil = request.POST.get('civil')
#         # chemistry = request.POST.get('chemistry')
#         # electrical = request.POST.get('electrical')
#         # energy = request.POST.get('energy')
#         # mechanical = request.POST.get('mechanical')
#         # other_mentorship=request.POST.get('other_mentorship')
#         # other_department = request.POST.get('other_department')
#         # no_of_mentees=request.POST.get('no_of_mentees')
#         # referral=request.POST.get('referral')
#         # suggestions=request.POST.get('suggestion')
        
        

#         # registration=Registration(fullname=fullname, rollno=rollno, department=department, degree=degree, degree_other=degree_other, graduation_year=graduation_year, designation=designation, experience=experience, contact=contact,  email=email, profiles=profiles, pref1=pref1, pref2=pref2, core=core,
#         # aerospace=aerospace,
#         # chemical = chemical,
#         # bsbe = bsbe,
#         # earthscience = earthscience,
#         # ep=ep,
#         # mems = mems,
#         # maths=maths,
#         # ieor=ieor,
#         # civil=civil,
#         # chemistry = chemistry,
#         # electrical=electrical,
#         # energy=energy,
#         # mechanical=mechanical,
#         # other_mentorship=other_mentorship ,
#         # other_department = other_department,
#         # no_of_mentees=no_of_mentees, referral=referral,  suggestions=suggestions)
#         # registration.save()
#         # return redirect('api/thanks')
#         # thank(request)
#         # return render(request, 'menteeinfo/thank.html')
        
#     context = {
#         # 'options': options._dict_,
#         'options': OPTIONS,
#     }
        
#     return render(request, 'menteeinfo/form.html', context)

# def thank(request):
#     return render(request, 'menteeinfo/thank.html')

# @api_view(['POST'])
# def testapi(request):
#     req_data = request.data
#     alumni_id = req_data['id']
#     duration = req_data['duration']
#     context = {'alumni_id': alumni_id, 'duration': duration}
#     return render(request, 'thank.html', context)


