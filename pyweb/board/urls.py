from django.urls import path
from board import views

app_name = 'board' # 만들고 m-name 방식으로 생성 가능

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('question/create/', views.question_create, name='question_create'), # 질문 등록
    path('answers/create/<int:question_id>/', views.answer_create, name='answer_create'), # 답변 등록
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'), # 질문 수정
    #path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'), # 답변 수정
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'), # 질문 삭제
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete') # 답변 삭제
]


