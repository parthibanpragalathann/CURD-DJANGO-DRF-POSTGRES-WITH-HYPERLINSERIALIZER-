from django.db import models

# Created DRONE models here.
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


