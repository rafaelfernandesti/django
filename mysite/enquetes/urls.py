from django.urls import path
from . import views

app_name = "enquetes"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/",views.detail, name="detail"),
    path("<int:question_id>/results/",views.results, name="resultados"),
    path("<int:question_id>/vote/",views.vote, name="vote"),
]
