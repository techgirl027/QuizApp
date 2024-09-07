from django.urls import path, include
from app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_, name="login"),
    path("register/", views.register, name="register"),
    path("answer-detail/<int:id>/", views.answerDetail, name="answerDetail"),
    path("quiz-list/", views.quizList, name="quizList"),
    path("all-quiz-list/", views.allQuizList, name="allQuizList"),
    path("quiz-detail/<int:id>/", views.quizDetail, name="quizDetail"),
    path("quiz-list-detail/<int:id>/", views.quizListDetail, name="quizListDetail"),
    path("quiz-list-excel/<int:id>/", views.quizListDetailExcel, name="quizDeailExcel"),
    path(
        "questionDelete/<int:id>/<int:pk>/", views.questionDelete, name="questionDelete"
    ),
    path(
        "optionDelete/<int:ques>/<int:option>/", views.deleteOption, name="optionDelete"
    ),
    path("question-detail/<int:id>/", views.questionDetail, name="questionDetail"),
    path("create-quiz/", views.create_quiz, name="createQuiz"),
    path("create-question/<int:id>/", views.questionCreate, name="questionCreate"),
]
