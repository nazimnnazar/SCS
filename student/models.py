from django.db import models

GENDER = (
    ('Male','Male'),
    ('Female','Female')
)
RELIGION = (
    ('OBC','OBC'),
    ('OEC','OEC'),
    ('General','General')
)
RELATIONSHIP_OF_GUARDIAN = (
    ('Father','Father'),
    ('Mother','Mother'),
    ('Step Guardian','Step Guardian'),
    ('Brother','Brother'),
    ('Sister','Sister'),
    ('Other','Other')
)
class StudentApplication(models.Model):
    student_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    contact_number = models.CharField(max_length=12)
    date_of_birth = models.DateField(auto_now=False,auto_now_add=False,verbose_name="Date of birth")
    gender = models.CharField(max_length=200,default="",choices=GENDER)
    religion = models.CharField(max_length=200,default="",choices=RELIGION)
    photo = models.FileField(upload_to = 'Photo')
    Aadhar = models.FileField(upload_to ='Aadhar')
    Signature = models.FileField(upload_to='student_Signature')
    address = models.CharField(max_length=300)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    pincode = models.IntegerField()
    guardianname = models.CharField(max_length=200)
    guardian_contact_number = models.CharField(max_length=12)
    relationship_of_guardian= models.CharField(max_length=200,default="",choices=RELATIONSHIP_OF_GUARDIAN)
    signacher_of_guardian= models.FileField(upload_to ='signacher')
    school_name= models.CharField(max_length=200)
    school_location= models.CharField(max_length=200)
    sslc_total_persantage= models.IntegerField()
    sslc_pass_out_year= models.DateField(auto_now=False,auto_now_add=False,verbose_name="Pass Of year")
    sslc_certificate_upload= models.FileField(upload_to='sslc_certificate')
    higher_secondary_chool_name= models.CharField(max_length=200)
    higher_secondary_school_location= models.CharField(max_length=200)
    higher_secondary_total_mark= models.IntegerField()
    higher_secondary_pass_out_year= models.DateField(auto_now=False,auto_now_add=False,verbose_name="pass out year")
    higher_secondary_certificate_upload= models.FileField(upload_to ='HS_certificate')
    DisplayFields = ['student_name','email','contact_number','date_of_birth','gender','religion']
    SearchableFields = ['student_name','email','contact_number','date_of_birth','gender','religion']
