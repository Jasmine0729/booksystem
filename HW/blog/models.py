from django.db import models

class Author(models.Model):
    AuthorID=models.IntegerField(primary_key = True)
    Name=models.CharField(max_length = 30)
    Age=models.CharField(max_length = 30)
    Country=models.CharField(max_length = 30)

class Book(models.Model):
    ISBN=models.CharField(max_length = 30,primary_key = True)
    Title=models.CharField(max_length = 30)
    AuthorID=models.ForeignKey(Author)
    Publisher=models.CharField(max_length = 50)
    PublishDate=models.DateField()
    #Price=models.CharField(max_length = 20)