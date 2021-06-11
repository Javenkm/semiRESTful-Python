from django.db import models

# Create your models here.

class Shows(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    releaseDate = models.DateTimeField()
    description = models.CharField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ShowManager()


class ShowManager(models.Model):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) > 25:
            error["title"] = "Title should not be more than 25 characters"
        if len(postData['description']) < 10:
            errors["description"] = "Description should be at least 10 characters in length"
        return errors