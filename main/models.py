from django.db import models

# Create your models here.
class Property(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=350)
    slug = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=100)
    price = models.IntegerField()
    price_in = models.CharField(max_length=10)
    area_sqft = models.IntegerField()
    plot_or_house_or_flat = models.CharField(max_length=5)
    floors = models.IntegerField(default=1, blank=True, null=True)
    bedroom = models.IntegerField(blank=True, null=True)
    bathroom = models.IntegerField(blank=True, null=True)
    balcony = models.IntegerField(blank=True, null=True)
    img1 = models.ImageField(default="")
    img2 = models.ImageField(default="")
    img3 = models.ImageField(default="")
    img4 = models.ImageField(default="")
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title + ' - ' + self.location

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=13)
    messege = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Messege from ' + self.name + ' - ' + self.email