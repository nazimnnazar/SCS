from django import forms
from . models import StudentApplication
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError 
class StudentApplicationForm(forms.ModelForm):
    student_name = forms.CharField(
        label = 'student_name ' ,min_length=3,max_length=50,
        validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
        message="Only Letter Is Allowed")],
        error_messages ={'requires':'The Full name is requires !'},
        widget=forms.TextInput(attrs={'placeholder':'Student Name'})
    )
    photo = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs = {
            }
        )
    )
    email = forms.CharField(
        label = "Email",
        min_length=3,max_length=30,
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
        message="Enter Valid Email Address")],
        widget=forms.TextInput(attrs={'placeholder':'Email'})
    )
    def clean_email(self):
        email = self.cleaned_data.get('email')
        for i in StudentApplication.objects.all():
            if i.email == email:
                raise forms.ValidationError('Denaie! ' + email + ' is already register')
        return email
    class Meta:
        model = StudentApplication
        fields = "__all__"
        widgets={
            'date_of_birth':forms.DateInput(
                attrs={
                    'style':'font-size:16px;',
                    'type':'date',
                    'onkeydown':'retrun false',
                }
            ),
            'sslc_pass_out_year':forms.DateInput(
                attrs={
                    'style':'font-size:16px;',
                    'type':'date',
                    'onkeydown':'retrun false',
                }
            ),
            'higher_secondary_pass_out_year':forms.DateInput(
                attrs={
                    'style':'font-size:16px;',
                    'type':'date',
                    'onkeydown':'retrun false',
                }
            ),
        }
    def __init__(self, *args,**kwargs):
        super(StudentApplicationForm,self).__init__(*args,**kwargs)
        self.fields["gender"].choices = [('','Select your gender'),] + list(self.fields["gender"].choices)[0:]
        self.fields["religion"].choices = [('','Select your religion'),] + list(self.fields["religion"].choices)[0:]
        self.fields["relationship_of_guardian"].choices = [('','Relationship of guardian'),] + list(self.fields["relationship_of_guardian"].choices)[0:]
        self.fields["student_name"].required = True
        self.fields["email"].required = True
        self.fields["contact_number"].required = True
        self.fields["date_of_birth"].required = True
        self.fields["gender"].required = True
        self.fields["religion"].required = True
        self.fields["photo"].required = True
        self.fields["Aadhar"].required = True
        self.fields["Signature"].required = True
        self.fields["address"].required = True
        self.fields["state"].required = True
        self.fields["city"].required = True
        self.fields["pincode"].required = True
        self.fields["guardianname"].required = True
        self.fields["guardian_contact_number"].required = True
        self.fields["relationship_of_guardian"].required = True
        self.fields["signacher_of_guardian"].required = True
        self.fields["school_name"].required = True
        self.fields["school_location"].required = True
        self.fields["sslc_total_persantage"].required = True
        self.fields["sslc_pass_out_year"].required = True
        self.fields["sslc_certificate_upload"].required = True
        self.fields["higher_secondary_chool_name"].required = True
        self.fields["higher_secondary_school_location"].required = True
        self.fields["higher_secondary_total_mark"].required = True
        self.fields["higher_secondary_pass_out_year"].required = True
        self.fields["higher_secondary_certificate_upload"].required = True
        self.fields["student_name"].widget.attrs.update({'style':'font-size:15px','placeholder':'Student Name'})
        self.fields["email"].widget.attrs.update({'style':'font-size:15px','placeholder':'Email'})
        self.fields["contact_number"].widget.attrs.update({'style':'font-size:15px','placeholder':'Contact Number','data-mask':'(00) 00-00'})
        self.fields["date_of_birth"].widget.attrs.update({'style':'font-size:15px','placeholder':'Date Of Birth'})
        self.fields["gender"].widget.attrs.update({'style':'font-size:15px','placeholder':'Gender'})
        self.fields["religion"].widget.attrs.update({'style':'font-size:15px','placeholder':'Religion'})
        self.fields["photo"].widget.attrs.update({'style':'font-size:15px','placeholder':'photo'})
        self.fields["Aadhar"].widget.attrs.update({'style':'font-size:15px','placeholder':'Aadhar'})
        self.fields["Signature"].widget.attrs.update({'style':'font-size:15px','placeholder':'Signature'})
        self.fields["address"].widget.attrs.update({'style':'font-size:15px','placeholder':'Address'})
        self.fields["state"].widget.attrs.update({'style':'font-size:15px','placeholder':'State'})
        self.fields["city"].widget.attrs.update({'style':'font-size:15px','placeholder':'City'})
        self.fields["pincode"].widget.attrs.update({'style':'font-size:15px','placeholder':'Pincode'})
        self.fields["guardianname"].widget.attrs.update({'style':'font-size:15px','placeholder':'Guardianname'})
        self.fields["guardian_contact_number"].widget.attrs.update({'style':'font-size:15px','placeholder':'Guardian Contact Number'})
        self.fields["relationship_of_guardian"].widget.attrs.update({'style':'font-size:15px','placeholder':'Relationship Of Guardian'})
        self.fields["signacher_of_guardian"].widget.attrs.update({'style':'font-size:15px','placeholder':'Signacher Of Guardian'})
        self.fields["school_name"].widget.attrs.update({'style':'font-size:15px','placeholder':'School Name'})
        self.fields["school_location"].widget.attrs.update({'style':'font-size:15px','placeholder':'School Location'})
        self.fields["sslc_total_persantage"].widget.attrs.update({'style':'font-size:15px','placeholder':'SSLC Total Persantage'})
        self.fields["sslc_pass_out_year"].widget.attrs.update({'style':'font-size:15px','placeholder':'SSLS Pass Out Year'})
        self.fields["sslc_certificate_upload"].widget.attrs.update({'style':'font-size:15px','placeholder':'SSLC Certificate Upload'})
        self.fields["higher_secondary_chool_name"].widget.attrs.update({'style':'font-size:15px','placeholder':'Higher Hecondary School Name'})
        self.fields["higher_secondary_school_location"].widget.attrs.update({'style':'font-size:15px','placeholder':'Higher Secondary School Location'})
        self.fields["higher_secondary_total_mark"].widget.attrs.update({'style':'font-size:15px','placeholder':'Higher Secondary Total Mark'})
        self.fields["higher_secondary_pass_out_year"].widget.attrs.update({'style':'font-size:15px','placeholder':'Higher Secondary Pass Out Year'})
        self.fields["higher_secondary_certificate_upload"].widget.attrs.update({'style':'font-size:15px','placeholder':'Higher Secondary Certificate Upload'})