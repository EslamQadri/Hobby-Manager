from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


DAY_CHOICES = (
    ("monday", "Monday"),
    ("tuesday", "Tuesday"),
    ("wednesday", "Wednesday"),
    ("thursday", "Thursday"),
    ("friday", "Friday"),
    ("saturday", "Saturday"),
    ("sunday", "Sunday"),
)


# Create your models here.
class Hobby(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hobby = models.CharField("Titel", max_length=250)
    note = models.TextField(blank=True, null=True)
    days_of_hobby = MultiSelectField(choices=DAY_CHOICES, max_choices=7, max_length=56)

    def __str__(self) -> str:
        return f"{self.user.username } {self.hobby}"


class HobbyProgress(models.Model):
    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE)
    day = models.CharField("day", max_length=9, choices=DAY_CHOICES)
    is_completed = models.BooleanField("cheek", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.hobby.hobby}"
