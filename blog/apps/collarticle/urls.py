from django.conf.urls import url
from .views import CountView

urlpatterns = [

    url(r'count/$',CountView.as_view())

]