from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('',views.home,name='home'),
   path('about/',views.about,name='about'),
   path('contact/',views.contact_us,name='contact'),
   path('feature/',views.feature,name='feature'),
   path('menu/',views.menu,name='menu'),
   path('booking/',views.booking,name='booking'),
   path('team/',views.team,name='team'),
   path('blog/',views.blog,name='blog'),
   path('single/',views.single,name='single'),
   path('order/',views.order,name='order'),
   path('registration/',views.registration,name='registration'),
   path('login/',views.signin,name='login'),
   path('dashboard/',views.dashboard,name="dashboard"),
   path('logout/',views.user_logout,name="logout"),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
