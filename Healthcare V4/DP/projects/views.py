
from urllib import request
from django.shortcuts import render
import email
from msilib.schema import ListView
from sre_constants import SUCCESS
from turtle import pos
from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import  User
from django.contrib import messages,auth
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import is_valid_path, reverse_lazy
# from mysqlx import Auth
from django .views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView
from main_app.views import post
from projects.models import Contact, Post,Comment ,Appointment,Prescription#CategoryAcc
# , registerEnquiry,Profile
from .forms import PostForm,EditForm,CommentForm
from django.core.mail import send_mail

# Create your views here.

class HomeView(ListView):
    model=Post
    template_name='innerPro/home.html'
    ordering=['-post_date']
    # ordering=['-pk']

class articleview(DetailView):
    model=Post
    template_name='UpdateEdit.html'

class AddPostview(CreateView):
    model=Post
    form_class=PostForm
    template_name='innerPro/add_postpage.html'
    # fields='__all__'
    # fileds=('title','body')
class AddCategoryview(CreateView):
    model=Post
    # form_class=PostForm
    template_name='innerPro/add_CategoryPage.html'
    fields='__all__'
    # fileds=('title','body')

class UpdatePostView(UpdateView):
    model=Post
    form_class=EditForm
    template_name='innerPro/updatePost.html'
    # fields=['title','body']
class DeletePostView(DeleteView):
    model=Post
   
    template_name='innerPro/delete_post.html'
    succes_url=reverse_lazy('homeview')
 

# def CategoryView(request,cats):
#     category_posts=Post.objects.filter(category=cats)
#     return render(request,'innerPro/categories.html',{'cats':cats,'category_posts':category_posts})

class AddCommentview(CreateView):
    model=Comment
    form_class=CommentForm
    template_name='innerPro/add_comments.html'
    succes_url=reverse_lazy('homeview')

    def form_valid(self,form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)
    # fields='__all__'

class AddContactview(CreateView):
    model=Contact
    template_name='contact.html'
    fields='__all__'
    succes_url=reverse_lazy('contact')

    # def sendmail(self):
    #     if request.method=="post":
    #         m_name=request.Post['name']
    #         email=request.Post['email']
    #         body=request.Post['body']

    #         send_mail(
    #             m_name,
    #             email,
    #             body,
    #             ['ashrafultan10@gmail.com'],
    
    
    #         )
    #         return render(request,'contact.html',{'m_name':name})
    




# def AddContactview(request):
#     if request.method=="Post":
#         name=request.Post['name']
#         email=request.Post['email']
#         body=request.Post['body']
#         ins=Contact(name=name,email=email,body=body)
#         ins.save()
#         print(name,email)
#     return render(request,'contact.html')

# def AddAppointmentview(request):
    
#     if request.method=='POST':
#         your_name=request.Post['your-name']
#         your_phone  =request.Post['your-phone']
#         your_email  =request.Post['your-email']
#         your_address=request.Post['your-address']
#         your_schedule=request.Post['your-schedule']


#         return render(request,'appointment.html',{
#             'your_name':your_name,
#             'your_schedule':your_schedule,
#              'your_phone  ': your_phone  ,
#              'your_email  ': your_email  ,
#              'your_address': your_address,
    
#         })

#     else:
#          return render(request,'basic.html')

class AddAppointmentview(CreateView):
    model=Appointment
    template_name='appointment.html'
    fields='__all__'
    succes_url=reverse_lazy('appointment')



def all_appointment(request):
    appointment_list=Appointment.objects.all()
    return render(request,'innerPro/printappointment.html',
    { 'appointment_list':appointment_list })

# class all_appointment(ListView):
#     model=Appointment
#     appointment_list=Appointment.objects.all()
#     template_name=('innerPro/printappointment.html',
#     {'appointment_list':appointment_list})


def payment_appointment(request):
    
    return render(request,'innerPro/paymentDemo.html')

class AddPrescriptionview(CreateView):
    model=Prescription
    template_name='innerPro/prescription.html'
    fields='__all__'
    succes_url=reverse_lazy('prescription')



def PrescriptionShow(request):
        showprescription_list=Prescription.objects.all()
        return render(request,'innerPro/showPrescription.html',
        { 'showprescription_list':showprescription_list })
    






     