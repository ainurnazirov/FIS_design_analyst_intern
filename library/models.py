from django.db import models


class author (models.Model):
    last_name = models.CharField(max_length=70)
    first_name = models.CharField(max_length=70)
    patronymic = models.CharField(max_length=70)

class publishing_house (models.Model):
    title = models.CharField(max_length=255)

class book (models.Model):
    title = models.CharField(max_length=70)
    id_author = models.ForeignKey(author, on_delete=models.PROTECT)
    id_publish = models.ForeignKey(publishing_house, on_delete=models.PROTECT)
    publish_year = models.IntegerField()
    count = models.IntegerField()

class student (models.Model):
    last_name = models.CharField(max_length=70)
    first_name = models.CharField(max_length=70)
    patronymic = models.CharField(max_length=70)

class book_issue (models.Model):
    id_book = models.ForeignKey(book, on_delete=models.PROTECT)
    id_student = models.ForeignKey(student, on_delete=models.PROTECT)
    issue_date = models.DateField(auto_now=False, auto_now_add=False)

class book_return (models.Model):
    id_issue = models.ForeignKey(book_issue, on_delete=models.PROTECT)
    return_date = models.DateField(auto_now=False, auto_now_add=False)
