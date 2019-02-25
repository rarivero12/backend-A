from django.urls import path

from . import views


app_name = 'portafolio'

urlpatterns = [
    path('hello/', views.index, name='index'),
    path("polls/", views.polls_list, name="polls_list"),
    path("polls/<int:pk>/", views.polls_detail, name="polls_detail")
]
