
from django import forms
from .models import  Post,Comment #CategoryAcc

# choices=[('Magical','Magical'),('Spy','Spy'),('Health','Health')]
# choices=CategoryAcc.objects.all().values_list('name','name')
# choice_list=[]
# for item in choices:
#    choice_list.append(item)
class EditForm(forms.ModelForm):
     class Meta:
        model=Post
        fields=('title','author','body')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),

         
         }

class PostForm(forms.ModelForm):
     class Meta:
        model=Post
        fields=('title','title_tag','author','category','body','snippet')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            # 'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'snippet':forms.Textarea(attrs={'class':'form-control'}),

         
         }

class CommentForm(forms.ModelForm):
     class Meta:
        model=Comment
        fields=('name','body')

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),

         
         }

# class AppointmentForm(forms.ModelForm):
#      class Meta:
#         model=Appointment
#         fields=('title','title_tag','author','category','body','snippet')

#         widgets={
#             'title':forms.TextInput(attrs={'class':'form-control'}),
#             'title_tag':forms.TextInput(attrs={'class':'form-control'}),
#             # 'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
#             'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
#             # 'author':forms.Select(attrs={'class':'form-control'}),
#             'body':forms.Textarea(attrs={'class':'form-control'}),
#             'snippet':forms.Textarea(attrs={'class':'form-control'}),

         
#          }
