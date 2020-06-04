from  .views import aboutview,homeview,kitchenview,careview,holdview,codesview,contactview
from django.urls import path
app_name = 'home'

urlpatterns = [

    path('',homeview,name='home'),
    path('about',aboutview,name='about'),
    path('kitchen',kitchenview,name='kitchen'),
    path('care',careview,name='care'),
    path('codes',codesview,name='codes'),
    path('contact',contactview,name='contact'),
]