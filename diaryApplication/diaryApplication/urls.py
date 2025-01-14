"""
URL configuration for diaryApplication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from diary.views import home_page,add_new_entry,fetch_entries,fetch_individual_diary_entry,not_found
handler404 = not_found

urlpatterns = [
    path('',home_page),
    path('diary/<int:id>/', fetch_individual_diary_entry),
    path('add-new-entry',add_new_entry),
    path('view-entries',fetch_entries),
    path('admin/', admin.site.urls),
    
]
