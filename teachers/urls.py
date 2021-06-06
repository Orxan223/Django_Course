from django.urls import path, include
from .views import TeacherListView

urlpatterns = [
    path('', TeacherListView.as_view(), name='teachers'),
  

]
