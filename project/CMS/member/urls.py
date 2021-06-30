from django.conf.urls import url
from .views import Members_post


urlpatterns = [url('/signup', Members_post.as_view())]
