from django.db import models


class DataModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(DataModel):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)


class Book(DataModel):
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Publisher(DataModel):
	name = models.CharField(max_length=255)
	books = models.ManyToManyField(Book, related_name="publishers")
