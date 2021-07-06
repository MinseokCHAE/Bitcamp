from CMS.member import views_new, views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    url(r'^signup', views_new.members),
    url(r'^list', views_new.members),
    url(r'^login', views_new.login),
    url(r'^edit', views_new.member_modify),
    path('delete/<slug:pk>', views_new.member),

]
