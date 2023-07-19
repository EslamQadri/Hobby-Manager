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
    print(users)

    for user in users:
        hobbys = Hobby.objects.filter(user=user)
        for hobby in hobbys:
            days_of_hobby = hobby.days_of_hobby
            for day in days_of_hobby:
                print(day == theday.lower())

