from app.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import connection
from pprint import pprint

# def run():
#     restaurant = Restaurant()
#     restaurant.name = 'My Indian Restaurant'
#     restaurant.latitude = 52.3
#     restaurant.longitude = 65.7
#     restaurant.date_opened = timezone.now()
#     restaurant.restaurant_type = Restaurant.TypeChoices.INDIAN

#     restaurant.save()

# def run():
#     restaurants = Restaurant.objects.all()
#     print(restaurants)

#     print(connection.queries)


# def run():
#     Restaurant.objects.create(
#         name = "Pizza World",
#         date_opened = timezone.now(),
#         restaurant_type = Restaurant.TypeChoices.ITALIAN,
#         latitude = 23.6,
#         longitude = 59.0
#     )

#     print(connection.queries)


# def run():
#     restaurant = Restaurant.objects.first()
#     user = User.objects.first()
#     Rating.objects.create(user=user, restaurant = restaurant, ratings = 3)

#     print(connection.queries)


# def run():
#     rating = Rating.objects.first()
#     print(rating.restaurant)

#     pprint(connection.queries)


# def run():
#     restaurant = Restaurant.objects.first()
#     # print(restaurant.rating_set.all())         # Reverse Relation, if want to override rating_set then write 'related_name' in foreign field
#     print(restaurant.ratings.all())     # Now use related name
#     # pprint(connection.queries)



# def run():
#     Sale.objects.create(
#         restaurant = Restaurant.objects.first(),
#         income = 5.33,
#         datetime = timezone.now()
#     )
#     Sale.objects.create(
#         restaurant = Restaurant.objects.first(),
#         income = 8.42,
#         datetime = timezone.now()
#     )
#     Sale.objects.create(
#         restaurant = Restaurant.objects.first(),
#         income = 6.85,
#         datetime = timezone.now()
#     )



def run():
    restaurant = Restaurant.objects.first()
    print(restaurant.sales.all())                   # sales is a related name