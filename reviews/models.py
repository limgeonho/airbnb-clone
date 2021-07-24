from django.db import models
from django.db.models.deletion import CASCADE
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()

    accuracy = models.IntegerField()

    communication = models.IntegerField()

    cleanliness = models.IntegerField()

    location = models.IntegerField()

    check_in = models.IntegerField()

    value = models.IntegerField()

    user = models.ForeignKey("users.User", related_name="reviews", on_delete=CASCADE)

    room = models.ForeignKey("rooms.Room", related_name="reviews", on_delete=CASCADE)

    def __str__(self):
        return f"{self.review} - {self.room}"

    def rating_average(self):
        # model에 함수를 만드는 이유는 admin에 만들면 admin에서만 볼 수 있지만 다른 페이지에서도 사용자들에게도 보여주고 활용하기 위해서...
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 2)

    rating_average.short_description = "Avg."
