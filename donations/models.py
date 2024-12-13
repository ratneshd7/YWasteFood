from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Food Donation Model
class food_donation(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Picked', 'Picked'),
        ('About to Be Picked', 'About to Be Picked'),
        ('Received', 'Received'),
        ('Delivered', 'Delivered'),
        ('Declined', 'Declined'),
    )

    d_user = models.ManyToManyField(User)
    quantity = models.IntegerField(null=True)
    description = models.TextField(null=True)
    status = models.CharField(max_length=20, null=True,
                              choices=STATUS, default='Pending')
    date_donated = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('-date_donated',)

    # def __str__(self):
    #     return f'{self.d_user}\'s Food Donation'
    
class foodInventory(models.Model):
    for_people = models.IntegerField(null=True)
