from django.db import models

class AcademicProject(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the project title")
    description = models.TextField(help_text="Enter the project description")
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
