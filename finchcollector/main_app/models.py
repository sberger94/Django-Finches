from django.db import models
from django.urls import reverse

# Create your models here.
SPOTTED = (
    ('N', 'North America'),
    ('S', 'South America'),
    ('A', 'Africa'),
    ('E', 'Europe'),
    ('S', 'Asia'),
    ('U', 'Australia'),
    ('T', 'Antarctica'),
)

class Finch(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

class Spotted(models.Model):
    date = models.DateField('spotted on')
    location = models.CharField(
        max_length=1,
        choices=SPOTTED,
        default=SPOTTED[0][0]
        )

    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"Spotted in {self.get_location_display()} on {self.date}"