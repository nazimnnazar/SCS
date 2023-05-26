from django import forms
from . models import Teacher
class TeacherForm(forms.ModelForm):
    RELIGION = [
        ('','Select Your Religion'),
        ('OBC','OBC'),
        ('OEC','OEC'),
        ('General','General')
    ]
    DESOGNATION = [
        ('','Select Your Designation'),
        ('PGT','PGT'),
        ('TGT','TGT'),
        ('PRT','PRT'),
    ]
    GENDER =[
        ('','Select Your Gender'),
        ('Female','Female'),
        ('Male','Male')
    ]
    gender = forms.CharField(
        label='Gender',
        widget = forms.Select(
            choices = GENDER,
            attrs = {
                'class' : 'form-control'
            }
        )
    )
    religion = forms.CharField(
        label='Religion',
        widget = forms.Select(
            choices = RELIGION,
            attrs = {
                'class' : 'form-control'
            }
        )
    )
    designation = forms.CharField(
        label='designation',
        widget = forms.Select(
            choices = DESOGNATION,
            attrs = {
                'class' : 'form-control'
            }
        )
    )
    class Meta:
        model = Teacher
        fields = "__all__"
        widgets={
            'date_of_birth':forms.DateInput(
                attrs={
                    'style':'font-size:16px;',
                    'type':'date',
                    'onkeydown':'retrun false',
                }
            )
        }
    def __init__(self,*args,**kwargs):
        super(TeacherForm,self).__init__(*args,**kwargs)
