from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100) # 제목
    content = models.TextField() # 내용
    pub_date = models.DateTimeField(auto_now_add=True) # 생성일
    modify_date = models.DateTimeField(auto_now=True) # 입력 폼이 비어도
    photo = models.ImageField(upload_to='blog/post/%Y/%m/%d/', null=True, blank=True) # null 허용, 파일 첨부 안할 때도 있음


    def __str__(self):
        return self.title