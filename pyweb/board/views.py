from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from board.models import Question
from board.forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'board/index.html')

# 질문 등록
@login_required(login_url='common:login')
def question_list(request):
    #question_list = Question.objects.all()
    question_list = Question.objects.order_by('create_date') # 내림차순
    context ={'question_list':question_list}
    return render(request, 'board/question_list.html', context)

def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    # 포털에서 데이터가 없으면 가져오고 없으면 404 페이지 오류 처리를 함
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'board/detail.html', context)

def question_create(request):
        if request.method == 'POST':
            form = QuestionForm(request.POST) # 입력된 데이터가 있는 폼
            if form.is_valid(): # 폼이 유효하다면(유효성 검사를 통과했다면)
                question = form.save(commit=False) # 가저장
                question.author = request.user # 세션 권한(로그인한)있는 글쓴이
                question.create_date = timezone.now() # 등록일 생성
                form.save() # 실제 저장
                return redirect('board:question_list') # 질문 목록 페이지로 이동

        else:
            form = QuestionForm() # 폼 객체 생성 (빈 폼 생성)
            context ={'form': form}

        return render(request, 'board/question_form.html', context) #get 방식

# 답변 등록
@login_required(login_url='common:login')
def answer_create(request, question_id):
    # 질문이 1개 있어야 답변을 등록할 수 있음
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST': #POST를 소문자로 작성 시 작동안함
        form = AnswerForm(request.POST)
        if form.is_valid(): # 유효성 검사
            answer = form.save(commit=False) # 가저장(content)
            answer.author = request.user # 로그인한 사람
            answer.create_date = timezone.now() # 답변 등록일 생성
            answer.question = question # 외래키 저장
            answer.save() # 실제 저장
            return redirect('board:detail', question_id=question.id)
    else:
        form = AnswerForm() # 빈 폼 생성
        context = {'question': question, 'form':form}
    return render(request, 'board/detail.html', context)

# 질문 삭제
@login_required(login_url='common:login')
def question_delete(request, question_id):
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('board:question_list')