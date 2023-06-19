from django.db import models
from django.utils import timezone

class Question(models.Model):
    # 필드
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self): # 객체 정보를 문자열로 반환
        return self.question_text

#항목 테이블 (엔티티)

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

def __str__(self):
    return self.choice_text

