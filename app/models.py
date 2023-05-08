from djongo import models

class Comment(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    comment = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)