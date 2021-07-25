from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from core import models as core_models

# from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """RoomType Model Definition"""

    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):

    """Amenity Model Definition"""

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """Facility Model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """HouseRule Model Definition"""

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    """Room Model Definition"""

    name = models.CharField(max_length=140)

    description = models.TextField()

    country = CountryField()

    city = models.CharField(max_length=80)

    price = models.IntegerField()

    address = models.CharField(max_length=140)

    guests = models.IntegerField()

    beds = models.IntegerField()

    bedrooms = models.IntegerField()

    baths = models.IntegerField()

    check_in = models.TimeField()

    check_out = models.TimeField()

    instant_book = models.BooleanField(default=False)

    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    # User에 있는 내용을 import해서 사용하기 위함... FK를 이용해서 User와 Room을 연결함.
    # room은 many이지만 host는 one
    # related_name = 은 foreign key의 대상이 당신의 element에 접근할 수 있도록 해주는 것이다.

    room_type = models.ForeignKey(
        "RoomType",
        related_name="rooms",
        on_delete=models.SET_NULL,
        null=True,
    )

    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)

    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)

    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews), 2)
        return 0
