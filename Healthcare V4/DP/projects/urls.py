from unicodedata import name
from django.urls import path
from . import views
from .views import AddCategoryview, AddCommentview, AddPostview, HomeView, articleview,UpdatePostView,DeletePostView,AddContactview,AddAppointmentview,AddPrescriptionview
#CategoryView
    
urlpatterns = [

    path('homeview/', HomeView.as_view(), name="homeview"),
    path('article/<int:pk>/comment/', AddCommentview.as_view(), name='add_comment'),
    path('article/<int:pk>', articleview.as_view(), name="article_detail"),
    path('add_category/', AddCategoryview.as_view(), name="Category"),
    path('add_post/', AddPostview.as_view(), name='add_post'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name="update_view"),
    path('article/<int:pk>/remove',DeletePostView.as_view(),name="delete_view"),
    # path('category/<str:cats>/',CategoryView,name="category_view"),
    
    # path('contact/', views.AddContactview, name='contact'),
    path('contact/', AddContactview.as_view(), name="contact"),
    # path('appointment.html', views.AddAppointmentview, name="appointment"),
    # path('appointment/<int:pk>', AddAppointmentview.as_view(), name='appointment'),
    path('appointment/', AddAppointmentview.as_view(), name="appointment"),
    path('printScript', views.all_appointment, name="printScript"),
    path('prescription/', AddPrescriptionview.as_view(), name="prescription"),
    path('payment', views.payment_appointment, name="payment"),
    #  path('prescriptionshow/', PrescriptionShow.as_view(), name="prescriptionshow"),
       path('prescriptionshow', views.PrescriptionShow, name="prescriptionshow"),
    
]