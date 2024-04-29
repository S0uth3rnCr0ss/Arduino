from django.urls import path, include
from .views import postUNOdata
# fetchData

urlpatterns = [path("postdata/", postUNOdata)]
            #    path("fetchData/",fetchData)]
