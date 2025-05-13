# Third party
# hacky trick to add python2 compatibility to a python3 project after python2 eol
from django.urls import path

# Local application / specific library imports
from . import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="Index")
]
