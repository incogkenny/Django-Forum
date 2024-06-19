# Import necessary modules from Django and the project
from django.contrib import admin
from .models import Questions, Answers, QuestionGroups


# Define an inline admin interface for Answers
class AnswerInline(admin.TabularInline):
    model = Answers  # Link the inline admin to the Answers model


# Define an admin interface for Questions
class QuestionsAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]  # Include the Answers inline admin in the Questions admin

    class Meta:
        model = Questions  # Link the admin to the Questions model


# Define an admin interface for Answers
class AnswersAdmin(admin.ModelAdmin):
    class Meta:
        model = Answers  # Link the admin to the Answers model


# Define an admin interface for QuestionGroups
class QuestionGroupsAdmin(admin.ModelAdmin):
    class Meta:
        model = QuestionGroups  # Link the admin to the QuestionGroups model


# Register the admin interfaces with the Django admin site
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(QuestionGroups, QuestionGroupsAdmin)
admin.site.register(Answers, AnswersAdmin)
