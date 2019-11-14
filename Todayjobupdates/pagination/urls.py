"""pagination URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from app import views
from pagination import settings

from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.loginPage,name="main"),
    path("savedetails/",views.savedetails,name="savedetails"),
    path("verityuser/",views.verityuser,name="verityuser"),
    path("welcome/",views.homepage,name="welcome"),

    path("postjob/",views.postjob,name='postjob'),
    path("savejob/",views.savejob,name="savejob"),

    path("viewjobs/",views.viewjobs,name="viewjobs"),

    path("logout/",views.logout,name="logout"),
    path("forgotpassword/",views.forgotpassword,name="forgotpassword"),
    path("updatedpassword/",views.updatedpassword,name="updatedpassword"),


    path("profile/",views.profile,name="profile"),

    path("offcampusdrive/",views.offcampusdrive,name="offcampusdrive"),
    path("walkindrive/",views.walkindrive,name="walkindrive"),
    path("experiancejobs/",views.experiancejobs,name="experiancejobs"),
    path("passout2020/", views.passout2020, name="passout2020"),
    path("passout2019/", views.passout2019, name="passout2019"),
    path("passout2018/", views.passout2018, name="passout2018"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
