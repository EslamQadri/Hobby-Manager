from hobby.models import Hobby, HobbyProgress
from django.contrib.auth.models import User
from datetime import datetime

theday = datetime.now().strftime("%A")  # Get the full name of the day (e.g., "Monday")

from django.http.response import HttpResponse


def create_hobby_prograss():
    """
    to create a daily hobbys
    """
    users = User.objects.all()

    for user in users:
        hobbys = Hobby.objects.filter(user=user, days_of_hobby__contains=theday.lower())
        for hobby in hobbys:
            HobbyProgress.objects.create(hobby=hobby, day=theday.lower())
            print(
                f"created  by {user.username} and hobby name is {hobby.hobby} and the day is {theday.lower()}"
            )
        # for hobby in hobbys:
