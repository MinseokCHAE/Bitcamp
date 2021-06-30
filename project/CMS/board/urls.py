from django.conf.urls import url
from .views import Boards_post


urlpatterns = [url('/postwrite', Boards_post.as_view())]
