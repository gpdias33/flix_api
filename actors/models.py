from django.db import models


NATIONALITY_CHOICES = (
    ('US', 'United States'),
    ('UK', 'United Kingdom'),
    ('CA', 'Canada'),
    ('AU', 'Australia'),
    ('FR', 'France'),
    ('DE', 'Germany'),
    ('IN', 'India'),
    ('JP', 'Japan'),
    ('BR', 'Brazil'),
    ('Other', 'Other'),
)

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(choices=NATIONALITY_CHOICES, max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name