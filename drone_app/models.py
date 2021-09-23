from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager



# Created DRONE models here.

# Choose User Roles
user_role_type = ((1, "level1"), (2, "level2"), (3, "level3"))   #Type of User Role.

# Choose Gender
gender_choice = [
    (1, "Male"),
    (2, "Female"),
    (3, "Transgender")
]
# Choose Participate or not

participate_choice = [
    ("participate", "Participate"),
    ("not participate", "Not Participate")
]


class CustomUser(AbstractUser):                 #Authentication user model.
        username = models.CharField(max_length=150)
        password = models.CharField(max_length=150)
        password2 = models.CharField(max_length=150)
        email = models.EmailField(_('email address'), unique=True)
        first_name = models.CharField(max_length=150)
        last_name = models.CharField(max_length=150)

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

        objects = CustomUserManager()

        def __str__(self):
            return self.email


# Drone categories ( DroneCategory model)
class DronesCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Drones ( Drone model)
class Drones(models.Model):
    name = models.CharField(max_length=50)
    drone_category = models.ForeignKey(DronesCategory, on_delete=models.CASCADE)
    manufacture_date = models.DateField()
    is_participated = models.CharField(choices=participate_choice, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Pilots ( Pilot model)
class Pilots(models.Model):
    name = models.CharField(max_length=50)
    gender = models.IntegerField(choices=gender_choice)
    number_race = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Competitions ( Competition model)
class Competitions(models.Model):
    drone = models.ForeignKey(Drones, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilots, on_delete=models.CASCADE)
    distance = models.IntegerField(blank=False, default=0)
    date = models.DateTimeField()


