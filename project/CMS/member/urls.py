from CMS.member import views_new
from django.conf.urls import url

urlpatterns = [
    url(r'^signup', views_new.members),
    url(r'^list', views_new.members)

]
