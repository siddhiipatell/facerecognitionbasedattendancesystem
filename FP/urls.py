"""FP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
                  path('admin/', admin.site.urls, name='admin'),
                  path('', views.index, name='index'),
                  path('index', views.index, name='index'),
                  path('index#contact', views.index, name='index'),

                  path('S_Login/admin', admin.site.urls, name='admin'),
                  path('F_login/admin', admin.site.urls, name='admin'),
                  path('S_registration/admin', admin.site.urls, name='admin'),
                  path('F_Registration/admin', admin.site.urls, name='admin'),
                  path('capture/admin', admin.site.urls, name='admin'),

                  path('S_Login/', views.s_login, name='S_Login'),
                  path('S_Login/f_login', views.f_login, name='f_login'),
                  path('S_Login/capture', views.capture, name='capture'),

                  path('capture/S_Login', views.s_login, name='S_Login'),

                  path('F_login/', views.f_login, name='F_login'),
                  path('F_login/S_Login', views.s_login, name='S_Login'),

                  path('S_registration/', views.s_registration, name='S_registration'),
                  path('S_Login/S_registration', views.s_registration, name='S_registration'),

                  path('F_Registration/', views.f_registration, name='F_Registration'),
                  path('F_login/F_Registration', views.f_registration, name='F_Registration'),

                  path('S_registration/capture', views.capture, name='capture'),
                  path('F_Registration/F_login', views.f_login, name='F_login'),

                  path('capture', views.capture, name='capture'),
                  path('Faculty', views.faculty, name='Faculty'),
                  path('F_login/Faculty', views.faculty, name='Faculty'),

                  path('S_registration/S_Login', views.s_login, name='S_Login'),
                  path('student', views.student, name='student'),
                  path('S_Login/student', views.student, name='student'),

                  path('Faculty/f_logout', views.f_logout, name='f_logout'),
                  path('f_logout', views.f_logout, name='f_logout'),
                  path('F_login/F_login', views.f_login, name='F_login'),
                  path('F_login/Faculty/f_logout', views.f_logout, name='f_logout'),
                  path('S_Login/S_Login', views.s_login, name='S_Login'),

                  path('Faculty/viewAttendance', views.viewAttendance, name='viewAttendance'),
                  path('viewAttendance', views.viewAttendance, name='viewAttendance'),
                  path('F_login/viewAttendance', views.viewAttendance, name='viewAttendance'),
                  path('F_login/Faculty/viewAttendance', views.viewAttendance, name='viewAttendance'),

                  path('editprofile', views.editprofile, name='editprofile'),
                  path('S_Login/editprofile', views.editprofile, name='editprofile'),
                  path('student/editprofile', views.editprofile, name='editprofile'),

                  path('editprofile1', views.editprofile1, name='editprofile1'),
                  path('F_login/editprofile1', views.editprofile1, name='editprofile1'),
                  path('faculty/editprofile1', views.editprofile1, name='editprofile1'),

                  path('monthAttendance', views.monthAttendance, name='monthAttendance'),
                  path('F_login/monthAttendance', views.monthAttendance, name='monthAttendance'),
                  path('faculty/monthAttendance', views.monthAttendance, name='monthAttendance'),

                  path('F_login/month', views.month, name='month'),
                  path('month', views.month, name='month'),
                  path('faculty/month', views.month, name='month'),

                  path('F_login/viewA', views.viewA, name='viewA'),
                  path('viewA', views.viewA, name='viewA'),
                  path('faculty/viewA', views.viewA, name='viewA'),

              ] + static(settings.STATIC_URL, documeent_root=settings.STATIC_ROOT)
