from django.urls import path
from . import views

urlpatterns = [
    path("get-quiz/<int:id>/", views.getQuiz, name="getQuiz"),
    path("quiz-detail/<int:id>/", views.quizDetail, name="quiz_detail"),
    path("make-answer/<int:id>/", views.makeAnswer, name="makeAnswer"),
    path("results/", views.results, name="results"),
    path("result-detail/<int:id>/", views.result_detail, name="resultDetail"),
    path(
        "result-deatil-excel/<int:id>/",
        views.answerDetailExcel,
        name="resultDetailExcel",
    ),
]
