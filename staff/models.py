from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=30)
    guardian_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    contact_number = models.CharField(max_length=12)
    date_of_birth = models.DateField(auto_now=False,auto_now_add=False,verbose_name="Date of birth")
    gender = models.CharField(max_length=200,default="")
    religion = models.CharField(max_length=200,default="")
    address = models.CharField(max_length=300)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    pincode = models.IntegerField()
    photo = models.FileField(upload_to='Teacher Photos')
    designation = models.CharField(max_length=100,default="")
    subject = models.CharField(max_length=300)
    languages = models.CharField(max_length=300)
    sslc_certificate_upload = models.FileField(upload_to='SSLC Certificate of Techers')
    sslc_percentage = models.CharField(max_length=100)
    plustwo_certificate_upload = models.FileField(upload_to=' PlusTwo certificate of Techers')
    plustwo_percentage = models.CharField(max_length=100)
    degree_certificate_upload = models.FileField(upload_to='Degree Certificate of Techers')
    degree_persentage = models.CharField(max_length=100)
    b_ed_certificate_upload= models.FileField(upload_to='B.ED Certificate of Techers')
    b_ed_persentage = models.CharField(max_length=100)
    m_ed_certificate_upload= models.FileField(upload_to='M.ED Certificate of Techers')
    m_ed_persentage = models.CharField(max_length=100)
    set_certificate_upload = models.FileField(upload_to='SET Certificate of Techers')
    net_certificate_upload = models.FileField(upload_to='SET Certificate of Techers')
    k_tet_certificate_upload = models.FileField(upload_to='SET Certificate of Techers')
    experience = models.CharField(max_length=100)
    cv_upload = models.FileField(upload_to='CV Of Techers')
    resume_upload = models.FileField(upload_to='Resume Of Techers')
    DisplayFields = ['name','email','contact_number','date_of_birth','gender','subject','religion','state']
    SearchableFields = ['name','email','contact_number','date_of_birth','gender','subject','religion','state']
