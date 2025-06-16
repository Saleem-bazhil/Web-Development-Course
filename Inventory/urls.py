from django.urls import path, include
from .views import *

urlpatterns = [
    path("home/", home),
    path("main/", main),
    path("courses/", Courses),
    path("html/", Htmlpage),
    path("css/", Csspage),
    path("js/", JavacriptPage),
    path("bootstrap/", BootstrapPage),
    path("react/", React),
    path("python/", Python),
    path('django/',Django),
]
