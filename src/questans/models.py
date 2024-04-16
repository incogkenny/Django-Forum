from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Questions(models.Model):
    #fields and other data
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.TextField()
    description = models.TextField(null=True, blank=True)
    points = models.IntegerField(default=0)
    group = models.ForeignKey('QuestionGroups', on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    #creates a slug of from the title of a Question
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Questions, self).save(*args, **kwargs)

    #changes unicode within admin page to object 'title'
    def __unicode__(self):
        return self.title
    #changes str within admin page to object 'title'
    def __str__(self):
        return self.title


class Answers(models.Model):
    #fields and other data
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #takes in the id of the question that is being answered
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    #users entered answer
    answer = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    is_anonymous = models.BooleanField(default=False)


    def __unicode__(self):
        return self.id


class QuestionGroups(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

class QGroups(models.Model):
    all_groups = QuestionGroups.objects.values()
    GROUP_CHOICES = [(d['id'], 'Photosynthesis') for d in all_groups]