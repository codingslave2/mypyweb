from django.urls import path
from board import views

app_name = 'board' # 만들고 m-name 방식으로 생성 가능

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('question/create/', views.question_create, name='question_create'), # 질문 등록
    path('answers/create/<int:question_id>/', views.answer_create, name='answer_create'), # 답변 등록
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete')
]


