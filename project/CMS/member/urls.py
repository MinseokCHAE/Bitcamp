from CMS.member import views_new, views
from django.conf.urls import url

urlpatterns = [
    url(r'^signup', views.Members_post),
    url(r'^list', views_new.members),
    url(r'^login', views_new.members)

]
