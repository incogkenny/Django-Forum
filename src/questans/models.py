# Import necessary modules from Django and the project
from django.db import models
from django.conf import settings
from django.utils.text import slugify


# Define a model for Questions
class Questions(models.Model):
    # Define the fields for the model
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.TextField()
    description = models.TextField(null=True, blank=True)
    points = models.IntegerField(default=0)
    group = models.ForeignKey('QuestionGroups', on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    # Override the save method to create a slug from the title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Questions, self).save(*args, **kwargs)

    # Override the unicode method to return the title
    def __unicode__(self):
        return self.title

    # Override the str method to return the title
    def __str__(self):
        return self.title


# Define a model for Answers
class Answers(models.Model):
    # Define the fields for the model
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    is_anonymous = models.BooleanField(default=False)

    # Override the unicode method to return the id
    def __unicode__(self):
        return self.id


# Define a model for QuestionGroups
class QuestionGroups(models.Model):
    name = models.CharField(max_length=100)

    # Override the unicode method to return the name
    def __unicode__(self):
        return self.name

    # Override the str method to return the name
    def __str__(self):
        return self.name


# Define a model for QGroups
class QGroups(models.Model):
    all_groups = QuestionGroups.objects.values()
    GROUP_CHOICES = [(d['id'], 'Photosynthesis') for d in all_groups]
