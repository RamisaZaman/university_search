from django.db import models

class University(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    ranking = models.IntegerField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class Professor(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    research_area = models.CharField(max_length=255)
    email = models.EmailField()
    profile_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.university.name})"
