from django.conf.urls import url
from .views import ReuserView
urlpatterns = [
    url(r'register/$',ReuserView.as_view())
]