from django.db import models


class Article (models.Model):
    title = models.CharField('title', max_length=200)
    content = models.TextField('content')
    pub_date = models.TextField('publication date')


class Comment (models.Model):
    article = models.ForeignKey(Article, on_delete= models.CASCADE)
    author = models.CharField('author', max_length=50)
    text = models.CharField('text', max_length= 500)